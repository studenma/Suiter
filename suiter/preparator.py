import logging
logger = logging.getLogger(__name__)

from exceptions import EndpointSemanticError
import suiter_classes_and_globals as globe

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

def url_string_parser(url):
    """ 
    Parse the given url 
    * search for all parameters in url
    * evaluate what type of parameter it is:
        ** enumerate type
        ** global variable type
        ** local variable type
    * add these parameteres to a 'globe.all_parameters'
    * all params are replaced with a starting and ending symbol of non priority tag
    Return a tuple:
        * modified url 
            ** before: https://mydomain/addUser/<:user:>/<>/<1,2,3,4,5>/<:used:>
            ** after:  https://mydomain/addUser/<>/<>/<>/<>
        * url_parameters_array:
        [
            {'location': 'endpoint', 'type': 'variable', 'content': '', 'name': 'user', 'id': 0}
            {'location': 'endpoint', 'type': 'enumerate', 'content': '', 'id': 1}
            {'location': 'endpoint', 'type': 'enumerate', 'content': '1,2,3,4,5', 'id': 2}
            {'location': 'endpoint', 'type': 'variable', 'content': '', 'name': 'used', 'id': 3}
        ]
    """
    logging.debug('Calling the url_parser function with a following parameter: {}'.format(url))

    # starting and ending variables
    enum_start_tag = globe.config.url.enum.start
    enum_end_tag = globe.config.url.enum.end
    variable_start_tag = globe.config.url.variable.start
    variable_end_tag = globe.config.url.variable.end
    # prio and non prio variables
    prio_start_tag = globe.config.url.priority_start
    non_prio_start_tag = globe.config.url.non_priority_start
    prio_end_tag = globe.config.url.priority_end
    non_prio_end_tag = globe.config.url.non_priority_end 

    """
    Search for all parameters in url
    variables:
        * e_idx     = index of location, where the enumerate start tag was found
        * v_idx     = index of location, where the variable start tag was found
        * position  = indicates the location of pointer in url (to avoid searching tags which were already been found)
        * globe.param_id_counter = current parameter id (global varaible - is reseted to 0 after every combine call)
        * globe.all_parameters   = list of all parameters collected (reseted after every combine call) 
    used functions:
        * find_between() = to get the content in between starting and ending tag
            ** returns: 
    """
    position = 0
    # the first searchs of url enumerate and varaible starting tags
    e_idx = url.find(globe.config.url.enum.start)
    v_idx = url.find(globe.config.url.variable.start)
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
                Modify url for current parameter
                Get the content of current parameter
                Count the position for next search
                """
                # get (modified_url, content, position)
                url_tuple = find_between(url[position:], enum_start_tag, enum_end_tag, non_prio_start_tag, non_prio_end_tag)
                temp = url
                url = url[:position] + url_tuple[0]
                content = url_tuple[1]
                position = len(temp[:position]) + url_tuple[2]

                """
                Add the information about this parameter to a global variable 'globe.all_parameters'
                """
                p = {"location": "endpoint", "type": "enumerate", "content": content, "id": globe.param_id_counter}
                globe.all_parameters.append(p)

                """
                Evaluate which tag was already evaluated
                If e_idx or v_idx was evaluated, the next occurence have to be searched
                In this case the indexes are the same -> have to search new idx for both
                """
                e_change = e_idx
                v_change = v_idx
            elif prio_start_tag is variable_start_tag:
                """
                Modify url for current parameter
                Get the content of current parameter (variable)
                Count the position for next search
                """
                # get (modified_url, content, position)
                url_tuple = find_between(url[position:], variable_start_tag, variable_end_tag, non_prio_start_tag, non_prio_end_tag)
                temp = url
                url = url[:position] + url_tuple[0]
                variable = url_tuple[1]
                position = len(temp[:position]) + url_tuple[2]

                """
                Add the information about this parameter to a global variable 'globe.all_parameters'
                """
                p = {"location": "endpoint", "type": "variable", "content": '', "name": variable, "id": globe.param_id_counter}
                globe.all_parameters.append(p)

                """
                Evaluate which tag was already evaluated
                If e_idx or v_idx was evaluated, the next occurence have to be searched
                In this case the indexes are the same -> have to search new idx for both
                """
                v_change = v_idx
                e_change = e_idx
            else:
                message = "Should have never gotten here"
                raise EndpointSemanticError(__name__, "url_parser", message)
        else:
            if e_idx < v_idx:
                """
                Unless the e_idx == -1
                -> e_idx should be evaluated before v_idx
                -> v_idx will stay the same, new e_idx will be search then
                """
                if e_idx == -1:
                    """
                    Modify url for current parameter
                    Get the content of current parameter (variable)
                    Count the position for next search
                    """
                    # get (modified_url, content, position)
                    url_tuple = find_between(url[position:], variable_start_tag, variable_end_tag, non_prio_start_tag, non_prio_end_tag)
                    temp = url
                    url = url[:position] + url_tuple[0]
                    variable = url_tuple[1]
                    position = len(temp[:position]) + url_tuple[2]

                    """
                    Add the information about this parameter to a global variable 'globe.all_parameters'
                    """
                    p = {"location": "endpoint", "type": "variable", "content": '', "name": variable, "id": globe.param_id_counter}
                    globe.all_parameters.append(p)

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
                    Modify url for current parameter
                    Get the content of current parameter (content)
                    Count the position for next search
                    """
                    # get (modified_url, content, position)
                    url_tuple = find_between(url[position:], enum_start_tag, enum_end_tag, non_prio_start_tag, non_prio_end_tag)
                    temp = url
                    url = url[:position] + url_tuple[0]
                    content = url_tuple[1]
                    position = len(temp[:position]) + url_tuple[2]
                   
                    """
                    Add the information about this parameter to a global variable 'globe.all_parameters'
                    """
                    p = {"location": "endpoint", "type": "enumerate", "content": content, "id": globe.param_id_counter}
                    globe.all_parameters.append(p)
                    
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
                    Modify url for current parameter
                    Get the content of current parameter (content)
                    Count the position for next search
                    """
                    # get (modified_url, content, position)
                    url_tuple = find_between(url[position:], enum_start_tag, enum_end_tag, non_prio_start_tag, non_prio_end_tag)
                    temp = url
                    url = url[:position] + url_tuple[0]
                    content = url_tuple[1]
                    position = len(temp[:position]) + url_tuple[2]

                    """
                    Add the information about this parameter to a global variable 'globe.all_parameters'
                    """
                    p = {"location": "endpoint", "type": "enumerate", "content": content, "id": globe.param_id_counter}
                    globe.all_parameters.append(p)

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
                    Modify url for current parameter
                    Get the content of current parameter (content)
                    Count the position for next search
                    """
                    # get (modified_url, content, position)
                    url_tuple = find_between(url[position:], variable_start_tag, variable_end_tag, non_prio_start_tag, non_prio_end_tag)
                    temp = url
                    url = url[:position] + url_tuple[0]
                    variable = url_tuple[1]
                    position = len(temp[:position]) + url_tuple[2]

                    """
                    Add the information about this parameter to a global variable 'globe.all_parameters'
                    """
                    p = {"location": "endpoint", "type": "variable", "content": '', "name": variable, "id": globe.param_id_counter}
                    globe.all_parameters.append(p)

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
                raise EndpointSemanticError(__name__, "url_parser", message)

        """
        WHILE EVALUATION
        Find the first occurence of ENUM start tag or VARIABLE start tag
        in the next iteration of while, the already evaluated part of url is ignored
        (e_change+1 and v_change+1 means it starts to search from this index)
        if nothing is found -> -1 is returned
        """
        e_idx = url.find(enum_start_tag, e_change+1)
        v_idx = url.find(variable_start_tag, v_change+1)
        globe.param_id_counter += 1
    
    return url,globe.all_parameters

def get_endpoint_info(endpoint_element):
    """
    Get the information about endpoint part in call
    Tuple (modified_url, endpoint_params) is returned
    """
    logging.debug('Getting info about endpoint part')

    """ URL 
    TODO: Check if the url structure is valid - nested tags and so on
    Get the information about url
    """
    url_param_tuple = url_string_parser(endpoint_element['values'])
    return url_param_tuple


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

def get_method_info(method_element):
    """
    Get the information about endpoint part in call
    Method_param info is returned:
        * ex.: {"location": "method", 'type': 'enumerate', 'content': 'GET', 'id': 4}
        * ex.: {"location": "method", 'type': 'variable', 'content': '', 'name': 'var', 'id': 4}
    """
    logging.debug('Getting info about method part')

    method_p = method_string_parser(method_element['values'])
    return method_p
    # # get the array size of a method values
    # arr_size = len(method_element['values'])
    # # there is only one element in value array
    # if arr_size == 1:
    #     # if this element is not in list allowed HTTP method -> it has to be a varaible type
    #     # TODO: split the varaible name out of it and do soemthing with that
    #     if method_element['values'][0] in globe.list_of_allowed_http_methods:
    #         """ Add the information about this parameter to a global variable 'globe.all_parameters' """
    #         result = {"location": "method", 'type': 'enumerate', 'content': method_element['values'][0], 'id': globe.param_id_counter}
    #     else:
    #         """ The method contains a variable """
    #         # split the value string and get the variable name
    #         _,variable_name,_ = find_between(method_element['values'][0], globe.config.method.variable.start, globe.config.method.variable.end, '', '')
    #         """ Add the information about this parameter to a global variable 'globe.all_parameters' """
    #         result = {"location": "method", 'type': 'variable', 'content': '', 'name': variable_name, 'id': globe.param_id_counter}       
    #     globe.param_id_counter += 1
    # elif arr_size > 1:
    #     """ Add the information about this parameter to a global variable 'globe.all_parameters' """
    #     result = {"location": "method", 'type': 'enumerate', 'content': method_element['values'], 'id': globe.param_id_counter}
    #     globe.param_id_counter += 1
    # else:
    #     message = "Should have never gotten here"
    #     raise EndpointSemanticError(__name__, "get_method_info", message) 
    
    # globe.all_parameters.append(result)
    # return result

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
        p = {"location": "header", 'type': 'enumerate', 'content': header_string, 'id': globe.param_id_counter}
        globe.all_parameters.append(p)
        globe.param_id_counter += 1
    return p

def header_dictionary_parser(header_dict):
    print(header_dict)

    exit(5)

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
        # value is string
        p = header_string_parser(header_element['values'])
    elif values_type is dict:
        # value is dictionary
        p = header_dictionary_parser(header_element['values'])
    else:
        # error should be raised
        exit(2)

    exit(1)

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
    None
