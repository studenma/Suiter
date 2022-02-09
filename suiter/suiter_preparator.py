"""
This module provides the funcionality to create the input file for a templator module. 
It reads the input json file, retrieve all the data out of it and combine its parameters 
with respect to the user's specifications
"""

import json
import logging
logger = logging.getLogger(__name__)

from suiter_exceptions import *
import suiter_classes_and_globals as globe
from suiter_combine_request import api_call_combine, evaluate_combine_response, add_parameter_to_combine_call, add_array_to_a_combine_call
from suiter_general import replace_the_tag_with_value, get_file_content, verify_tway_value, yes_or_no, get_header_from_file

def create_a_resulted_file_pretty(final_result_array, file_path):
    """ 
    Create a file for templator and open it for reading 
    """
    try:
        f = open(file_path, 'w')
    except:
        message = "Could not open a templator input file"
        raise OpenFileError(__name__, "create_a_resulted_file_pretty", message)

    """ 
    Pretify the string for templator to the readable format
    Write it to the file simultaneously
    """
    tab = '\t'
    # FIRST LAYER
    f.write('[' + '\n')
    current_tc_idx = 0
    index_of_last_tc = len(final_result_array) - 1
    for test_case in final_result_array:
        # SECOND LAYER
        f.write(tab+'[' + '\n')
        index_of_last_call = len(test_case) - 1
        current_call_idx = 0
        for call in test_case:
            # THIRD LAYER
            if current_call_idx == index_of_last_call:
                # no comma at the end
                f.write(2*tab + str(call) + '\n')
            else:
                # comma at the end
                f.write(2*tab + str(call) + ',\n')
            # END THIRD LAYER
            current_call_idx += 1
        # SECOND LAYER END
        if current_tc_idx == index_of_last_tc:
            # no comma at the end
            f.write(tab+']' + '\n')
        else:
            # comma at the end
            f.write(tab+']' + ',\n')
        current_tc_idx+=1
    # FIRST LAYER END
    f.write(']' + '\n')
    f.close()

def create_a_body_files(final_combinations):
    """
    Create a body file for each combination in request
    """
    final_combinations_with_files = []
    request_idx = 1
    for request in final_combinations:
        """ Go through all the request in test sequence """
        """ BODY """
        create_body_toggle = request[1]
        if create_body_toggle == True:
            """ The request's body has to be moved to a file """
            idx = 1
            for combination in request[0]:
                """ Iterate through all the request combiantions """
                # every combination consist of the value and it's variables (values are at index 0) 
                # every value consists of: [URL, method, header, body] -> body is index 3
                file_content = str(combination[0][3])
                with open("./result/body_files/request_{}_body_{}".format(request_idx, idx), "w") as f:
                        f.write(file_content)
                # replace the content of body in combiantion with it's file path
                combination[0][3] = "./body_files/request_{}_body_{}".format(request_idx, idx)
                idx+=1
        elif create_body_toggle == False:
            # nothing needs to be done
            None
        elif create_body_toggle == 'no_params':
            """ 
            There are no parameters in body
            Create just a single file 
            """
            file_content = request[0][0][0][3]
            with open("./result/body_files/request_{}_body_1".format(request_idx), "w") as f:
                f.write(file_content)
            for combination in request[0]:
                combination[0][3] = "./body_files/request_{}_body_1".format(request_idx)
        else:
            raise ShouldHaveNotGottenHereError(__name__, "add_method_to_combine_request")
        final_combinations_with_files.append(request[0])
        """ HEADER """
        request_idx+=1
    return final_combinations_with_files

def prepare_final_combine_request(combined_requests, file_content):
    """
    From a given calls cases, make a last combine request to combine them 
    """
    number_of_requests_in_sequence = len(combined_requests)

    # Check if the number of resulted calls is the same as the number of calls in input json
    if len(globe.inputData.test_sequence) != number_of_requests_in_sequence:
        raise ShouldHaveNotGottenHereError(__name__, "prepare_final_combine_request")

    """
    Create a combine request for final call combination
    If the 't-way' key is specified, set the value of it, otherwise all combinations are made (the t-way value is the same as the number of combine parameter)
    """
    final_combine_call = globe.CombineCallClass()
    if 't-way' in file_content:
        tway_value = file_content['t-way']
    else:
        raise ShouldHaveNotGottenHereError(__name__, "prepare_final_combine_request")
    final_combine_call.body['t_strength'] = tway_value

    """
    Add values to combine request body
    * the values are given to combine just as an 'index' to an existing array, where are these parametere values stored
    ** the indexes to the array have to be combined instead of actual value (to avoid problems with global variables)
    """
    for call_idx in range(number_of_requests_in_sequence):
        block_name = "FINAL_REQUEST_{}".format(call_idx)
        list_of_indexes = []
        for idx in range(len(combined_requests[call_idx])):
            list_of_indexes.append(str(idx))
        else:
            add_array_to_a_combine_call(list_of_indexes, final_combine_call, block_name)

    """
    Call a combine
    """
    combine_response = api_call_combine(final_combine_call)

    """
    Evaluate the final combine response
    Replace all global variables with its actual value
    """
    final_result = []
    for case in combine_response:
        """ Go through all the cases in combine response """
        cases_array = []
        all_globals = {}
        for value_idx in range(len(case)):
            """
            Go through every value in case. 
            * Replace the call indexes with their value and append the test case to a new array 'cases_array'
            * Get all the test case variables.
            """
            value_of_case = combined_requests[value_idx][int(case[value_idx])][0]
            case_globals = combined_requests[value_idx][int(case[value_idx])][1]
            all_globals.update(case_globals)
            cases_array.append(value_of_case)


        """ 
        Replace all the globals in the resulted test cases stored in a 'cases_array'
        """
        test_cases = []
        for element in cases_array:
            element_array = []
            for part in element:
                part = single_remove_global_from_string(part, all_globals, 'body')
                element_array.append(part)
            test_cases.append(element_array)
    
        final_result.append(test_cases)
    return final_result

def find_between(string, start_tag, end_tag, replace_with_start, replace_with_end):
    """ 
    Get the content between start_tag and end_tag
    Replace this content and its tags with a non- priority tags (doesn't really matter which one is used, but it has to be unified in whole application)    
    EXAMPLE: https://<:variable:>/the/rest/of/a/url
    Returns a tuple:
    * string cut of:
        * after: <>/the/rest/of/a/url
    * content between the tags
        * 'variable'
    * position in url
        * 10
    """
    try:
        # get the index-range of content between start_tag and end_tag
        get_from = string.index(start_tag) + len(start_tag)
        get_to = string.index(end_tag, get_from)
        # get the content between them
        content = string[get_from:get_to]
        # remove this content from string together with it's tags -> replace it with non-priority tags
        modified_string = string[:(get_from-len(start_tag))] + replace_with_start + replace_with_end + string[(get_to+len(end_tag)):]
        """
        Get the position of already evaluated part of string (this function is going to be called more than a once for the same string)
        So, next iteration has to start from this position, otherwise it will find the same tag
        """
        position = get_from-len(start_tag) + len(replace_with_start) + len(replace_with_end)
    except ValueError:
        message = "Some of the tag was probably not ended"
        raise EndpointSemanticError(__name__, "find_between", message)
    return (modified_string, content, position)

def general_string_parser(content_string, location, param_id_cnt, config):
    """ 
    Parse the given string of endpoint/method/header/body content 
    * search for all parameters in this string
    **  all params are replaced with a starting and ending symbol of non priority tag
    * evaluate what type of parameter it is:
        ** enumerate type
        ** global variable type
        ** local variable type
    * add these parameteres to a 'globe.all_parameters' (to indicate which global variable names were used within this application run)
    Return a tuple:
        * modified string -> every parameter is replaced with a non priority start and end tag 
            ** before: https://mydomain/addUser/<:user:>/<>/<1,2,3,4,5>/<:used:>
            ** after:  https://mydomain/addUser/<>/<>/<>/<>
            # before:  {'Content-type': '<123,456>', '<>': '<:var:>'}
            # after:   {'Content-type': '<>', '<>': '<>'}
        * list of parameters found:
        [
            {'location': $location, 'type': 'global_variable', 'name': 'user', 'id': 0}
            {'location': $location, 'type': 'global_variable', 'name': 'used', 'id': 1}
            {'location': $location, 'type': 'local_variable', 'id': 2}
            {'location': $location, 'type': 'enumerate', 'content': 'ABC', 'id': 3}
            {'location': $location, 'type': 'enumerate', 'content': '1,2,3,4,5', 'id': 4}
        ]
    """
    logging.debug('Calling the general_string_parser function with a following parameters: [{}, {}]'.format(content_string, location))

    """
    Get the format of tags
    * 2 types of tags in each part
    ** enumerate and local_variable (default <>)
    ** global_variable (default <::>)
    * By default, the enumerate tag is substring of global variable tag
    ** the priority tag is the one which should be searched in string first
    ** by default, priority tag is global_variable
    """

    # enumerate tags
    enum_start_tag = getattr(config, location).enum.start
    enum_end_tag = getattr(config, location).enum.end
    # global varaible tags
    variable_start_tag = getattr(config, location).variable.start
    variable_end_tag = getattr(config, location).variable.end
    # priority tags
    prio_start_tag = getattr(config, location).priority_start
    prio_end_tag = getattr(config, location).priority_end
    # non priority tags
    non_prio_start = getattr(config, location).non_priority_start
    non_prio_end = getattr(config, location).non_priority_end

    globe_param_id_counter = param_id_cnt


    # # enumerate tags
    # enum_start_tag = getattr(globe.config, location).enum.start
    # enum_end_tag = getattr(globe.config, location).enum.end
    # # global varaible tags
    # variable_start_tag = getattr(globe.config, location).variable.start
    # variable_end_tag = getattr(globe.config, location).variable.end
    # # priority tags
    # prio_start_tag = getattr(globe.config, location).priority_start
    # prio_end_tag = getattr(globe.config, location).priority_end
    # # non priority tags
    # non_prio_start = getattr(globe.config, location).non_priority_start
    # non_prio_end = getattr(globe.config, location).non_priority_end

    # list of all parameters in given string
    parameters = []
    """
    Search for all parameters in endpoint/method/header/body
    variables:
        * e_idx     = index of location, where the enumerate start tag was found
        * v_idx     = index of location, where the global variable start tag was found
        * position  = indicates the location of pointer in string (to avoid searching tags which were already been found)
        * globe.param_id_counter = current parameter id (each parameter has a different ID - in context of whole app run)
    used functions:
        * find_between() = to get the content between the starting and ending tag
    """
    position = 0 # possitional index in the string
    # the first search of enumerate and variable starting tags in string
    e_idx = content_string.find(enum_start_tag)
    v_idx = content_string.find(variable_start_tag)
    while e_idx != -1 or v_idx != -1: # end this loop when no more starting tags were found
        """
        If the ENUM and VARIABLE indexes were found in the same index
        -> it means one of them is substring of another one
        The one which is not a substring has always the priority
        * default example: https://<:variable:>
            -> both '<' and '<:' starts at the same position
            -> the '<:' is more important
        """
        if e_idx == v_idx:
            if prio_start_tag == enum_start_tag:
                """
                ENUM tag is the priority one
                * Get the content of current parameter
                * Modify a tagged string
                * Count the position for next search
                * find_between(string, start_tag, end_tag, start_replacement, end_replacement) returns tuple:
                    * string cut
                        * before: https://<:variable:>/the/rest/of/a/url
                        * after: <>/the/rest/of/a/url
                    * content between the tags
                        * 'variable'
                    * position in url
                        * 10
                """                
                resulted_tuple = find_between(content_string[position:], enum_start_tag, enum_end_tag, non_prio_start, non_prio_end)
                original_string = content_string
                content_string = content_string[:position] + resulted_tuple[0]
                content = resulted_tuple[1]
                position = len(original_string[:position]) + resulted_tuple[2]

                """
                Add the information about this parameter to a resulted array of parameters
                """
                # check if the content is empty string
                if len(content) == 0:
                    # -> it is a local variable
                    p = {"location": location, "type": "local_variable", "id": globe_param_id_counter}
                else:
                    # -> it is a enumerated type
                    p = {"location": location, "type": "enumerate", "content": content, "id": globe_param_id_counter}
                parameters.append(p)
                
                """
                Evaluate which tag was already evaluated
                If e_idx or v_idx was evaluated, the next occurence of it has to be searched
                In this case the indexes are the same -> have to search new indexes for both
                """
                e_change = e_idx
                v_change = v_idx
            elif prio_start_tag == variable_start_tag:
                """
                VARIABLE tag is the priority one
                * Get the content of current parameter
                * Modify a tagged string
                * Count the position for next search
                """
                resulted_tuple = find_between(content_string[position:], variable_start_tag, variable_end_tag, non_prio_start, non_prio_end)
                original_string = content_string
                content_string = content_string[:position] + resulted_tuple[0]
                variable = resulted_tuple[1]
                position = len(original_string[:position]) + resulted_tuple[2]

                """
                Add the information about this parameter to a resulted array of parameters
                """
                p = {"location": location, "type": "global_variable", "name": variable, "id": globe_param_id_counter}
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
                ENUM is found before VARIABLE
                * unless the e_idx is not -1 (no more tag was found)
                -> e_idx should be evaluated before v_idx
                -> v_idx will stay the same, only the new e_idx will be search at the end
                """
                if e_idx == -1:
                    """
                    No more ENUM tags were found in string
                    * Get the content of current parameter
                    * Modify a tagged string
                    * Count the position for next search
                    """
                    resulted_tuple = find_between(content_string[position:], variable_start_tag, variable_end_tag, non_prio_start, non_prio_end)
                    original_string = content_string
                    content_string = content_string[:position] + resulted_tuple[0]
                    variable = resulted_tuple[1]
                    position = len(original_string[:position]) + resulted_tuple[2]
                    
                    """
                    Add the information about this parameter to a resulted array of parameters
                    """
                    p = {"location": location, "type": "global_variable", "name": variable, "id": globe_param_id_counter}
                    parameters.append(p)

                    """
                    Evaluate which tag was already evaluated
                    If e_idx or v_idx was evaluated, the next occurence have to be searched
                    In this case only the new v_idx should be searched 
                    (e_idx will be search as well, but from a v_idx starting point) -> algorithm will find the same one as before
                    """
                    v_change = v_idx
                    e_change = v_idx
                else:
                    """
                    ENUM is found before VARIABLE
                    * Get the content of current parameter
                    * Modify a tagged string
                    * Count the position for next search
                    """
                    resulted_tuple = find_between(content_string[position:], enum_start_tag, enum_end_tag, non_prio_start, non_prio_end)
                    original_string = content_string
                    content_string = content_string[:position] + resulted_tuple[0]
                    content = resulted_tuple[1]
                    position = len(original_string[:position]) + resulted_tuple[2]

                    """
                    Add the information about this parameter to a resulted array of parameters
                    """
                    # check if the content is empty string
                    if len(content) == 0:
                        # -> it is a local variable
                        p = {"location": location, "type": "local_variable", "id": globe_param_id_counter}
                    else:
                        # -> it is a enumerated type
                        p = {"location": location, "type": "enumerate", "content": content, "id": globe_param_id_counter}
                    parameters.append(p)
                    
                    """
                    Evaluate which tag was already evaluated
                    If e_idx or v_idx was evaluated, the next occurence have to be searched
                    In this case only the new e_idx should be searched 
                    (v_idx will be search as well, but from a e_idx starting point) -> algorithm will find the same one as before
                    """
                    e_change = e_idx
                    v_change = e_idx
            elif v_idx < e_idx:
                """
                VARIABLE is found before ENUM
                * unless the v_idx is not -1 (no more tag was found)
                -> v_idx should be evaluated before e_idx
                -> e_idx will stay the same, only the new v_idx will be search at the end
                """
                if v_idx == -1:
                    """
                    No more VARIABLE tags were found in string
                    * Get the content of current parameter
                    * Modify a tagged string
                    * Count the position for next search
                    """
                    resulted_tuple = find_between(content_string[position:], enum_start_tag, enum_end_tag, non_prio_start, non_prio_end)
                    original_string = content_string
                    content_string = content_string[:position] + resulted_tuple[0]
                    content = resulted_tuple[1]
                    position = len(original_string[:position]) + resulted_tuple[2]

                    """
                    Add the information about this parameter to a resulted array of parameters
                    """
                    # check if the content is empty string 
                    if len(content) == 0:
                        # -> it is a local variable
                        p = {"location": location, "type": "local_variable", "id": globe_param_id_counter}
                    else:
                        # -> it is an enumerated type
                        p = {"location": location, "type": "enumerate", "content": content, "id": globe_param_id_counter}
                    parameters.append(p)

                    """
                    Evaluate which tag was already evaluated
                    If e_idx or v_idx was evaluated, the next occurence have to be searched
                    In this case only the new e_idx should be searched 
                    (v_idx will be search as well, but from a e_idx starting point) -> algorithm will find the same one as before
                    """
                    e_change = e_idx
                    v_change = e_idx
                else:
                    """
                    VARIABLE is found before ENUM
                    * Get the content of current parameter
                    * Modify a tagged string
                    * Count the position for next search
                    """
                    resulted_tuple = find_between(content_string[position:], variable_start_tag, variable_end_tag, non_prio_start, non_prio_end)
                    original_string = content_string
                    content_string = content_string[:position] + resulted_tuple[0]
                    variable = resulted_tuple[1]
                    position = len(original_string[:position]) + resulted_tuple[2]

                    """
                    Add the information about this parameter to a resulted array of parameters
                    """
                    p = {"location": location, "type": "global_variable", "name": variable, "id": globe_param_id_counter}
                    parameters.append(p)

                    """
                    Evaluate which tag was already evaluated
                    If e_idx or v_idx was evaluated, the next occurence have to be searched
                    In this case only the new v_idx should be searched 
                    (e_idx will be search as well, but from a v_idx starting point) -> algorithm will find the same one as before
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
        globe_param_id_counter += 1
    return content_string,parameters

def remove_single_values_params(taged_string, param_array, location):
    """
    Remove the single values parameters
    Also, replace their value in tagged string
    """
    # this array is discarded and never used at the end of this function (is used just to check that the single+multiple == all)
    single_params_array = [] 
    # this array is returned togetger with tagged string 
    combine_params_array = []  
    # get the number of all parameters (to validate that the single+multiple == all)
    all_params_array = len(param_array)
    """
    This function should be called only with a param_array with the same locations
    """
    for par in param_array:
        if par['location'] != location:
            raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")

    """
    Decide which tag should be replaced - endpoint, method, body and header may have different non-priority tags
    Tagged string is tagged with a non-priority tag
    """
    start_tag = getattr(globe.config, location).non_priority_start
    end_tag = getattr(globe.config, location).non_priority_end
    tag = start_tag + end_tag

    """
    Pop all values from param_array one by one
    """
    param_idx = 0 # this counter indicates the nth occurence of tag which should be replaced
    while len(param_array) != 0:
        parameter = param_array.pop(0)
        """
        Decide what type of parameter is this one
        """
        if parameter['type'] == 'global_variable':
            """ GLOBAL VARIABLE """
            if 'value' in parameter.keys(): 
                # if there is 'value' in keys -> it is a global variable with a already existing value
                # so, it should be removed and replaced
                single_params_array.append(parameter)
                replacement = parameter['value']
                taged_string = replace_the_tag_with_value(taged_string, tag, replacement, param_idx)
                param_idx-=1
            else:
                if ('reserved' in parameter.keys()) and (parameter['reserved'] == True):
                    # this global variable name has already been used
                    # it is replaced in a string of global variable name covered in nonpriority tags (example: <varaible_name>) 
                    replacement = start_tag + parameter['name'] + end_tag
                    taged_string = replace_the_tag_with_value(taged_string, tag, replacement, param_idx)
                    single_params_array.append(parameter)
                    # the number of tags in string decreased -> the parameters has to be decreased as well (the param_idx has to be the same in next run -> now it gets -1, at the end of while it gets +1)
                    param_idx-=1 
                elif ('content' not in parameter.keys()) or (type(parameter['content']) is not list):
                    # check if the 'content' element does exist or is not array - but should have never gotten here
                    raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
                else:
                    if len(parameter['content']) == 1:
                        # GLOBLANI PROMENNA BYLA STANOVENA NA ZAKLADE TOHO, ZE TAM JE JEN JEDEN PARAMETER -> MUSI SE PRIDAT DO LOKALNICH PROMENNYCH
                        globe.global_params_with_value[parameter['name']] = parameter['content'][0]
                        # globe.global_params_reserved.append(parameter['name'])
                        single_params_array.append(parameter)
                        taged_string = replace_the_tag_with_value(taged_string, tag, parameter['content'][0], param_idx)
                        # the number of tags in string decreased -> the parameters has to be decreased as well (the param_idx has to be the same in next run -> now it gets -1, at the end of while it gets +1)
                        param_idx-=1
                    else:
                        combine_params_array.append(parameter)
        elif parameter['type'] == 'local_variable':
            """ LOCAL VARIABLE """
            if 'content' not in parameter.keys():
                # content key should exist in parameter info
                raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
            if type(parameter['content']) is not list:
                # content should be an array
                raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
            # check if the content does have only one element
            if len(parameter['content']) == 1:
                single_params_array.append(parameter)
                taged_string = replace_the_tag_with_value(taged_string, tag, parameter['content'], param_idx)
                # the number of tags in string decreased -> the parameters has to be decreased as well (the param_idx has to be the same in next run -> now it gets -1, at the end of while it gets +1)
                param_idx-=1
            else:
                combine_params_array.append(parameter)
        elif parameter['type'] == 'enumerate':
            """ ENUMERATE """
            # can be string or list (should not have a list with one value, but it is supported here as well just to be sure)
            if 'content' not in parameter.keys():
                # content key should exist in parameter info
                raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
            if type(parameter['content']) is str:
                """ STRING """
                # if enumerate is a string, it has only one value for sure -> can be replaced
                single_params_array.append(parameter)
                taged_string = replace_the_tag_with_value(taged_string, tag, parameter['content'], param_idx)
                # the number of tags in string decreased -> the parameters has to be decreased as well (the param_idx has to be the same in next run -> now it gets -1, at the end of while it gets +1)
                param_idx-=1
            elif type(parameter['content']) is list:
                """ ARRAY """
                # check if the content does have only one element
                if len(parameter['content']) == 1:
                    exit(1)
                    single_params_array.append(parameter)
                    taged_string = replace_the_tag_with_value(taged_string, tag, parameter['content'], param_idx)
                    # the number of tags in string decreased -> the parameters has to be decreased as well (the param_idx has to be the same in next run -> now it gets -1, at the end of while it gets +1)
                    param_idx-=1
                else:
                    combine_params_array.append(parameter)
            else:
                # other types of content are not supported 
                raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
        else:
            raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
        param_idx+=1

    """
    Check if the size of single_params_array + combine_params_array == all_params_array
    """
    if len(single_params_array) + len(combine_params_array) != all_params_array:
        raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
    
    """
    Check if the number of tags in string is still the same as the number of parameters which will be combined (to make sure all tags will be replaced afterwards)
    """
    tag_count = taged_string.count(tag)
    if tag_count != len(combine_params_array):
        raise ShouldHaveNotGottenHereError(__name__, "remove_single_values_params")
    # return the tuple of tagged string and the parameters to be combined for this string
    return taged_string,combine_params_array

def edit_the_parameter_array(element, parameter_array, location):
    """
    Edit the given array of parameters
    * check if a global variable already has a value
    * separate the enumerate string by separator
    * remove single values parameters
    * check if the global variable does have the value in global_params
    * extend the information about parameter of the possible value it can acquire
    """
    """
    Iterate over all elements in returned param array
    Different behavior for:
        * global_variable
            * if the global variable was used before -> set the 'Reserved': True 
            * if the global variable was not used before -> add a possible values parameter can acquire
        * local_variable
        * enumerate
    Variables:
    * inputed_global_params = global variables of input json file
    * global_params_reserved = indicates the global variable names which were used already 
    """ 
    inputed_global_params = globe.inputData.global_params
    separator = getattr(globe.config, location).enum.separator
    for parameter in parameter_array:
        if parameter['type'] == 'global_variable':
            """ GLOBAL VARAIBLE """
            if parameter['name'] in globe.global_params_reserved:
                # the global variable was used sometimes before (it will be replaced with a actual value after all combinations)
                parameter['reserved'] = True
            else:
                # the global variable was not used before
                if parameter['name'] not in inputed_global_params:
                    message = "The global parameter '{}' does not exist in input data".format(parameter['name'])
                    raise EndpointSemanticError(__name__, "edit_the_parameter_array", message)
                # insert the content array of this global variable into param information
                parameter['content'] = inputed_global_params[parameter['name']]
                # add this global to a reserved global variables (to forbit it to combine it multiple times)
                globe.global_params_reserved.append(parameter['name'])
        elif parameter['type'] == 'local_variable':
            """ LOCAL VARAIBLE """ 
            try:
                # Pop and get the first valuea of local parameters
                local_params_pop = element['local_params'].pop(0)
            except IndexError:
                message = "There is not enough local parameters in {}".format(location)
                raise EndpointSemanticError(__name__, "edit_the_parameter_array", message)
            try:
                # insert these values into parameter information
                parameter['content'] = local_params_pop['values']
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

def single_remove_global_from_string(tagged_string, global_values, location):
    """
    Replace the given tagged string with a values of global variables (stored in global_values as a dictionary)
    The location specifies which start and end tags were used to distinguish what is the global variable and what is not
    Input: 
    ('https://mydomain/addUser/4/GET/ABC/1/usr1/asd/fgh/<user>/A', {'user': 4, 'method': 'GET'})
    Output:
    ('https://mydomain/addUser/4/GET/ABC/1/usr1/asd/fgh/4/A', {'user': 4, 'method': 'GET'})
    """
    start_tag = getattr(globe.config, location).non_priority_start
    end_tag = getattr(globe.config, location).non_priority_end
    for key in global_values.keys():
        tag = start_tag + key + end_tag
        while tag in tagged_string:
            replacement = str(global_values[key])
            tagged_string = replace_the_tag_with_value(tagged_string, tag, replacement, 0)
    return tagged_string

def postprocessing_of_globals(tagedString_globalsArray, location):
    """ 
    Replace the global variables with values
    * if there is more global variables with a same name in one location -> only the first occurence is replaced if this function is not called
    """
    resulted_array = []
    for element in tagedString_globalsArray:
        new_tagged_string = single_remove_global_from_string(element[0], element[1], location)
        resulted_tuple = (new_tagged_string,element[1])
        resulted_array.append(resulted_tuple)
    return resulted_array

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

def split_combine_response_into_locations(combine_response, info_about_combine_blocks, endpoint, header, body):
    """
    Split the given combinations (combine result) by the location in which the parameter is used
    Evaluate if the result does make sense:
    * there can be only one 'indexes' value within the one location
    * if there is 'inexes' value -> there cannot be any 'parameters' values
    Example output:
        endpoint_combined_indexes = [5,1,3,4,5,2] - the values are indexes to array
            or
        endpoint_combine_response = [
            ['a', 1, 'aaa'],
            ['b', 2, 'bbb'],
            ['c', 3, 'ccc']
        ]
    """
    endpoint_combined_indexes = []
    header_combined_indexes = []
    body_combined_indexes = []

    endpoint_combine_response = []
    method_combine_response = []
    header_combine_response = []
    body_combine_response = [] 
    """ Split the combine response into another arrays """
    # Go through all test cases of combine request
    for case in combine_response:
        endies = []
        headies = []
        bodies = []
        methies = []

        if type(case) is not list:
            raise ShouldHaveNotGottenHereError(__name__, "split_combine_response_into_locations")

        # Go through all of the case's values
        for value_idx in range(len(case)):
            # Get the infromation about this value
            info_about_current_block = info_about_combine_blocks[value_idx]
            if info_about_current_block['location'] == 'endpoint':
                """ ENDPOINT """
                if info_about_current_block['type'] == 'indexes':
                    """ indexes """
                    index_value_of_this_case = endpoint[int(case[value_idx])]
                    endpoint_combined_indexes.append(index_value_of_this_case)
                elif info_about_current_block['type'] == 'parameters':
                    """ parameters """
                    value_of_case = case[value_idx]
                    endies.append(value_of_case)
                else:
                    raise ShouldHaveNotGottenHereError(__name__, "split_combine_response_into_locations")
            elif info_about_current_block['location'] == 'method':
                """ METHOD """
                if info_about_current_block['type'] == 'parameters':
                    """ parameters """
                    value_of_case = case[value_idx]
                    methies.append(value_of_case)
                else:
                    raise ShouldHaveNotGottenHereError(__name__, "split_combine_response_into_locations")
            elif info_about_current_block['location'] == 'header':
                """ HEADER """
                if info_about_current_block['type'] == 'indexes':
                    """ indexes """
                    value_of_case = header[int(case[value_idx])]
                    header_combined_indexes.append(value_of_case)
                elif info_about_current_block['type'] == 'parameters':
                    """ parameters """
                    value_of_case = case[value_idx]
                    headies.append(value_of_case)
                else:
                    raise ShouldHaveNotGottenHereError(__name__, "split_combine_response_into_locations")
            elif info_about_current_block['location'] == 'body':
                """ BODY """
                if info_about_current_block['type'] == 'indexes':
                    """ indexes """
                    value_of_case = body[int(case[value_idx])]
                    body_combined_indexes.append(value_of_case)
                elif info_about_current_block['type'] == 'parameters':
                    """ parameters """
                    value_of_case = case[value_idx]
                    bodies.append(value_of_case)
                else:
                    raise ShouldHaveNotGottenHereError(__name__, "split_combine_response_into_locations")
            else:
                raise ShouldHaveNotGottenHereError(__name__, "split_combine_response_into_locations")
        endpoint_combine_response.append(endies)
        method_combine_response.append(methies)
        header_combine_response.append(headies)
        body_combine_response.append(bodies)

    """ 
    Evaluate if the resulted arrays does make sense 
    * the amount of indexes used in one location cannot be higher then 1
    * if the indexes values are used -> there cannot be any parameter value
    * method can have only one parameter value
    """

    """ 
    Decide what should be returned
    * if the 'indexes' were used in location -> return {location}_combined_indexes
    * if the 'parameters' were used in location -> return {location}_combine_response
    """ 
    resulted_array = []
    # endpoint
    if len(endpoint_combined_indexes) > 0:
        resulted_array.append(endpoint_combined_indexes)
    else:
        resulted_array.append(endpoint_combine_response)
    # method
    resulted_array.append(method_combine_response)
    # header
    if len(header_combined_indexes) > 0:
        resulted_array.append(header_combined_indexes)
    else:
        resulted_array.append(header_combine_response)
    # body
    if len(body_combined_indexes) > 0:
        resulted_array.append(body_combined_indexes)
    else:
        resulted_array.append(body_combine_response)

    return resulted_array

def evaluate_endpoint_part_of_response(endpoint_combine_response, endpoint, endpoint_toggle):
    """ Evaluate the endpoint part of combine response """
    tag = globe.config.endpoint.non_priority_start + globe.config.endpoint.non_priority_end
    endpoint_test_cases = []
    if endpoint_toggle == 'indexes':
        endpoint_test_cases = endpoint_combine_response
    elif endpoint_toggle == 'parameters':
        endpoint_test_cases = evaluate_combine_response(endpoint_combine_response, endpoint, tag, 'endpoint')
    elif endpoint_toggle == 'done_string':
        # duplicate this string to have it in the same format (value, globals)
        temp_tuple = (endpoint[0], {})
        for _ in range(len(endpoint_combine_response)):
            endpoint_test_cases.append(temp_tuple)
    else:
        raise ShouldHaveNotGottenHereError(__name__, "add_method_to_combine_request")
    return endpoint_test_cases

def evaluate_method_part_of_response(method_combine_response, method, method_toggle):
    """ Evaluate the method part of combine response """
    tag = globe.config.method.non_priority_start + globe.config.method.non_priority_end
    method_test_cases = []
    if method_toggle == 'parameters':
        method_test_cases = evaluate_combine_response(method_combine_response, method, tag, 'method')
    elif method_toggle == 'done_string':
        # duplicate this string to have it in the same format (value, globals)
        temp_tuple = (method[0], {})
        for _ in range(len(method_combine_response)):
            method_test_cases.append(temp_tuple)
    else:
        raise ShouldHaveNotGottenHereError(__name__, "add_method_to_combine_request")
    return method_test_cases

def evaluate_header_part_of_response(header_combine_response, header, header_toggle):
    """ Evaluate the header part of combine response """
    tag = globe.config.header.non_priority_start + globe.config.header.non_priority_end
    header_test_cases = []
    if header_toggle == 'indexes':
        header_test_cases = header_combine_response
    elif header_toggle == 'parameters':
        header_test_cases = evaluate_combine_response(header_combine_response, header, tag, 'header')
    elif header_toggle == 'done_string':
        # duplicate this string to have it in the same format (value, globals)
        temp_tuple = (header[0], {})
        for _ in range(len(header_combine_response)):
            header_test_cases.append(temp_tuple)
    else:
        raise ShouldHaveNotGottenHereError(__name__, "add_method_to_combine_request")
    return header_test_cases

def evaluate_body_part_of_response(body_combine_response, body, body_toggle):
    """ Evaluate the body part of combine response """
    tag = globe.config.body.non_priority_start + globe.config.body.non_priority_end
    body_test_cases = []
    if body_toggle == 'indexes':
        body_test_cases = body_combine_response
    elif body_toggle == 'parameters':
        body_test_cases = evaluate_combine_response(body_combine_response, body, tag, 'body')
    elif body_toggle == 'done_string':
        # duplicate this string to have it in the same format (value, globals)
        temp_tuple = (body[0], {})
        for _ in range(len(body_combine_response)):
            body_test_cases.append(temp_tuple)
    else:
        raise ShouldHaveNotGottenHereError(__name__, "add_method_to_combine_request")
    return body_test_cases

def evaluate_main_combine_response(combine_response, info_about_combine_blocks, final_combinations, endpoint, method, header, body, toggles):
    """
    Evaluate the main combine response (combine the endpoint, method, header and body)
    Return an resulted combination tuple (array of values and it's variables)
    """
    endpoint_toggle = toggles[0]
    method_toggle = toggles[1]
    header_toggle = toggles[2]
    body_toggle = toggles[3]
    create_files_toggle = toggles[4]

    """ 
    Split the combine response into locations 
    """ 
    splited_combine_request = split_combine_response_into_locations(combine_response, info_about_combine_blocks, endpoint, header, body)
    endpoint_combine_response = splited_combine_request[0]
    method_combine_response = splited_combine_request[1]
    header_combine_response = splited_combine_request[2]
    body_combine_response = splited_combine_request[3]

    """
    Evaluate the combine response
    * Look into endpoint taged url 
        -> are there any tags? Or is it fulfiled? Should I have some toggle to indicate that?
        -> fill the tags with values -> what with a global variables behaviour -> should be similiar 
            algorithm to the one before -> but it has to support global variables across the all parts
    Look into method taged string 
        -> should it be skiped? Or should the value be taken
    Look into header taged string
    Look into body taged string
    """
    endpoint_test_cases = evaluate_endpoint_part_of_response(endpoint_combine_response, endpoint, endpoint_toggle)
    method_test_cases = evaluate_method_part_of_response(method_combine_response, method, method_toggle)
    header_test_cases = evaluate_header_part_of_response(header_combine_response, header, header_toggle)
    body_test_cases = evaluate_body_part_of_response(body_combine_response, body, body_toggle)

    """
    The number of endpoint, method, header and body values should be the same 
    Also, it should be the same as the number of cases returned from combine request
    """
    combine_response_length = len(combine_response)
    endpoint_test_cases_length = len(endpoint_test_cases)
    method_test_cases_length = len(method_test_cases)
    header_test_cases_length = len(header_test_cases)
    body_test_cases_length = len(body_test_cases)

    if not (combine_response_length == endpoint_test_cases_length == method_test_cases_length == header_test_cases_length == body_test_cases_length):
        raise ShouldHaveNotGottenHereError(__name__, "add_method_to_combine_request")
            
    """
    Replace all global params at all locations
    * Each global_variable is searched in all parts: endpoint, method, header, body
    Output example:
        result = [
            ([URL, method, header, body], {GLOBALS}),
            ([URL, method, header, body], {GLOBALS})
            ....
        ]
    """
    resulted_request_combination = []
    for test_case_idx in range(len(combine_response)):
        # get the values of endpoint, method, header and body for current test case
        endpoint,endpoint_globals = endpoint_test_cases[test_case_idx]
        method,method_globals = method_test_cases[test_case_idx]
        header,header_globals = header_test_cases[test_case_idx]
        body,body_globals = body_test_cases[test_case_idx]

        # get all the global params for this test case
        all_globals = {}
        all_globals.update(endpoint_globals)
        all_globals.update(method_globals)
        all_globals.update(header_globals)
        all_globals.update(body_globals)

        """
        Replace all global params at all locations
        * Each global_variable is searched in all parts: endpoint, method, header, body
        """
        for key in all_globals.keys():
            # endpoint
            start_tag = globe.config.endpoint.non_priority_start
            end_tag = globe.config.endpoint.non_priority_end
            tag = start_tag + key + end_tag
            while tag in endpoint:
                endpoint = replace_the_tag_with_value(endpoint, tag, str(all_globals[key]), 0)
            # method
            start_tag = globe.config.method.non_priority_start
            end_tag = globe.config.method.non_priority_end
            tag = start_tag + key + end_tag
            while tag in method:
                method = replace_the_tag_with_value(method, tag, str(all_globals[key]), 0)
            # header
            start_tag = globe.config.header.non_priority_start
            end_tag = globe.config.header.non_priority_end
            tag = start_tag + key + end_tag
            while tag in header:
                header = replace_the_tag_with_value(header, tag, str(all_globals[key]), 0)
            # body
            start_tag = globe.config.body.non_priority_start
            end_tag = globe.config.body.non_priority_end
            tag = start_tag + key + end_tag
            while tag in body:
                body = replace_the_tag_with_value(body, tag, str(all_globals[key]), 0)
        test_case = [endpoint, method, header, body]
        resulted_test_case_tuple = (test_case, all_globals)
        resulted_request_combination.append(resulted_test_case_tuple)

    """ 
    Add the resulted combinations of current request to the array with all requests in test sequence 
    """
    resulted_tuple = (resulted_request_combination, create_files_toggle)
    final_combinations.append(resulted_tuple)

def get_body_info(body_element):
    """
    Get the information about body part of request
    Output
    * Tuple (tagged_body, body_params) is returned
    * The body toggle is returned:
    ** 'indexes' means the combine call was called inside the body element
    ** 'parameters' means the values are not combined yet
    ** 'done_string' means nothing needs to be combined in body
    Possible inputs:
        * STRING - file path
            * value_is_body_string == False or value_is_body_string is not set
            * if only single file is passed, the parameters are searched in file content as well
            "values": "body.json"
            "values": "<>"
            "values": "<body1.json,body2.json,body3.json>"
            "values": "<:body_var:>"
        * STRING - body content
            * value_is_body_string == True
            "values": "TotoJeTelo"
            "values": "Toto<1,2,3>Telo"
            "values": "Toto<:variable:>Telo"
    """
    logging.debug('Getting info about body part')

    # this toggle indicates whatever the body files should have been created for each combination of the parameters (at the end of Suiter application)
    create_files_toggle = False

    """
    Get the type of a input specification
    Following formats are allowed:
    * STRING
    ** content is a file path (or multiple file paths)
    ** if value_is_body_string -> the content is not a file path, but the body content
    ** if there is only single file path -> the parameters can be searched inside of file as well
    """
    values_type = type(body_element['values'])
    if values_type is str:
        """ STRING """
        """
        Check if the string consists of file paths or body content
        """
        if 'value_is_string' in body_element:
            # get the boolean value 
            value_is_string = body_element['value_is_string']
        else:
            # value is file path
            value_is_string = False

        if value_is_string == True:
            """ if the content of body is given in input file, file has to be created for it """
            create_files_toggle = 'no_params'

        """ 
        Get all the parameters and their information from a given header string 
        """
        body_tuple = general_string_parser(body_element['values'], 'body', globe.param_id_counter, globe.config)
        tagged_string = body_tuple[0]
        param_array = body_tuple[1]

        """
        Edit the parameters
        * Insert all the values param can acquire
        """
        edit_the_parameter_array(body_element, param_array, 'body')

        """
        Remove the single values parameters
        Also, replace their value in tagged string
        """
        tagged_string,param_array = remove_single_values_params(tagged_string, param_array, 'body')

        """
        If there is only one file path, search the content of this file and look for a parameters inside
        """
        if len(param_array) == 0 and value_is_string == False:
            """ 
            Get all the parameters and their information from a given body file content 
            Set the create_files_toggle = True
            * at the end of the Suiter application, the body file for every combination has to be created
            """
            create_files_toggle = True
            file_content = get_file_content(tagged_string)
            tagged_string,param_array = general_string_parser(file_content, 'body', globe.param_id_counter, globe.config)

            """
            if no parameters were found in file content, each file for each body will not be created
            """
            if len(param_array) == 0:
                create_files_toggle = 'no_params'

            """
            Edit the parameters
            * Insert all the values param can acquire
            """
            edit_the_parameter_array(body_element, param_array, 'body')

            """
            Remove the single values parameters
            Also, replace their value in tagged string
            """
            tagged_string,param_array = remove_single_values_params(tagged_string, param_array, 'body')
    elif values_type is dict:
        raise ShouldHaveNotGottenHereError(__name__, "get_body_info")
    else:
        raise ShouldHaveNotGottenHereError(__name__, "get_body_info")

    """
    Check if all the values from local_params were used
    """
    if len(body_element['local_params']) != 0:
        message = "The number of local parameteres of body is higher then needed"
        raise InputFileError(__name__, "get_body_info", message)


    """
    Check if the 't-way' element is set
    Combine the parameters only within the body element
    """
    tag = globe.config.body.non_priority_start + globe.config.body.non_priority_end
    if 't-way' in body_element.keys():
        # get the value of t-way
        tway_value = body_element['t-way']

        # check if the t-way value does make sense in comparison with number of parameters
        number_of_parameteres = len(param_array)
        verify_tway_value(tway_value, number_of_parameteres)

        """
        Create a combine request for body
        """
        local_combine_call = globe.CombineCallClass()
        local_combine_call.body['t_strength'] = str(tway_value)
        # insert all parameters into a combine input
        for parameter in param_array:
            add_parameter_to_combine_call(parameter, local_combine_call)

        """ 
        Call the combine 
        """
        combine_response = api_call_combine(local_combine_call)

        """
        Evaluate the combine response
        """
        body_test_cases = evaluate_combine_response(combine_response, (tagged_string,param_array), tag, 'body')
        
        """
        Replace the global params with values
        * in case of multiple global parameters with a same name, the other occurences are replaced with value
        """
        body_test_cases = postprocessing_of_globals(body_test_cases, 'body')          
        return body_test_cases,'indexes',create_files_toggle
    else:
        resulted_tuple = (tagged_string,param_array)
        if len(param_array) == 0:
            return resulted_tuple,'done_string',create_files_toggle
        return resulted_tuple,'parameters',create_files_toggle

def get_header_info(header_element):
    """
    Get the information about header part of request
    Header param info is returned:
        * ex.: {"location": "header", 'type': 'enumerate', 'content': 'header1.yaml', 'id': 3}
        * ex.: {"location": "header", 'type': 'local_variable', 'content': '', 'name': 'var', 'id': 3}
        * ex.: {'location': 'header', 'type': 'global_variable', 'name': 'user', 'id': 4}
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

    """
    Get the type of a input specification
    Following formats are allowed:
    * STRING
    ** content is a file path (or multiple file paths)
    ** if there is only single file path -> the parameters can be searched inside a file as well
    * DICTIONARY
    """
    values_type = type(header_element['values'])
    if values_type is str:
        """ STRING """
        """ Get all the parameters and their information from a given header string """
        header_tuple = general_string_parser(header_element['values'], 'header', globe.param_id_counter, globe.config)
        tagged_string = header_tuple[0]
        param_array = header_tuple[1]

        """
        Edit the parameters
        * Insert all the values param can acquire
        """
        edit_the_parameter_array(header_element, param_array, 'header')

        """
        Remove the single values parameters
        Also, replace their value in tagged string
        """
        tagged_string,param_array = remove_single_values_params(tagged_string, param_array, 'header')

        """
        If there is only one file path, search the content of this file and look for a parameters inside
        """
        if len(param_array) == 0:
            # get file content
            file_content = get_file_content(tagged_string)
            # get the information of parameters inside of a file
            header_file_tuple = general_string_parser(file_content, 'header', globe.param_id_counter, globe.config)
            # edit the parameters (insert all the values param can acquire)
            edit_the_parameter_array(header_element, header_file_tuple[1], 'header')
            # remove single values parameters
            tagged_string,param_array = remove_single_values_params(header_file_tuple[0], header_file_tuple[1], 'header')
        else:
            """
            Replace the file paths with its value
            """
            for parameter in param_array:
                new_content_array = []
                for header_path in parameter['content']:
                    """ get the content of this file """
                    try:
                        header_file_content = json.dumps(get_header_from_file(header_path))
                    except:
                        message = "The header file content cannot be transfered to json"
                        raise OpenFileError(__name__, "get_header_info", message)
                    """ replace the quotes to double qoutes """
                    # replace the content from file path to it's value
                    new_content_array.append(header_file_content)
                parameter['content'] = new_content_array

    elif values_type is dict:
        """ DICTIONARY """
        # read the value and transfer it to a python dictionary
        header_value_string = json.dumps(header_element['values'])
        # get the information of parameters inside of a file
        tagged_string,param_array = general_string_parser(header_value_string, 'header', globe.param_id_counter, globe.config)

        # edit the parameters (insert all the values param can acquire)
        edit_the_parameter_array(header_element, param_array, 'header')

        tagged_string,param_array = remove_single_values_params(tagged_string, param_array, 'header')
    else:
        raise ShouldHaveNotGottenHereError(__name__, "get_header_info")

    """
    Check if all the values from local_params were used
    """
    if len(header_element['local_params']) != 0:
        message = "The number of local parameteres of header is higher then needed"
        raise InputFileError(__name__, "get_endpoint_info", message)

    """
    Check if the 't-way' element is set
    Combine the parameters only within the header element
    """
    tag = globe.config.header.non_priority_start + globe.config.header.non_priority_end
    if 't-way' in header_element.keys():
        # get the value of t-way
        tway_value = header_element['t-way']
        
        # check if the t-way value does make sense in comparison with number of parameters
        number_of_parameteres = len(param_array)
        verify_tway_value(tway_value, number_of_parameteres)

        """
        Create a combine request for header
        """
        local_combine_call = globe.CombineCallClass()
        local_combine_call.body['t_strength'] = str(tway_value)
        # insert all parameters into a combine input 
        for parameter in param_array:
            add_parameter_to_combine_call(parameter, local_combine_call)
       
        """ 
        Call the combine 
        """
        combine_response = api_call_combine(local_combine_call)

        """
        Evaluate the combine response
        """
        header_test_cases = evaluate_combine_response(combine_response, (tagged_string,param_array), tag, 'header')

        """
        Replace the global params with values
        * in case of multiple global parameters in header dictioanry, the other occurences are replaced with value
        """
        header_test_cases = postprocessing_of_globals(header_test_cases, 'header')

        return header_test_cases,'indexes' 

    resulted_tuple = (tagged_string,param_array)
    if len(param_array) == 0:
        return resulted_tuple,'done_string'
    return resulted_tuple,'parameters'

def get_method_info(method_element):
    """
    Get the information about method part of request
    Output
    * array of method parameters is returned:
        * ex.: {"location": "method", 'type': 'enumerate', 'content': 'GET', 'id': 4}
        * ex.: {"location": "method", 'type': 'variable', 'content': '', 'name': 'var', 'id': 4}
    * method toggle is returned
    ** 'parameters' means that the values in method needs to be combined
    ** 'done_string' means that the value is already evaluated and no combination is neccessary
    """
    logging.debug('Getting info about method part')

    """
    Get all the parameters and their information from a given method specification
    """
    parameters_tuple = general_string_parser(method_element['values'], 'method', globe.param_id_counter, globe.config)
    tagged_string = parameters_tuple[0]
    param_array = parameters_tuple[1]

    """
    Edit the parameters
    * Insert all the values param can acquire
    """
    edit_the_parameter_array(method_element, param_array, 'method')

    """
    Check if all the values from local_params were used
    """
    if len(method_element['local_params']) != 0:
        message = "The number of local parameteres of method is higher then needed"
        raise InputFileError(__name__, "edit_the_parameter_array", message)

    """
    Remove the single values parameters
    Also, replace their value in tagged string
    """
    tagged_string,param_array = remove_single_values_params(tagged_string, param_array, 'method')

    resulted_tuple = (tagged_string,param_array)
    if len(param_array) == 0:
        return resulted_tuple,'done_string'
    else:
        return resulted_tuple,'parameters'

def get_endpoint_info(endpoint_element):
    """
    Get the information about endpoint part of request
    Output
    * Tuple (tagged_url, endpoint_params) is returned
    * The endpoint toggle is returned:
    ** 'indexes' means the combine call was called inside the endpoint element
    ** 'parameters' means the values are not combined yet
    ** 'done_string' means nothing needs to be combined in endpoint url
    """
    logging.debug('Getting info about endpoint part')

    """
    Get the format of tag
    """
    tag = globe.config.endpoint.non_priority_start + globe.config.endpoint.non_priority_end
  
    """
    Get all the parameters and their information from a given URL string
    """
    parameters_tuple = general_string_parser(endpoint_element['values'], 'endpoint', globe.param_id_counter, globe.config)
    tagged_string = parameters_tuple[0]
    param_array = parameters_tuple[1]

    all_endpoint_params = param_array

    """
    Edit the parameters
    * Insert all the values param can acquire
    """
    edit_the_parameter_array(endpoint_element, param_array, 'endpoint')

    """
    Check if all the values from local_params were used
    """
    if len(endpoint_element['local_params']) != 0:
        message = "The number of local parameteres of endpoint is higher then needed"
        raise InputFileError(__name__, "edit_the_parameter_array", message)

    """
    Remove the single values parameters
    Also, replace their value in tagged string
    """
    tagged_string,param_array = remove_single_values_params(tagged_string, param_array, 'endpoint')

    """
    Check if the 't-way' element is set
    Combine the parameters only within the endpoint element
    """
    if 't-way' in endpoint_element.keys():
        # get the value of t-way
        tway_value = endpoint_element['t-way']

        # check if the t-way value does make sense in comparison with number of parameters
        number_of_parameteres = len(param_array)
        verify_tway_value(tway_value, number_of_parameteres)

        """
        Create a combine request for endpoint
        """
        local_combine_call = globe.CombineCallClass()
        local_combine_call.body['t_strength'] = str(tway_value)
        # insert all parameters into a combine input 
        for parameter in param_array:
            add_parameter_to_combine_call(parameter, local_combine_call)
       
        """ 
        Call the combine 
        """
        combine_response = api_call_combine(local_combine_call)

        """
        Evaluate the combine response
        """
        endpoint_test_cases = evaluate_combine_response(combine_response, (tagged_string,param_array), tag, 'endpoint')
    
        """
        Replace the global params with values
        * in case of multiple global parameters in url string, the other occurences are replaced with value
        """
        endpoint_test_cases = postprocessing_of_globals(endpoint_test_cases, 'endpoint')
        
        # 'indexes' indicates that the combine call was called inside of a endpoint element
        return endpoint_test_cases,"indexes"   
    else:
        resulted_tuple = (tagged_string,param_array)
        if len(param_array) == 0:
            return resulted_tuple,"done_string"
        else:
            return resulted_tuple,"parameters"

def create_input_file_for_templator(file_content, file_path):
    """
    Create a input file for templator module
    """

    call_idx = -1
    # the array with all the combinations + the information if the body/header files should have been created for each test_case
    final_combinations = []
    for call in globe.inputData.test_sequence:
        call_idx+=1
        logging.debug('Getting info about call')

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
        body,body_toggle,create_files_toggle = get_body_info(call['body'])

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
               
        """ 
        Call combine 
        Check if there are at least 2 parameters to be combined 
        """
        combine_response = []
        if len(info_about_combine_blocks) == 1:
            if info_about_combine_blocks[0]['location'] == 'endpoint':
                for element in endpoint[1][0]['content']:
                    combine_response.append([str(element)])
            elif info_about_combine_blocks[0]['location'] == 'method':
                for element in method[1][0]['content']:
                    combine_response.append([str(element)])
            elif info_about_combine_blocks[0]['location'] == 'header':
                for element in header[1][0]['content']:
                    combine_response.append([str(element)])
            elif info_about_combine_blocks[0]['location'] == 'body':
                for element in body[1][0]['content']:
                    combine_response.append([str(element)])
            toggles = [endpoint_toggle, method_toggle, header_toggle, body_toggle, create_files_toggle]
            evaluate_main_combine_response(combine_response, info_about_combine_blocks, final_combinations, endpoint, method, header, body, toggles)
        elif len(info_about_combine_blocks) == 0:
            """ 
            There are no parameters to combine
            * tway has to be equal 1 (checked in verify_tway_value function)
            * combine is not called
            * the combine_response is simualted (returns empty array)
            """ 
            # resulted_tuple = (resulted_request_combination, create_files_toggle)
            # final_combinations.append(resulted_tuple)
            resulted_request_combination = [([endpoint[0], method[0], header[0], body[0]], {})]
            resulted_tuple = (resulted_request_combination, create_files_toggle)
            final_combinations.append(resulted_tuple)
        else:
            combine_response = api_call_combine(combine_call)
            toggles = [endpoint_toggle, method_toggle, header_toggle, body_toggle, create_files_toggle]
            evaluate_main_combine_response(combine_response, info_about_combine_blocks, final_combinations, endpoint, method, header, body, toggles)
    # END FOR

    """
    Create a body files 
    """
    final_combinations = create_a_body_files(final_combinations)

    """
    Combine the resulted requests array 
    Create a file for templator in pretty format
    """
    # Check if there are multiple requests to be combined + at least one of the request has to have multiple combination values
    if 't-way' in file_content:
        final_result = prepare_final_combine_request(final_combinations, file_content)
    else:
        """ Create an array with values """
        final_result = []
        values_array = []
        indexes_array = []
        globals_array = []

        for element in final_combinations:
            ar = []
            idx_ar = []
            glob_ar = {}
            cnt = 0
            for combination in element:
                tup = (combination[0],combination[1])
                ar.append(tup)
                idx_ar.append(cnt)
                cnt+=1
            values_array.append(ar)
            indexes_array.append(idx_ar) 
        """ Combine each to each """
        import itertools
        combined = []
        for pair in itertools.product(*indexes_array):
            combined.append(pair)

        """ Get the values back """
        for combination in combined:
            value_idx = 0
            temp_array = []
            for value in combination:
                # print(value, value_idx, values_array[value_idx][value])
                temp_array.append(values_array[value_idx][value])
                value_idx+=1
            final_result.append(temp_array)

        """
        Replace all global variables with its actual value
        """
        final_final_result = []
        for case in final_result:
            """ Go through all the cases in combine response """
            cases_array = []
            all_globals = {}
            for req in case:
                """
                Go through every value in case. 
                * Replace the call indexes with their value and append the test case to a new array 'cases_array'
                * Get all the test case variables.
                """
                value_of_case = req[0]
                case_globals = req[1]
                all_globals.update(case_globals)
                cases_array.append(value_of_case)

            """ 
            Replace all the globals in the resulted test cases stored in a 'cases_array'
            """
            test_cases = []
            for element in cases_array:
                element_array = []
                location_cnt = 0 # 0 = endpoint, 1 = metrhod, 2 = header, 3 = body
                for part in element:
                    # what is the location -> to use the proper non priority tag
                    # TODO: tohle by se melo udelat i v combine casti
                    if location_cnt == 0:
                        loc = 'endpoint'
                    elif location_cnt == 1:
                        loc = 'method'
                    elif location_cnt == 2:
                        loc = 'header'
                    elif location_cnt == 3:
                        loc = 'body'
                    else:
                        exit(2)
                    part = single_remove_global_from_string(part, all_globals, loc)
                    element_array.append(part)
                    location_cnt+=1
                test_cases.append(element_array)
            final_final_result.append(test_cases)
            
        final_result = final_final_result 

    """
    Check if the number of test cases isn't too high
    The limit for number of test cases is specified in config file
    If the limit is exceeded -> ask user if he really wants to do that
    """
    number_of_allowed = int(globe.config.limits.final_tc_limit)
    number_of_test_cases = len(final_result)
    if number_of_test_cases > number_of_allowed:
        message = "The number of resulted test cases is higher then allowed. The number of test cases: {}, the nubmer of allowed test cases: {}. If you want to continue without asking, run an Suiter with --force argument. Do you want to continue?".format(number_of_test_cases, number_of_allowed)
        if yes_or_no(message) == False:
            exit(1)
    
    # create a file for templator
    create_a_resulted_file_pretty(final_result, file_path)
