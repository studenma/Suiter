import json
import logging
logger = logging.getLogger(__name__)

from exceptions import *
import suiter_classes_and_globals as globe
from combine_request import api_call_combine, evaluate_combine_response, add_parameter_to_combine_call, add_indexes_of_parameter_to_combine_call
from general import replace_the_tag_with_value, get_file_content

def find_between(string, start_tag, end_tag, replace_with_start, replace_with_end):
    """ Return the substring + the original string without this substring """
    try:
        # get the index-range of content between start_tag and end_tag
        get_from = string.index(start_tag) + len(start_tag)
        get_to = string.index(end_tag, get_from)
        # get the content of it
        content = string[get_from:get_to]

        # remove this start and end tag and replace it with non-priority ones (doesn't really matter which one is used, but it has to be unified)
        modified_string = string[:(get_from-len(start_tag))] + replace_with_start + replace_with_end + string[(get_to+len(end_tag)):]

        # get the position of already evaluated part of string (this function is going to be called more than a once for the same string)
        # So, next iteration has to start from this position, otherwise it will find the same tag
        position = get_from-len(start_tag) + len(replace_with_start) + len(replace_with_end)
    except ValueError:
        message = "Some of the tag was probably not ended"
        raise EndpointSemanticError(__name__, "find_between", message)

    return (modified_string, content, position)

def tag_substring_evaluation(tag1, tag2):
    """
    Return a more important tag:
        if the first variable is the substring of the second one: return tuple (tag2,tag1)
        if the second variable is the substring of the first one: return tuple (tag1,tag2)
    Return None if none of them are substrings
    """
    logging.debug('Evaluating the tag substrings: {} and {}'.format(tag1, tag2))
    if tag1 == tag2:
        message = "The start tag '{}' and it's end '{}' can not be the same".format(tag1,tag2)
        raise ConfigurationFileError(__name__, "conf_variabletag_substring_evaluation_substring_evaluation", message)
    elif tag1 in tag2:
        return (tag2,tag1)
    elif tag2 in tag1:
        return (tag1,tag2)
    else:
        None

def general_string_parser(content_string, location):
    """ 
    Parse the given string of header/url content 
    * search for all parameters in this string
    * evaluate what type of parameter it is:
        ** enumerate type
        ** global variable type
        ** local variable type
    * add these parameteres to a 'globe.all_parameters'
    * all params are replaced with a starting and ending symbol of non priority tag
    Return a tuple:
        * modified string -> every parameter is replaced with a low-prio start and end tag 
            ** before: https://mydomain/addUser/<:user:>/<>/<1,2,3,4,5>/<:used:>
            ** after:  https://mydomain/addUser/<>/<>/<>/<>
            # before:  {'Content-type': '<123,456>', '<>': '<:var:>'}
            # after:   {'Content-type': '<>', '<>': '<>'}
        * list of found parameters:
        [
            {'location': $location, 'type': 'global_variable', 'name': 'user', 'id': 0}
            {'location': $location, 'type': 'global_variable', 'name': 'used', 'id': 1}
            {'location': $location, 'type': 'local_variable', 'id': 2}
            {'location': $location, 'type': 'enumerate', 'content': 'ABC', 'id': 3}
            {'location': $location, 'type': 'enumerate', 'content': '1,2,3,4,5', 'id': 4}
            
        ]
    """
    logging.debug('Calling the general_string_parser function with a following parameters: [{}, {}]'.format(content_string, location))

    # if the location is endpoint -> the varaibles in global class are stored as 'url', not 'endpoint'
    if location == "endpoint":
        globe_location = 'url'
    else:
        # otherwise it is the same name as in the location variable passed by function parameter
        globe_location = location
    
    # starting and ending variables
    enum_start_tag = getattr(globe.config, globe_location).enum.start
    enum_end_tag = getattr(globe.config, globe_location).enum.end
    variable_start_tag = getattr(globe.config, globe_location).variable.start
    variable_end_tag = getattr(globe.config, globe_location).variable.end
    # prio and non prio variables
    prio_start_tag = getattr(globe.config, globe_location).priority_start
    prio_end_tag = getattr(globe.config, globe_location).priority_end
    non_prio_start_tag = getattr(globe.config, globe_location).non_priority_start
    non_prio_end_tag = getattr(globe.config, globe_location).non_priority_end
    # list of all parameters in given string
    parameters = []

    """
    Search for all parameters in header/url
    variables:
        * e_idx     = index of location, where the enumerate start tag was found
        * v_idx     = index of location, where the variable start tag was found
        * position  = indicates the location of pointer in string (to avoid searching tags which were already been found)
        * globe.param_id_counter = current parameter id (global varaible - is reseted to 0 after every combine call)
        * globe.all_parameters   = list of all parameters collected (reseted after every combine call) 
    used functions:
        * find_between() = to get the content in between starting and ending tag
            ** returns: 
    """
    position = 0
    # the first search of enumerate and varaible starting tags in string
    e_idx = content_string.find(enum_start_tag)
    v_idx = content_string.find(variable_start_tag)
    # end this loop when no more starting tags were found
    while e_idx != -1 or v_idx != -1:   
        """
        If the ENUM and VARIABLE indexes were found in the same index
        -> it means one of them is substring of another one
        The non substring one has always the priority (priority tags in config class)
        """
        if e_idx == v_idx:
            if prio_start_tag == enum_start_tag:
                """
                Modify contnet_string for current parameter
                Get the content of current parameter
                Count the position for next search
                """
                # get (modified_content_string, content, position)
                resulted_tuple = find_between(content_string[position:], enum_start_tag, enum_end_tag, non_prio_start_tag, non_prio_end_tag)
                temp = content_string
                content_string = content_string[:position] + resulted_tuple[0]
                content = resulted_tuple[1]
                position = len(temp[:position]) + resulted_tuple[2]

                # check if the content is empty string -> it is a local variable
                # otherwise it is enumerate type
                if len(content) == 0:
                    p = {"location": location, "type": "local_variable", "id": globe.param_id_counter}
                else:
                    p = {"location": location, "type": "enumerate", "content": content, "id": globe.param_id_counter}
                
                # add the information about this parameter to a reulted array
                parameters.append(p)

                """
                Evaluate which tag was already evaluated
                If e_idx or v_idx was evaluated, the next occurence have to be searched
                In this case the indexes are the same -> have to search new idx for both
                """
                e_change = e_idx
                v_change = v_idx
            elif prio_start_tag is variable_start_tag:
                """
                Modify content_string for current parameter
                Get the content of current parameter (variable)
                Count the position for next search
                """
                # get (modified_content_string, content, position)
                resulted_tuple = find_between(content_string[position:], variable_start_tag, variable_end_tag, non_prio_start_tag, non_prio_end_tag)
                temp = content_string
                content_string = content_string[:position] + resulted_tuple[0]
                variable = resulted_tuple[1]
                position = len(temp[:position]) + resulted_tuple[2]
                p = {"location": location, "type": "global_variable", "name": variable, "id": globe.param_id_counter}

                # add the information about this parameter to a reulted array
                parameters.append(p)

                """
                Evaluate which tag was already evaluated
                If e_idx or v_idx was evaluated, the next occurence have to be searched
                In this case the indexes are the same -> have to search new idx for both
                """
                v_change = v_idx
                e_change = e_idx
            else:
                message = "Should have never gotten here"
                raise EndpointSemanticError(__name__, "general_string_parser", message)
        else:
            if e_idx < v_idx:
                """
                Unless the e_idx == -1
                -> e_idx should be evaluated before v_idx
                -> v_idx will stay the same, new e_idx will be search then
                """
                if e_idx == -1:
                    """
                    Modify content_string for current parameter
                    Get the content of current parameter (variable)
                    Count the position for next search
                    """
                    # get (modified_content_string, content, position)
                    resulted_tuple = find_between(content_string[position:], variable_start_tag, variable_end_tag, non_prio_start_tag, non_prio_end_tag)
                    temp = content_string
                    content_string = content_string[:position] + resulted_tuple[0]
                    variable = resulted_tuple[1]
                    position = len(temp[:position]) + resulted_tuple[2]
                    p = {"location": location, "type": "global_variable", "name": variable, "id": globe.param_id_counter}
                    
                    # add the information about this parameter to a reulted array
                    parameters.append(p)

                    """
                    Evaluate which tag was already evaluated
                    If e_idx or v_idx was evaluated, the next occurence have to be searched
                    In this case only the new v_idx should be searched 
                    (e_idx will be search as well, but from a v_idx starting point) -> algorithm will find the same as before
                    """
                    v_change = v_idx
                    e_change = v_idx
                else:
                    """
                    Modify content_string for current parameter
                    Get the content of current parameter (content)
                    Count the position for next search
                    """
                    # get (modified_content_string, content, position)
                    resulted_tuple = find_between(content_string[position:], enum_start_tag, enum_end_tag, non_prio_start_tag, non_prio_end_tag)
                    temp = content_string
                    content_string = content_string[:position] + resulted_tuple[0]
                    content = resulted_tuple[1]
                    position = len(temp[:position]) + resulted_tuple[2]

                    # check if the content is empty string -> it is a local variable
                    # otherwise it is enumerate type
                    if len(content) == 0:
                        p = {"location": location, "type": "local_variable", "id": globe.param_id_counter}
                    else:
                        p = {"location": location, "type": "enumerate", "content": content, "id": globe.param_id_counter}

                    # add the information about this parameter to a reulted array
                    parameters.append(p)
                    
                    """
                    Evaluate which tag was already evaluated
                    If e_idx or v_idx was evaluated, the next occurence have to be searched
                    In this case only the new e_idx should be searched 
                    (v_idx will be search as well, but from a e_idx starting point) -> algorithm will find the same as before
                    """
                    e_change = e_idx
                    v_change = e_idx
            elif v_idx < e_idx:
                """
                Unless the v_idx == -1
                -> v_idx should be evaluated before e_idx
                -> e_idx will stay the same, new v_idx will be search then
                """
                if v_idx == -1:
                    """
                    Modify content_string for current parameter
                    Get the content of current parameter (content)
                    Count the position for next search
                    """
                    # get (modified_content_string, content, position)
                    resulted_tuple = find_between(content_string[position:], enum_start_tag, enum_end_tag, non_prio_start_tag, non_prio_end_tag)
                    temp = content_string
                    content_string = content_string[:position] + resulted_tuple[0]
                    content = resulted_tuple[1]
                    position = len(temp[:position]) + resulted_tuple[2]

                    # check if the content is empty string -> it is a local variable
                    # otherwise it is enumerate type
                    if len(content) == 0:
                        p = {"location": location, "type": "local_variable", "id": globe.param_id_counter}
                    else:
                        p = {"location": location, "type": "enumerate", "content": content, "id": globe.param_id_counter}

                    # add the information about this parameter to a reulted array
                    parameters.append(p)

                    """
                    Evaluate which tag was already evaluated
                    If e_idx or v_idx was evaluated, the next occurence have to be searched
                    In this case only the new e_idx should be searched 
                    (v_idx will be search as well, but from a e_idx starting point) -> algorithm will find the same as before
                    """
                    e_change = e_idx
                    v_change = e_idx
                else:
                    """
                    Modify content_string for current parameter
                    Get the content of current parameter (content)
                    Count the position for next search
                    """
                    # get (modified_content_string, content, position)
                    resulted_tuple = find_between(content_string[position:], variable_start_tag, variable_end_tag, non_prio_start_tag, non_prio_end_tag)
                    temp = content_string
                    content_string = content_string[:position] + resulted_tuple[0]
                    variable = resulted_tuple[1]
                    position = len(temp[:position]) + resulted_tuple[2]
                    p = {"location": location, "type": "global_variable", "name": variable, "id": globe.param_id_counter}
                    
                    # add the information about this parameter to a reulted array
                    parameters.append(p)

                    """
                    Evaluate which tag was already evaluated
                    If e_idx or v_idx was evaluated, the next occurence have to be searched
                    In this case only the new v_idx should be searched 
                    (e_idx will be search as well, but from a v_idx starting point) -> algorithm will find the same as before
                    """
                    v_change = v_idx
                    e_change = v_idx
            else:
                message = "Should have never gotten here"
                raise EndpointSemanticError(__name__, "general_string_parser", message)

        """
        WHILE EVALUATION
        Find the first occurence of ENUM start tag or VARIABLE start tag
        in the next iteration of while, the already evaluated part of content_string is ignored
        (e_change+1 and v_change+1 means it starts to search from this index)
        if nothing is found -> -1 is returned
        """
        e_idx = content_string.find(enum_start_tag, e_change+1)
        v_idx = content_string.find(variable_start_tag, v_change+1)
        globe.param_id_counter += 1
    
    return content_string,parameters

def remove_single_values_params(taged_string, param_array, location):
    """ Remove the single values parameters and replace odpovidajici tag ve stringu """
    # TODO: this function is not tested at all -> just with one use case
    single_params_array = []
    combine_params_array = []  
    param_array_size = len(param_array)

    # print("---- JSEM NA ZACATKU ---")
    # print(taged_string)
    # for element in param_array:
    #     print(element)
    # print(location)
    """
    Decide which tag should be replaced - endpoint, method, body and header may have different non-priority tag
    Taged string is taged with a non-priority tag
    This function is called only with a param_array with the same locations
    """
    if location == 'endpoint':
        tag = str(globe.config.url.non_priority_start) + str(globe.config.url.non_priority_end)
    elif location == 'method':
        tag = str(globe.config.method.non_priority_start) + str(globe.config.method.non_priority_end)
    elif location == 'header':
        tag = str(globe.config.header.non_priority_start) + str(globe.config.header.non_priority_end)
    elif location == 'body':
        tag = str(globe.config.body.non_priority_start) + str(globe.config.body.non_priority_end)
    else:
        raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")

    # pop all values from param_array one by one
    param_idx = 0 # this idx indcates on which occurence in struing the tag should be replaced -> it is neccessary to be here
    while len(param_array) != 0:
        parameter = param_array.pop(0)
        """
        Decide what type of parameter is this one - should be the same for all array which is sent
        """
        if parameter['type'] == 'global_variable':
            """ GLOBAL VARIABLE """
            # if there is 'value' key -> it is a global variable with a already existing value
            if 'value' in parameter.keys():
                # so, it should be removed and replaced
                single_params_array.append(parameter)
                # TODO: replace the value in string
            else:
                # check if the 'reserved' element does exist (the global variable has already been added)
                if ('reserved' in parameter.keys()) and (parameter['reserved'] == True):
                    # if the 'reserved' element is contained -> it is added to combine call without any change
                    combine_params_array.append(parameter)
                # check if the 'content' element does exist or is not array
                elif ('content' not in parameter.keys()) or (type(parameter['content']) is not list):
                    raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
                else:
                    # check if the content does have only one element (TODO: should this even be allowed?)
                    if len(parameter['content']) == 1:
                        single_params_array.append(parameter)
                        taged_string = replace_the_tag_with_value(taged_string, tag, parameter['content'], param_idx)
                        param_idx-=1 # the number of parameters is decreased -> the idx has to be the same in next run (now it is -1, at the end of while, there is +1)
                    else:
                        combine_params_array.append(parameter)
        elif parameter['type'] == 'local_variable':
            """ LOCAL VARIABLE """
            # content key should exist in param info
            if 'content' not in parameter.keys():
                raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
            # content should be an array
            if type(parameter['content']) is not list:
                raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
            # check if the content does have only one element
            if len(parameter['content']) == 1:
                single_params_array.append(parameter)
                taged_string = replace_the_tag_with_value(taged_string, tag, parameter['content'], param_idx)
                param_idx-=1 # the number of parameters is decreased -> the idx has to be the same in next run (now it is -1, at the end of while, there is +1)
            else:
                combine_params_array.append(parameter)
        elif parameter['type'] == 'enumerate':
            """ ENUMERATE """
            # can be string or list (should have not have a list with one value, but it is supported here as well)
            # all values should be stored in 'content' element
            # check if 'content' element does exist
            if 'content' not in parameter.keys():
                raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
            # check if the type of content is array or string
            if type(parameter['content']) is str:
                single_params_array.append(parameter)
                taged_string = replace_the_tag_with_value(taged_string, tag, parameter['content'], param_idx)
                param_idx-=1 # the number of parameters is decreased -> the idx has to be the same in next run (now it is -1, at the end of while, there is +1)
            elif type(parameter['content']) is list:
                # check if the content does have only one element
                if len(parameter['content']) == 1:
                    single_params_array.append(parameter)
                    taged_string = replace_the_tag_with_value(taged_string, tag, parameter['content'], param_idx)
                    param_idx-=1 # the number of parameters is decreased -> the idx has to be the same in next run (now it is -1, at the end of while, there is +1)
                else:
                    combine_params_array.append(parameter)
            else:
                # other types are not supported 
                raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
        else:
            raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
        # TODO: removed to fix one problem -> not sure if another problem will not occur
        param_idx+=1

    # Check if size of single_params_array and size of combine_params_array = param_array's size
    # param_array is already 0, because all values were poped -> the param_array_size is evaluated in the beggining of function
    if len(single_params_array) + len(combine_params_array) != param_array_size:
        raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
    
    # Check if all tags in taged string were replaced - or at least the number of combine params match the numbeer of tags in string
    tag_count = taged_string.count(tag)
    if tag_count != len(combine_params_array):
        # the number of parameters which will be sent to combine does not correspond to the number of tags in string
        raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
    
    # print(taged_string)
    # print("---- JSEM NA KONCI ---")
    # exit(4)
    return taged_string,combine_params_array

def edit_the_parameter_array(endpoint_element, parameter_array, location):
    """
    Evaluate the string parser resulted parameter
    * check if a global variable already has a value
    * separate the enumerate string by separator
    * remove single values parameters
    * check if the number of local variables is the same as the nubmer of values in local_params
    * check if the global variable does have the value in global_params
    """
    """
    Iterate over all elements in returned param array
    * evaluate global_variable
    * evaluate local_variable
    * evaluate enumerate
    """ 
    inputed_global_params = globe.inputData.global_params
    separator = getattr(globe.config, location).enum.separator
    for parameter in parameter_array:
        if parameter['type'] == 'global_variable':
            """ GLOBAL VARAIBLE """
            # check if the global variable already has assigned value
            if parameter['name'] in globe.global_params_with_value.keys():
                # it alredy have some value -> get the value and insert it into parameter info
                parameter['value'] = globe.global_params_with_value[parameter['name']]
            elif parameter['name'] in globe.global_params_reserved:
                # check if this global variable was used in current combine call
                parameter['reserved'] = True
            else:
                # the global parameter does not have assigned value yet
                # check if it does exist in input data
                if parameter['name'] not in inputed_global_params:
                    message = "The global parameter '{}' does not exist in input data".format(parameter['name'])
                    raise EndpointSemanticError(__name__, "get_endpoint_info", message)
                # insert the content array of this global variable into param information
                parameter['content'] = inputed_global_params[parameter['name']]
                # add this global to a reserved global variables (if the variable with a smae name occures in the same combine call)
                globe.global_params_reserved.append(parameter['name'])
        elif parameter['type'] == 'local_variable':
            """ LOCAL VARAIBLE """
            # Pop and get the first value of local parameters 
            try:
                pop_result = endpoint_element['local_params'].pop(0)
            except IndexError:
                message = "There is not enough local parameters in {}".format(location)
                raise EndpointSemanticError(__name__, "get_endpoint_info", message)
            
            # insert these values into parameter information
            try:
                parameter['content'] = pop_result['values']
            except:
                message = "There is something wrong with a local_parameter '{}' (probably missing 'values')".format(parameter['name'])
                raise EndpointSemanticError(__name__, "get_endpoint_info", message)         
        elif parameter['type'] == 'enumerate':
            """ ENUMERATE VARAIBLE """
            # separate the content by a separator
            splited = parameter['content'].split(separator)

            # if there is only one element in splited array -> make it a string
            splited_length = len(splited)
            if splited_length == 1:
                splited = str(splited[0])
            elif splited_length == 0:
                raise ShouldHaveNotGottenHereError(__name__, "get_endpoint_info") 

            # insert the separated values into parameter information
            parameter['content'] = splited
        else:
            ShouldHaveNotGottenHereError(__name__, "get_endpoint_info")

    # TODO: TODO: TODO: TODO: TODO: this have to be moved somewhere else
    # if the parameters are in file, it would fail
    # # check if the local params array is empty
    # # otherwise it means there is some extra local param which will not be used
    # if len(endpoint_element['local_params']) != 0:
    #     message = "The amount of local parameters is bigger than needed"
    #     raise EndpointSemanticError(__name__, "get_endpoint_info", message) 
    # # return is not neccessary because it is modified due deep copy
    # return parameter_array

def method_string_parser(method_string):
    """
    Parse the given method string and retrieve a desired data out of it
    4 possibilities of method entry:
        * "GET"
        * "<GET,POST,DELETE>"
        * "<>" + local_variable
        * "<:var:>" + global_variable
    Result:
        TODO:
    """
    logging.debug('Calling the method_string_parser function with following parameter: {}'.format(method_string))

    # get the length of a method_string
    len_method_str = len(method_string)
    # starting and ending parameters
    enum_start_tag = globe.config.method.enum.start
    enum_end_tag = globe.config.method.enum.end
    variable_start_tag = globe.config.method.variable.start
    variable_end_tag = globe.config.method.variable.end
    # prio and non prio variables
    prio_start_tag = globe.config.method.priority_start
    non_prio_start_tag = globe.config.method.non_priority_start
    prio_end_tag = globe.config.method.priority_end
    non_prio_end_tag = globe.config.method.non_priority_end 
    # count the length of each tag
    len_prio_start = len(prio_start_tag)
    len_prio_end = len(prio_end_tag)
    len_nonprio_start = len(non_prio_start_tag)
    len_nonprio_end = len(non_prio_end_tag)
    # find indexes of each tag
    prio_idx_start = method_string.find(prio_start_tag)
    prio_idx_end = method_string.find(prio_end_tag) 
    noprio_idx_start = method_string.find(non_prio_start_tag)
    noprio_idx_end = method_string.find(non_prio_end_tag)

    """
    Validate if the given string meets the requirements
    Requirements:
        * method_string is actually a string
        * there should be only one parameter (does not matter if it's global or local)
        * if there is parameter, check if it is closed as well
        * the parameter's tags are in correct order
    Count the number of occurences of:
        * enum_start_tag
        * enum_end_tag
        * variable_start_tag
        * variable_end_tag
    Check if these number makes sense 
    -> there should be only one parameter and it has to contain of start and end tag
    -> these starting and ending tags should be in correct order
    """
    
    """
    Evaluation based on a location of priority and non-priority tags in method_string
    """
    if prio_idx_start == 0:
        # there is priority tag at the very beginning 
        # check if the priority tag is closed as well -> it should be in a very end
        # the length of ending tag have to be counted in
        if (prio_idx_end+len(prio_end_tag)) == len(method_string):
            # the priority tag is closed
            # get the content between priority tags
            content = method_string[len_prio_start:(len_method_str-len_prio_end)]
            # the content cannot contain any tag
            tags = [enum_start_tag,enum_end_tag,variable_start_tag,variable_end_tag]
            if any(x in content for x in tags):
                message = "The content of priority tags contain some other tag"
                raise EndpointSemanticError(__name__, "method_string_parser", message)
            # check if the priority tag is varaible or enumerate
            if prio_start_tag == enum_start_tag:
                # prio is enumerate
                """ Add the information about this parameter to a global variable 'globe.all_parameters' """
                p = {"location": "method", 'type': 'enumerate', 'content': content, 'id': globe.param_id_counter}
            else:
                # prio is variable
                """ Add the information about this parameter to a global variable 'globe.all_parameters' """
                p = {"location": "method", 'type': 'variable', 'name': content, 'id': globe.param_id_counter}
            globe.all_parameters.append(p)
            globe.param_id_counter += 1
        else:
            message = "The priority tag is not closed properly"
            raise EndpointSemanticError(__name__, "method_string_parser", message)
    elif noprio_idx_start == 0:
        # there is no priority tag, but non-priority tag is there
        # check if the non-priority tag is closed-> it should be in a very end
        # the length of ending tag have to be counted in
        if (noprio_idx_end+len(non_prio_end_tag)) == len(method_string):
            # the non-priority tag is closed
            # get the content between non-priority tags
            content = method_string[len_nonprio_start:(len_method_str-len_nonprio_end)]
            # the content cannot contain any tag
            tags = [enum_start_tag,enum_end_tag,variable_start_tag,variable_end_tag]
            if any(x in content for x in tags):
                message = "The content of non-priority tags contain some other tag"
                raise EndpointSemanticError(__name__, "method_string_parser", message)
            # check if the non-priority tag is varaible or enumerate
            if non_prio_start_tag == enum_start_tag:
                # non-prio is enumerate
                """ Add the information about this parameter to a global variable 'globe.all_parameters' """
                p = {"location": "method", 'type': 'enumerate', 'content': content, 'id': globe.param_id_counter}
            else:
                # prio is variable
                """ Add the information about this parameter to a global variable 'globe.all_parameters' """
                p = {"location": "method", 'type': 'variable', 'name': content, 'id': globe.param_id_counter}
            globe.all_parameters.append(p)
            globe.param_id_counter += 1
    else:
        # there is no starting tag of priority and non-priority -> it's a string with a single value
        # check if the method_string is in list of allowed HTTP methods
        if method_string in globe.list_of_allowed_http_methods:
            # it is a legit HTTP method
            """ Add the information about this parameter to a global variable 'globe.all_parameters' """
            p = {"location": "method", 'type': 'enumerate', 'content': method_string, 'id': globe.param_id_counter}
            globe.all_parameters.append(p)
            globe.param_id_counter += 1
        else:
            # it is some random string
            message = "The value of method string doesn't make sense"
            raise EndpointSemanticError(__name__, "method_string_parser", message)
    return p

def get_endpoint_info(endpoint_element):
    """
    Get the information about endpoint part in call
    Tuple (modified_url, endpoint_params) is returned
    Return:
        * Differenet output if the combine was called and if not
        COMBINE CALLED  -> (already filled url cases,True)
        NOT CALLED      -> ((taged_string, parameter_info),False)
    """
    logging.debug('Getting info about endpoint part')

    # get the tag of a taged_string - is in endpoint -> get the url non prio tag
    tag = globe.config.url.non_priority_start + globe.config.url.non_priority_end

    """ URL 
    TODO: Check if the url structure is valid - nested tags and so on
    Get the information about url
    """
    # (modified_string, params_array)
    parameters_tuple = general_string_parser(endpoint_element['values'], 'endpoint')

    #########################################################################################
    # this function was removed from this part and then modified to support endpoint,method, header and body
    edit_the_parameter_array(endpoint_element, parameters_tuple[1], 'url')
    #########################################################################################

    # remove the single values parameters -> also replace their value in modified string
    combine_params = remove_single_values_params(parameters_tuple[0], parameters_tuple[1], 'endpoint')


    """
    T-WAY
    """
    # check if the t-way element
    if 't-way' in endpoint_element.keys():
        local_combine_call = globe.CombineCallClass()
        local_combine_call.body['t_strength'] = str(endpoint_element['t-way'])

        for parameter in combine_params[1]:
            # add_parameter_to_combine_call(parameter, local_combine_call)
            add_indexes_of_parameter_to_combine_call(parameter, local_combine_call)
       
        """ Call the combine """
        combine_response = api_call_combine(local_combine_call)
        endpoint_test_cases = evaluate_combine_response(combine_response, combine_params, tag, 'endpoint', [])
        return endpoint_test_cases,True     
    return combine_params,False
        
    # """
    # Prepare the json body for a combine - add the parameters to the body
    # """
    # for parameter in combine_params[1]:
    #     add_parameter_to_combine_call(parameter, globe.combine_request)

    # """ 
    # check the optional keys
    # """
    # # check if the t-way element is on endpoint dictionary
    # if 't-way' in endpoint_element.keys():
    #     # t-way key je pouzit -> combine call will be requested
    #     globe.combine_request.body['t_strength'] = str(endpoint_element['t-way'])
    #     # TODO: check if the t_strength in combine call does make sense
    #     # TODO: t_strength = 1 -> how to call combine? Or should I implement it by myself?
    #     """
    #     Call the combine
    #     """
    #     combine_response = api_call_combine(globe.combine_request)
    #     endpoint_test_cases_tuple = evaluate_combine_response(combine_response, combine_params, tag, 'endpoint')
    #     # true indicated that the combine was called in this layer already
    #     return endpoint_test_cases_tuple,True 

    # # false indcates that the combine was not called and have to be called in upper layer
    # return combine_params,False

def get_method_info(method_element):
    """
    Get the information about endpoint part in call
    Method_param info is returned:
        * ex.: {"location": "method", 'type': 'enumerate', 'content': 'GET', 'id': 4}
        * ex.: {"location": "method", 'type': 'variable', 'content': '', 'name': 'var', 'id': 4}
    """
    logging.debug('Getting info about method part')

    # method_p = method_string_parser(method_element['values'])
    parameters_tuple = general_string_parser(method_element['values'], 'method')

    edit_the_parameter_array(method_element, parameters_tuple[1], 'method')

    """
    Evaluate if the method should be added to a combine call -> if there is a signle value, the method is just set to this value
    """
    # remove the single values parameters -> also replace their value in modified string
    combine_params = remove_single_values_params(parameters_tuple[0], parameters_tuple[1], 'method')
    return combine_params,False

def header_string_parser(header_string):
    """
    Parse the given header string and retrieve a desired data out of it
    4 possibilities of header entry:
        "values": "header1.yaml"
        "values": "<header1.yaml,header2.yaml,header3.yaml>"
        "values": "<>"
        "values": "<:header_variable:>"
    """
    logging.debug('Calling the header_string_parser function with following parameter: {}'.format(header_string))

    # get the length of a header_string
    len_header_str = len(header_string)
    # starting and ending parameters
    enum_start_tag = globe.config.header.enum.start
    enum_end_tag = globe.config.header.enum.end
    variable_start_tag = globe.config.header.variable.start
    variable_end_tag = globe.config.header.variable.end
    # prio and non prio variables
    prio_start_tag = globe.config.header.priority_start
    non_prio_start_tag = globe.config.header.non_priority_start
    prio_end_tag = globe.config.header.priority_end
    non_prio_end_tag = globe.config.header.non_priority_end 
    # count the length of each tag
    len_prio_start = len(prio_start_tag)
    len_prio_end = len(prio_end_tag)
    len_nonprio_start = len(non_prio_start_tag)
    len_nonprio_end = len(non_prio_end_tag)
    # find indexes of each tag
    prio_idx_start = header_string.find(prio_start_tag)
    prio_idx_end = header_string.find(prio_end_tag) 
    noprio_idx_start = header_string.find(non_prio_start_tag)
    noprio_idx_end = header_string.find(non_prio_end_tag)

    """
    Evaluation based on a location of priority and non-priority tags in header_string
    """
    if prio_idx_start == 0:
        # there is priority tag at the very beginning 
        # check if the priority tag is closed as well -> it should be in a very end
        # the length of ending tag have to be counted in
        if (prio_idx_end+len(prio_end_tag)) == len(header_string):
            # the priority tag is closed
            # get the content between priority tags
            content = header_string[len_prio_start:(len_header_str-len_prio_end)]
            # the content cannot contain any tag
            tags = [enum_start_tag,enum_end_tag,variable_start_tag,variable_end_tag]
            if any(x in content for x in tags):
                message = "The content of priority tags contain some other tag"
                raise EndpointSemanticError(__name__, "header_string_parser", message)
            # check if the priority tag is varaible or enumerate
            if prio_start_tag == enum_start_tag:
                # prio is enumerate
                """ Add the information about this parameter to a global variable 'globe.all_parameters' """
                p = {"location": "header", 'type': 'enumerate', 'content': content, 'id': globe.param_id_counter}
            else:
                # prio is variable
                """ Add the information about this parameter to a global variable 'globe.all_parameters' """
                p = {"location": "header", 'type': 'variable', 'name': content, 'id': globe.param_id_counter}
            globe.all_parameters.append(p)
            globe.param_id_counter += 1
        else:
            message = "The priority tag is not closed properly"
            raise EndpointSemanticError(__name__, "header_string_parser", message)
    elif noprio_idx_start == 0:
        # there is no priority tag, but non-priority tag is there
        # check if the non-priority tag is closed-> it should be in a very end
        # the length of ending tag have to be counted in
        if (noprio_idx_end+len(non_prio_end_tag)) == len(header_string):
            # the non-priority tag is closed
            # get the content between non-priority tags
            content = header_string[len_nonprio_start:(len_header_str-len_nonprio_end)]
            # the content cannot contain any tag
            tags = [enum_start_tag,enum_end_tag,variable_start_tag,variable_end_tag]
            if any(x in content for x in tags):
                message = "The content of non-priority tags contain some other tag"
                raise EndpointSemanticError(__name__, "header_string_parser", message)
            # check if the non-priority tag is varaible or enumerate
            if non_prio_start_tag == enum_start_tag:
                # non-prio is enumerate
                """ Add the information about this parameter to a global variable 'globe.all_parameters' """
                p = {"location": "header", 'type': 'enumerate', 'content': content, 'id': globe.param_id_counter}
            else:
                # prio is variable
                """ Add the information about this parameter to a global variable 'globe.all_parameters' """
                p = {"location": "header", 'type': 'variable', 'name': content, 'id': globe.param_id_counter}
            globe.all_parameters.append(p)
            globe.param_id_counter += 1
    else:
        # there is no starting tag of priority and non-priority -> it's a string with a single value
        """ Add the information about this parameter to a global variable 'globe.all_parameters' """
        content = header_string
        p = {"location": "header", 'type': 'enumerate', 'content': content, 'id': globe.param_id_counter}
        globe.all_parameters.append(p)
        globe.param_id_counter += 1
    return content

def get_header_info(header_element):
    """
    Get the information about header part in call
    Header_param info is returned:
        * ex.: {"location": "header", 'type': 'enumerate', 'content': 'header1.yaml', 'id': 3}
        * ex.: {"location": "header", 'type': 'variable', 'content': '', 'name': 'var', 'id': 3}
    Example inputs:
    * String
        "values": "header1.yaml"
        "values": "<header1.yaml,header2.yaml,header3.yaml>"
        "values": "<>"
        "values": "<:header_variable:>"  
    * Dictionary
        "values": {'Content-type': 'json', 'test': 'test_value'}
        "values": {'Content-type': 'json', 'test': 'test_value'}
        "values": {'Content-type': '<'1','2','3','4'>', 'test': '<1,2,3,4,5,6>'}
        "values": {'<>': '<>', 'test': 'test_value'}  
    * If there is only one header file, the parameteres can be in file content as well
        Content-Type: <123456>
		Host: <:var:>
    """
    logging.debug('Getting info about header part')

    """ Co je potreba udelat
    1. Podivat se, co mi to vlastne bylo predano
    check if the given element is string or dictionary
    STRING
    * do the same magic as in method? -> call header_string_parser
    * check if there is only one header file or there are some more
    # if there is only one -> check if there are some parametres in file content
    # if not -> ignore previous step and do the same logic as in method
    DICTIONARY
    * transfer dictioanry to the string ({} are not allowed to be as a tag - only in this case - otherwise it is allowed)
    * find all parameters - same logic was alredy done before in url
    FILE
    * open a file, get the content of file as a string
    * similiar logic to DICTIONARY
    * muze byt file modifikovan? nebo jen ulozit? pravdepdoobne vytvorit kopii - stejne se bude vytvaret kupa souboru pro test suite
    """
    values_type = type(header_element['values'])
    # check what type of value is given
    if values_type is str:
        # value is string -> the content is a file
        # header = header_string_parser(header_element['values'])
        header_tuple = general_string_parser(header_element['values'], 'header')

        # edit the output
        edit_the_parameter_array(header_element, header_tuple[1], 'header')
        # remove the single value parameters
        # if there are no more parameters left, it means there is only one file -> we should repead the process of 
        # seraching parameters, but this time in file content
        header_params = remove_single_values_params(header_tuple[0], header_tuple[1], 'header')
        if len(header_params[1]) == 0:
            # all parameteres have been already filled -> there is only one file
            # look it in file content
            file_content = get_file_content(header_params[0])
            header_file_tuple = general_string_parser(file_content, 'header')
            edit_the_parameter_array(header_element, header_file_tuple[1], 'header')
            header_params = remove_single_values_params(header_file_tuple[0], header_file_tuple[1], 'header')
    elif values_type is dict:
        # value is dictionary -> change the type to from dictionary to string
        header_value_string = json.dumps(header_element['values'])
        header_tuple = general_string_parser(header_value_string, 'header')
        # edit the output
        edit_the_parameter_array(header_element, header_tuple[1], 'header')
        header_params = remove_single_values_params(header_tuple[0], header_tuple[1], 'header')
    else:
        print("proper error should be raised")
        exit(2)

    # check if the local params array is empty
    # otherwise it means there is some extra local param which will not be used
    if len(header_element['local_params']) != 0:
        message = "The amount of local parameters is bigger than needed"
        raise EndpointSemanticError(__name__, "get_endpoint_info", message) 

    tag = globe.config.header.non_priority_start + globe.config.header.non_priority_end

    """
    T-WAY
    """
    # check if the t-way element is on endpoint dictionary
    if 't-way' in header_element.keys():
        local_combine_call = globe.CombineCallClass()
        local_combine_call.body['t_strength'] = str(header_element['t-way'])

        for parameter in header_params[1]:
            add_parameter_to_combine_call(parameter, local_combine_call)
       
        """ Call the combine """
        combine_response = api_call_combine(local_combine_call)
        endpoint_test_cases = evaluate_combine_response(combine_response, header_params, tag, 'header', [])
        return endpoint_test_cases,True 
    return header_params,False

def get_body_info(body_element):
    """
    Get the information about body part in call
    Example inputs:
    * STRING - file_path / body_content_string (toggle in input json: value_is_body_string)
        "values": "body.json"
        "values": "TotoJeTelo"
        "values": "<>"
        "values": "<body1.json,body2.json,body3.json>"
        "values": "<:body_var:>"
    * FILE    
    * if only single file is passed -> it can contain a parameters
    * open a file, get the content of file as a string
    * similiar logic to header FILE
    """
    logging.debug('Getting info about body part')

    print(body_element)

    values_type = type(body_element['values'])
    # check what type of value is given
    if values_type is str:
        # value is string -> the content is a file
        body_tuple = general_string_parser(body_element['values'], 'body')

        # edit the output
        edit_the_parameter_array(body_element, body_tuple[1], 'body')
        # remove the single value parameters
        # if there are no more parameters left, it means there is only one file -> we should repead the process of 
        # seraching parameters, but this time in file content
        body_params = remove_single_values_params(body_tuple[0], body_tuple[1], 'body')
        if len(body_params[1]) == 0:
            # all parameteres have been already filled -> there is only one file
            # look it in file content
            file_content = get_file_content(body_params[0])
            body_file_tuple = general_string_parser(file_content, 'body')
            edit_the_parameter_array(body_element, body_file_tuple[1], 'body')
            body_params = remove_single_values_params(body_file_tuple[0], body_file_tuple[1], 'body')
    elif values_type is dict:
        # value is dictionary -> change the type to from dictionary to string
        body_value_string = json.dumps(body_element['values'])
        body_tuple = general_string_parser(body_value_string, 'body')
        # edit the output
        edit_the_parameter_array(body_element, body_tuple[1], 'body')
        body_params = remove_single_values_params(body_tuple[0], body_tuple[1], 'body')
    else:
        print("proper error should be raised")
        exit(2)

    # check if the local params array is empty
    # otherwise it means there is some extra local param which will not be used
    if len(body_element['local_params']) != 0:
        message = "The amount of local parameters is bigger than needed"
        raise EndpointSemanticError(__name__, "get_endpoint_info", message) 

    tag = globe.config.body.non_priority_start + globe.config.body.non_priority_end
    
    """
    T-WAY
    """
    # check if the t-way element
    if 't-way' in body_element.keys():
        local_combine_call = globe.CombineCallClass()
        local_combine_call.body['t_strength'] = str(body_element['t-way'])

        for parameter in body_params[1]:
            add_parameter_to_combine_call(parameter, local_combine_call)
       
        """ Call the combine """
        combine_response = api_call_combine(local_combine_call)
        endpoint_test_cases = evaluate_combine_response(combine_response, body_params, tag, 'body', [])
        return endpoint_test_cases,True 
    return body_params,False

    # modified_body_string = general_string_parser(body_element['values'], 'body')
    # return modified_body_string
