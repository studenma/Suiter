import json
import logging
logger = logging.getLogger(__name__)
logger.propagate = False

from exceptions import *
import suiter_classes_and_globals as globe
from combine_request import api_call_combine, evaluate_combine_response, add_parameter_to_combine_call, add_indexes_of_parameter_to_combine_call
from general import replace_the_tag_with_value, get_file_content, verify_tway_value

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
    * add these parameteres to a 'globe.all_parameters' (indikuje, jake globalni promenne bybly pouzity v cele aplikace)
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
    # logging.debug('Calling the general_string_parser function with a following parameters: [{}, {}]'.format(content_string, location))

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
            elif prio_start_tag == variable_start_tag:
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

                # add the information about this parameter to a reulted array
                p = {"location": location, "type": "global_variable", "name": variable, "id": globe.param_id_counter}
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
        start_tag = str(globe.config.url.non_priority_start)
        end_tag = str(globe.config.url.non_priority_end)
    elif location == 'method':
        tag = str(globe.config.method.non_priority_start) + str(globe.config.method.non_priority_end)
        start_tag = str(globe.config.method.non_priority_start)
        end_tag = str(globe.config.method.non_priority_end)
    elif location == 'header':
        tag = str(globe.config.header.non_priority_start) + str(globe.config.header.non_priority_end)
        start_tag = str(globe.config.header.non_priority_start)
        end_tag = str(globe.config.header.non_priority_end)
    elif location == 'body':
        tag = str(globe.config.body.non_priority_start) + str(globe.config.body.non_priority_end)
        start_tag = str(globe.config.body.non_priority_start)
        end_tag = str(globe.config.body.non_priority_end)
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
                replacement = parameter['value']
                taged_string = replace_the_tag_with_value(taged_string, tag, replacement, param_idx)
                param_idx-=1
                # TODO: replace the value in string
            else:
                # check if the 'reserved' element does exist (the global variable has already been added)
                if ('reserved' in parameter.keys()) and (parameter['reserved'] == True):
                    # if the 'reserved' element is contained -> it is replaced in a string with a <:varaible_name:> 
                    replacement = start_tag + parameter['name'] + end_tag
                    taged_string = replace_the_tag_with_value(taged_string, tag, replacement, param_idx)
                    single_params_array.append(parameter)
                    param_idx-=1 # the number of parameters is decreased -> the idx has to be the same in next run (now it is -1, at the end of while, there is +1)
                # check if the 'content' element does exist or is not array
                elif ('content' not in parameter.keys()) or (type(parameter['content']) is not list):
                    raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
                else:
                    # check if the content does have only one element (TODO: should this even be allowed?)
                    if len(parameter['content']) == 1:
                        # GLOBLANI PROMENNA BYLA STANOVENA NA ZAKLADE TOHO, ZE TAM JE JEN JEDEN PARAMETER -> MUSI SE PRIDAT DO LOKALNICH PROMENNYCH
                        globe.global_params_with_value[parameter['name']] = parameter['content'][0]
                        # globe.global_params_reserved.append(parameter['name'])
                        single_params_array.append(parameter)
                        taged_string = replace_the_tag_with_value(taged_string, tag, parameter['content'][0], param_idx)
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
            if parameter['name'] in globe.global_params_reserved:
                # check if this global variable was used in current combine call
                parameter['reserved'] = True
            else:
                # the global parameter does not have assigned value yet
                # check if it does exist in input data
                if parameter['name'] not in inputed_global_params:
                    message = "The global parameter '{}' does not exist in input data".format(parameter['name'])
                    raise EndpointSemanticError(__name__, "edit_the_parameter_array", message)
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
                raise EndpointSemanticError(__name__, "edit_the_parameter_array", message)
            
            # insert these values into parameter information
            try:
                parameter['content'] = pop_result['values']
            except:
                message = "There is something wrong with a local_parameter '{}' (probably missing 'values')".format(parameter['name'])
                raise EndpointSemanticError(__name__, "edit_the_parameter_array", message)         
        elif parameter['type'] == 'enumerate':
            """ ENUMERATE VARAIBLE """
            # separate the content by a separator
            splited = parameter['content'].split(separator)

            # if there is only one element in splited array -> make it a string
            splited_length = len(splited)
            if splited_length == 1:
                splited = str(splited[0])
            elif splited_length == 0:
                raise ShouldHaveNotGottenHereError(__name__, "edit_the_parameter_array") 

            # insert the separated values into parameter information
            parameter['content'] = splited
        else:
            ShouldHaveNotGottenHereError(__name__, "edit_the_parameter_array")


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

def single_remove_global_from_string(taged_string, global_values, location):
    """
    Input: 
    ('https://mydomain/addUser/4/GET/ABC/1/usr1/asd/fgh/<user>/A', {'user': 4, 'method': 'GET'})
    Output:
    ('https://mydomain/addUser/4/GET/ABC/1/usr1/asd/fgh/4/A', {'user': 4, 'method': 'GET'})
    """
    start_tag = getattr(globe.config, location).non_priority_start
    end_tag = getattr(globe.config, location).non_priority_end
    for key in global_values.keys():
        tag = start_tag + key + end_tag
        while tag in taged_string:
            replacement = str(global_values[key])
            taged_string = replace_the_tag_with_value(taged_string, tag, replacement, 0)
    return taged_string


def postprocessing_of_globals(tagedString_globals_array, location):
    new_array = []
    for element in tagedString_globals_array:
        new_taged = single_remove_global_from_string(element[0], element[1], location)
        tuple_replacement = (new_taged,element[1])
        new_array.append(tuple_replacement)
    return new_array

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

    tag = globe.config.url.non_priority_start + globe.config.url.non_priority_end
    start_tag = globe.config.url.non_priority_start
    end_tag = globe.config.url.non_priority_end

    """ URL 
    TODO: Check if the url structure is valid - nested tags and so on
    Get the information about url
    """

    print("***********************")
    print("get_endpoint_info")
    print("***********************")
    
    parameters_tuple = general_string_parser(endpoint_element['values'], 'endpoint')
    print("------- GENERAL STRING PARSER -----------")
    print(parameters_tuple[0])
    for element in parameters_tuple[1]:
        print(element)

    #########################################################################################
    # this function was removed from this part and then modified to support endpoint,method, header and body
    edit_the_parameter_array(endpoint_element, parameters_tuple[1], 'url')
    #########################################################################################
    print("------- EDIT THE PARAMETER ARRAY -----------")
    print(parameters_tuple[0])
    for element in parameters_tuple[1]:
        print(element)

    # chek if the endpoint_element['local_params'] is empty (indicates that all the local parameters was used)
    # has to be here, because if the parameters are serached in file, it fails 
    if len(endpoint_element['local_params']) != 0:
        print(endpoint_element['local_params'])
        message = "The number of local parameteres is higher then needed"
        raise InputFileError(__name__, "edit_the_parameter_array", message)
        exit(1)


    # remove the single values parameters -> also replace their value in modified string
    combine_params = remove_single_values_params(parameters_tuple[0], parameters_tuple[1], 'endpoint')
    print("-------- REMOVE SINGLE VALUES PARAMS ----------")
    print(combine_params[0])
    for element in combine_params[1]:
        print(element)    

    """
    T-WAY
    """
    # check if the t-way element
    if 't-way' in endpoint_element.keys():
        tway_value = endpoint_element['t-way']

        # check if the t-way value does make sense in comparison with number of parameters
        number_of_parameteres = len(combine_params[1])
        from general import verify_tway_value
        verify_tway_value(tway_value, number_of_parameteres)

        print("jsem az tady")
        exit(1)

        local_combine_call = globe.CombineCallClass()
        local_combine_call.body['t_strength'] = str(tway_value)

        

        for parameter in combine_params[1]:
            add_parameter_to_combine_call(parameter, local_combine_call)
       
        print("----------COMBNINE INPUT-----------")
        for element in local_combine_call.body['parameters']:
            print(element)

        """ Call the combine """
        combine_response = api_call_combine(local_combine_call)

        print("----------COMBINE RESPONSE-----------")
        for element in combine_response:
            print(element)

        endpoint_test_cases = evaluate_combine_response(combine_response, combine_params, tag, 'endpoint', [])

        print("----------EVALUATED COMBINE RESPONSE-----------")
        for element in endpoint_test_cases:
            print(element)
        

        new_array = postprocessing_of_globals(endpoint_test_cases, 'url')
        
        print("----------POSTPROCESSING AFTER COMBINE-----------")
        for element in new_array:
            print(element)

        return new_array,"indexes"   
    else:
        print("-------NOT TWAY RESULT-----------")
        print(combine_params[0])
        for element in combine_params[1]:
            print(element)

        if len(combine_params[1]) == 0:
            return combine_params,"done_string"
        else:
            return combine_params,"parameters"
        
def get_method_info(method_element):
    """
    Get the information about endpoint part in call
    Method_param info is returned:
        * ex.: {"location": "method", 'type': 'enumerate', 'content': 'GET', 'id': 4}
        * ex.: {"location": "method", 'type': 'variable', 'content': '', 'name': 'var', 'id': 4}
    """
    logging.debug('Getting info about method part')

    print("***********************")
    print("get_method_info")
    print("***********************")

    # method_p = method_string_parser(method_element['values'])
    parameters_tuple = general_string_parser(method_element['values'], 'method')
    print("------- GENERAL STRING PARSER -----------")
    print(parameters_tuple[0])
    for element in parameters_tuple[1]:
        print(element)

    edit_the_parameter_array(method_element, parameters_tuple[1], 'method')
    print("------- EDIT THE PARAMETER ARRAY -----------")
    print(parameters_tuple[0])
    for element in parameters_tuple[1]:
        print(element)


    """
    Evaluate if the method should be added to a combine call -> if there is a signle value, the method is just set to this value
    """
    # remove the single values parameters -> also replace their value in modified string
    combine_params = remove_single_values_params(parameters_tuple[0], parameters_tuple[1], 'method')

    print("-------- REMOVE SINGLE VALUES PARAMS (RETURNED) ----------")
    print(combine_params[0])
    for element in combine_params[1]:
        print(element)  

    if len(combine_params[1]) == 0:
        return combine_params,'done_string'
    else:
        return combine_params,'parameters'

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
    print("***********************")
    print("get_header_info")
    print("***********************")

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
        print("------- GENERAL STRING PARSER (STR) -----------")
        print(header_tuple[0])
        for element in header_tuple[1]:
            print(element)

        # edit the output
        edit_the_parameter_array(header_element, header_tuple[1], 'header')
        print("------- EDIT THE PARAMETER ARRAY (STR) -----------")
        print(header_tuple[0])
        for element in header_tuple[1]:
            print(element)
        # remove the single value parameters
        # if there are no more parameters left, it means there is only one file -> we should repead the process of 
        # seraching parameters, but this time in file content
        header_params = remove_single_values_params(header_tuple[0], header_tuple[1], 'header')
        print("-------- REMOVE SINGLE VALUES PARAMS (STR) ----------")
        print(header_params[0])
        for element in header_params[1]:
            print(element)  
            
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
        print("------- GENERAL STRING PARSER (DICT) -----------")
        print(header_tuple[0])
        for element in header_tuple[1]:
            print(element)

        # edit the output
        edit_the_parameter_array(header_element, header_tuple[1], 'header')
        print("------- EDIT THE PARAMETER ARRAY (DICT) -----------")
        print(header_tuple[0])
        for element in header_tuple[1]:
            print(element)

        header_params = remove_single_values_params(header_tuple[0], header_tuple[1], 'header')
        print("-------- REMOVE SINGLE VALUES PARAMS (DICT) ----------")
        print(header_params[0])
        for element in header_params[1]:
            print(element)  
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
        return endpoint_test_cases,'indexes' 

    if len(header_params[1]) == 0:
        return header_params,'done_string'
    return header_params,'parameters'

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

    print("***********************")
    print("get_body_info")
    print("***********************")

    values_type = type(body_element['values'])
    # check what type of value is given
    if values_type is str:
        # value is string -> the content is a file
        body_tuple = general_string_parser(body_element['values'], 'body')
        print("------- GENERAL STRING PARSER (STR) -----------")
        print(body_tuple[0])
        for element in body_tuple[1]:
            print(element)

        # edit the output
        edit_the_parameter_array(body_element, body_tuple[1], 'body')
        print("------- EDIT THE PARAMETER ARRAY (STR) -----------")
        print(body_tuple[0])
        for element in body_tuple[1]:
            print(element)

        # remove the single value parameters
        # if there are no more parameters left, it means there is only one file -> we should repead the process of 
        # seraching parameters, but this time in file content
        body_params = remove_single_values_params(body_tuple[0], body_tuple[1], 'body')
        print("-------- REMOVE SINGLE VALUES PARAMS (STR) ----------")
        print(body_params[0])
        for element in body_params[1]:
            print(element)  

        if len(body_params[1]) == 0:
            # all parameteres have been already filled -> there is only one file
            # look it in file content
            file_content = get_file_content(body_params[0])
            body_file_tuple = general_string_parser(file_content, 'body')
            print("------- GENERAL STRING PARSER (FILE CONTENT) -----------")
            print(body_file_tuple[0])
            for element in body_file_tuple[1]:
                print(element)

            edit_the_parameter_array(body_element, body_file_tuple[1], 'body')
            print("------- EDIT THE PARAMETER ARRAY (FILE CONTENT) -----------")
            print(body_file_tuple[0])
            for element in body_file_tuple[1]:
                print(element)

            body_params = remove_single_values_params(body_file_tuple[0], body_file_tuple[1], 'body')
            print("-------- REMOVE SINGLE VALUES PARAMS (FILE CONTENT) ----------")
            print(body_params[0])
            for element in body_params[1]:
                print(element)  

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

    start_tag = globe.config.body.non_priority_start
    end_tag = globe.config.body.non_priority_end
    tag = start_tag + end_tag
    
    """
    T-WAY
    """
    # check if the t-way element
    if 't-way' in body_element.keys():
        local_combine_call = globe.CombineCallClass()
        local_combine_call.body['t_strength'] = str(body_element['t-way'])

        for parameter in body_params[1]:
            add_parameter_to_combine_call(parameter, local_combine_call)

        print("----------COMBNINE INPUT-----------")
        for element in local_combine_call.body['parameters']:
            print(element)

        """ Call the combine """
        combine_response = api_call_combine(local_combine_call)
        print("----------COMBINE RESPONSE-----------")
        for element in combine_response:
            print(element)
        
        body_test_cases = evaluate_combine_response(combine_response, body_params, tag, 'body', [])
        print("----------EVALUATED COMBINE RESPONSE-----------")
        for element in body_test_cases:
            print(element)

        new_array = postprocessing_of_globals(body_test_cases, 'body')
        print("----------POSTPROCESSING AFTER COMBINE-----------")
        for element in new_array:
            print(element)            
        return new_array,'indexes' 
    else:
        print("-------NOT TWAY RESULT-----------")
        print(body_params[0])
        for element in body_params[1]:
            print(element)

        if len(body_params[1]) == 0:
            return body_params,'done_string' 
        return body_params,'parameters'


def add_endpoint_to_combine_request(combine_call, endpoint, endpoint_toggle, info_about_combine_blocks):
    """ 
    Add the parameters of endpoint to the combine request 
    (if the combine was not called in endpoint element and it has some parameters)
    """
    if endpoint_toggle == 'indexes':
        list_of_indexes = []
        for idx in range(len(endpoint)):
            list_of_indexes.append(str(idx))
        add_array_to_a_combine_call(list_of_indexes, combine_call, "URL")
        info_about_combine_blocks.append({'location': 'endpoint', 'type': 'indexes'})
    elif endpoint_toggle == 'parameters':
        for parameter in endpoint[1]:
            add_parameter_to_combine_call(parameter, combine_call)
            info_about_combine_blocks.append({'location': 'endpoint', 'type': 'parameters'})
    elif endpoint_toggle == 'done_string':
        None # nothing needs to be done
    else:
        raise ShouldHaveNotGottenHereError(__name__, "add_endpoint_to_combine_request")

def add_method_to_combine_request(combine_call, method, method_toggle, info_about_combine_blocks):
    """ 
    Add the parameter of method to the combine request 
    Only one parameter is allowed to be in method part -> the combine cannot be called
    """
    if method_toggle == 'parameters':
        # in method can be only one parameter
        if len(method[1]) != 1:
            raise ShouldHaveNotGottenHereError(__name__, "add_method_to_combine_request")
        for parameter in method[1]:
            add_parameter_to_combine_call(parameter, combine_call)
            info_about_combine_blocks.append({'location': 'method', 'type': 'parameters'})
    elif method_toggle == 'done_string':
        None # nothing needs to be done
    else:
        raise ShouldHaveNotGottenHereError(__name__, "add_method_to_combine_request")

def add_header_to_combine_request(combine_call, header, header_toggle, info_about_combine_blocks):
    """ 
    Add the parameters of header to the combine request
    (if the combine was not called in header element and it has some parameters)
    """
    if header_toggle == 'indexes':
        array_values = []
        for element in header:
            array_values.append(element[0])
        add_array_to_a_combine_call(array_values, combine_call, "HEADER")
        info_about_combine_blocks.append({'location': 'header', 'type': 'indexes'})
    elif header_toggle == 'parameters':
        for element in header[1]:
            add_parameter_to_combine_call(element, combine_call)
            info_about_combine_blocks.append({'location': 'header', 'type': 'parameters'})
    elif header_toggle == 'done_string':
        None # nothing needs to be done
    else:
        raise ShouldHaveNotGottenHereError(__name__, "add_method_to_combine_request")

def add_body_to_combine_request(combine_call, body, body_toggle, info_about_combine_blocks):
    """ 
    Add the parameters of body to the combine request
    (if the combine was not called in body element and it has some parameters)
    """
    if body_toggle == 'indexes':
        list_of_indexes = []
        for idx in range(len(body)):
            list_of_indexes.append(str(idx))
        add_array_to_a_combine_call(list_of_indexes, combine_call, "BODY")
        info_about_combine_blocks.append({'location': 'body', 'type': 'indexes'})
    elif body_toggle == 'parameters':
        for element in body[1]:
            add_parameter_to_combine_call(element, combine_call)
            info_about_combine_blocks.append({'location': 'body', 'type': 'parameters'})
    elif body_toggle == 'done_string':
        None # nothing needs to be done
    else:
        raise ShouldHaveNotGottenHereError(__name__, "add_method_to_combine_request")

def evaluate_combine_response_main(combine_response, info_about_combine_blocks, test_cases_arrays):   
    endpoint_test_cases = test_cases_arrays[0]
    method_test_cases = test_cases_arrays[1]
    header_test_cases = test_cases_arrays[2]
    body_test_cases = test_cases_arrays[3]

    endpoint_param_array = []
    method_param_array = []
    header_param_array = []
    body_param_array = []     
    # Projdi jednotlive pripady z combine response
    case_cnt = 0
    for case in combine_response:
        # TODO: co udelat for idx in len combine response + call=combine_response.pop()
        test_case_parts = []
        headies = []
        bodies = []
        endies = []
        methies = []
        # projdi vsechny jeho hodnoty
        for value_idx in range(len(case)):
            # get the infromation about this value
            info_about_current_block = info_about_combine_blocks[value_idx]
            if info_about_current_block['location'] == 'endpoint':
                """ ENDPOINT """
                if info_about_current_block['type'] == 'indexes':
                    """ indexes """
                    value_of_case = endpoint[int(case[value_idx])]
                    endpoint_test_cases.append(value_of_case)
                elif info_about_current_block['type'] == 'parameters':
                    """ parameters """
                    value_of_case = case[value_idx]
                    endies.append(value_of_case)
                else:
                    print("Chyba")
                    exit(1)
            elif info_about_current_block['location'] == 'method':
                """ METHOD """
                if info_about_current_block['type'] == 'parameters':
                    """ parameters """
                    value_of_case = case[value_idx]
                    methies.append(value_of_case)
                else:
                    exit(1)
            elif info_about_current_block['location'] == 'header':
                """ HEADER """
                if info_about_current_block['type'] == 'indexes':
                    """ indexes """
                    value_of_case = header[int(case[value_idx])]
                    header_test_cases.append(value_of_case)
                elif info_about_current_block['type'] == 'parameters':
                    """ parameters """
                    value_of_case = case[value_idx]
                    headies.append(value_of_case)
                else:
                    exit(1)
            elif info_about_current_block['location'] == 'body':
                """ BODY """
                if info_about_current_block['type'] == 'indexes':
                    """ indexes """
                    value_of_case = body[int(case[value_idx])]
                    body_test_cases.append(value_of_case)
                elif info_about_current_block['type'] == 'parameters':
                    """ parameters """
                    value_of_case = case[value_idx]
                    bodies.append(value_of_case)
                else:
                    exit(1)
            else:
                exit(1)
        endpoint_param_array.append(endies)
        method_param_array.append(methies)
        header_param_array.append(headies)
        body_param_array.append(bodies)
        case_cnt+=1
    return (endpoint_param_array,method_param_array,header_param_array,body_param_array)

def create_input_file_for_templator():
    """
    Create a input file for templator module
    """
    call_idx = -1
    super_duper_result = []
    for call in globe.inputData.test_sequence:
        call_idx+=1
        logging.debug('Getting info about call')

        ###############DEBUG#################
        print("""
        **************************************
        Call number {} in sequence
        **************************************
        """.format(call_idx))
        #####################################

        """ 
        Get the information about each part of a request
        * The output varies depending on a fact whatever the combine call was called inside or not
        ** if combine was called    -> toggle == 'indexes'
                                    -> result = list of tuples: (all URLs with combined parameters, it's global variables)
        ** if combine was not called, but there are some parameteres to be combined
                                    -> toggle = 'parameters'
                                    -> result = array -> [0] modified string with marked parameters (to remeber where to insert them later on)
                                                         [1] list of information about parameters
        ** if combine was not called, there are no parameters to be combined
                                    -> toggle = 'done_string'
                                    -> result = value (usually string)           
        """
        endpoint,endpoint_toggle = get_endpoint_info(call['endpoint'])
        method,method_toggle = get_method_info(call['method'])
        header,header_toggle = get_header_info(call['header'])
        body,body_toggle = get_body_info(call['body'])

        """
        Create a combine request
        * Add values to combine request body
            * 'indexes'
            ** the indexes to the array have to be combined instead of actual value (to avoid problems with global variables)
            * 'parameters'
            ** standard combine request with parameters inserted with it's real values
            * 'done_string'
            ** nothing needs to be done (there is only one value which is used in all cases)
            * The info_about_combine_blocks array is defined 
            ** to remember which block of combine request is passed as a index to array
            ** the location is remembered to know where the parameter should be replaced after their combination
            ** {'location': 'endpoint', 'type': 'indexes'}
            ** {'location': 'header', 'type': 'parameters'}
        """
        info_about_combine_blocks = []
        # create combine call with default specification
        combine_call = globe.CombineCallClass()
        # change the value of t-way based on a specification
        combine_call.body['t_strength'] = call['t-way']
        # add blocks of parameters to a combine call
        add_endpoint_to_combine_request(combine_call, endpoint, endpoint_toggle, info_about_combine_blocks)
        add_method_to_combine_request(combine_call, method, method_toggle, info_about_combine_blocks)
        add_header_to_combine_request(combine_call, header, header_toggle, info_about_combine_blocks)
        add_body_to_combine_request(combine_call, body, body_toggle, info_about_combine_blocks)

        # check if the t-way value does make sense in comparison with number of parameters
        verify_tway_value(combine_call.body['t_strength'], len(combine_call.body['parameters']))
        
        ###############DEBUG#################
        print("------ MAIN COMBINE CALLS ----")
        for element in combine_call.body['parameters']:
            print(element)
        print("------ INFO ABOUT BLOCKS -----")
        for element in info_about_combine_blocks:
             print(element)
        ##################################### 
        
        """ 
        Call combine 
        """
        combine_response = api_call_combine(combine_call)

        ###############DEBUG#################
        print("----------COMBINE MAIN RESPONSE-----------")
        for element in combine_response:
            print(element)
        print("----------INFO ABOUT COMBINE BLOCKS-----------")
        for element in info_about_combine_blocks:
            print(element)
        ##################################### 

        """
        check if the number of values in combine response is equal to the number of it's descriptions (info_about_combine_blocks)
        """
        if len(info_about_combine_blocks) != len(combine_response[0]):
            raise ShouldHaveNotGottenHereError(__name__, "add_method_to_combine_request")


        """
        Evaluate the combine response
        Look into endpoint taged url 
            -> are there any tags? Or is it fulfiled? Should I have some toggle to indicate that?
            -> fill the tags with values -> what with a global variables behaviour -> should be similiar 
                algorithm to the one before -> but it has to support global variables across the all parts
        Look into method taged string 
            -> should it be skiped? Or should the value be taken
        Look into header taged string
        Look into body taged string
        """
        endpoint_test_cases = []
        method_test_cases = []
        header_test_cases = []
        body_test_cases = []
        test_cases_arrays = [endpoint_test_cases,method_test_cases,header_test_cases,body_test_cases]
        
        endpoint_param_array,method_param_array,header_param_array,body_param_array = evaluate_combine_response_main(combine_response, info_about_combine_blocks, test_cases_arrays)

        """ ENDPOINT """
        if endpoint_toggle == 'indexes':
            # nothing needs to be done
            endpoint_test_cases = endpoint_test_cases
        elif endpoint_toggle == 'parameters':
            endpoint_test_cases = evaluate_combine_response(endpoint_param_array, endpoint, '<>', 'endpoint', [])
        elif endpoint_toggle == 'done_string':
            # duplicate this string to have it in the same format (value, globals)
            temp_tuple = (endpoint[0], {})
            for _ in range(len(combine_response)):
                endpoint_test_cases.append(temp_tuple)
        else:
            exit(6)

        """ METHOD """
        if method_toggle == 'parameters':
            method_test_cases = evaluate_combine_response(method_param_array, method, '<>', 'method', [])
        elif method_toggle == 'done_string':
            # duplicate this string to have it in the same format (value, globals)
            temp_tuple = (method[0], {})
            for _ in range(len(combine_response)):
                method_test_cases.append(temp_tuple)
        else:
            exit(4)

        """ HEADER """
        if header_toggle == 'indexes':
            # nothing needs to be done
            header_test_cases = header_test_cases
        elif header_toggle == 'parameters':
            header_test_cases = evaluate_combine_response(header_param_array, header, '<>', 'header', [])
        elif header_toggle == 'done_string':
            # duplicate this string to have it in the same format (value, globals)
            temp_tuple = (header[0], {})
            for _ in range(len(combine_response)):
                header_test_cases.append(temp_tuple)
        else:
            exit(6)

        """ BODY """
        if body_toggle == 'indexes':
            # nothing needs to be done
            body_test_cases = body_test_cases
        elif body_toggle == 'parameters':
            body_test_cases = evaluate_combine_response(body_param_array, body, '<>', 'body', [])
        elif body_toggle == 'done_string':
            # duplicate this string to have it in the same format (value, globals)
            temp_tuple = (body[0], {})
            for _ in range(len(combine_response)):
                body_test_cases.append(temp_tuple)
        else:
            exit(6)

        print("----------ENDPOINT TEST CASES-----------")
        for element in endpoint_test_cases:
            print(element)
        print("----------METHOD TEST CASES-----------")
        for element in method_test_cases:
            print(element)
        print("----------HEADER TEST CASES-----------")
        for element in header_test_cases:
            print(element)
        print("----------BODY TEST CASES-----------")
        for element in body_test_cases:
            print(element)


        """
        result = [
            ([URL, method, header, body], {GLOBALS}),
            ([URL, method, header, body], {GLOBALS})
            ....
        ]
        """
        result = []


        combine_response_length = len(combine_response)
        endpoint_test_cases_length = len(endpoint_test_cases)
        method_test_cases_length = len(method_test_cases)
        header_test_cases_length = len(header_test_cases)
        body_test_cases_length = len(body_test_cases)
        print("----------ENDPOINT TEST CASES LENGTH-----------")
        print(combine_response_length)
        print(endpoint_test_cases_length)
        print(method_test_cases_length)
        print(header_test_cases_length)
        print(body_test_cases_length)
        if not (combine_response_length == endpoint_test_cases_length == method_test_cases_length == header_test_cases_length == body_test_cases_length):
            print("Ty sracky se sobe nerovnaji")
            exit(5)




        for test_case_idx in range(len(combine_response)):
            endpoint,endpoint_globals = endpoint_test_cases[test_case_idx]
            method,method_globals = method_test_cases[test_case_idx]
            header,header_globals = header_test_cases[test_case_idx]
            body,body_globals = body_test_cases[test_case_idx]

            all_globals = {}
            all_globals.update(endpoint_globals)
            all_globals.update(method_globals)
            all_globals.update(header_globals)
            all_globals.update(body_globals)

            """
            Nahrad globalni promenne
            """
            for key in all_globals.keys():
                # endpoint
                start_tag = globe.config.url.non_priority_start
                end_tag = globe.config.url.non_priority_end
                tag = start_tag + key + end_tag
                while tag in endpoint:
                    endpoint = replace_the_tag_with_value(endpoint, tag, str(all_globals[key]), 0)
                    print("ENDPOINT REPLACEMENT")

                # method
                start_tag = globe.config.method.non_priority_start
                end_tag = globe.config.method.non_priority_end
                tag = start_tag + key + end_tag
                while tag in method:
                    method = replace_the_tag_with_value(method, tag, str(all_globals[key]), 0)
                    print("METHOD REPLACEMENT")

                # header
                start_tag = globe.config.header.non_priority_start
                end_tag = globe.config.header.non_priority_end
                tag = start_tag + key + end_tag
                while tag in header:
                    header = replace_the_tag_with_value(header, tag, str(all_globals[key]), 0)
                    print("HEADER REPLACEMENT")

                # body
                start_tag = globe.config.body.non_priority_start
                end_tag = globe.config.body.non_priority_end
                tag = start_tag + key + end_tag
                while tag in body:
                    body = replace_the_tag_with_value(body, tag, str(all_globals[key]), 0)
                    print("BODY REPLACEMENT")
            test_case = [endpoint, method, header, body]
            resulted_tuple = (test_case, all_globals)
            result.append(resulted_tuple)

        

        print("----------RESULT-----------")
        for element in result:
            print(element)

        super_duper_result.append(result)
        for idx in range(len(super_duper_result)):
            print("----------SUPER DUPER RESULT {}-----------".format(idx))
            for element in super_duper_result[idx]:
                print(element)

    return super_duper_result
