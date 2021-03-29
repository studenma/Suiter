"""
This module reads and do an analysis of an input file
The goal is to create an unified input file for suiter module
"""

from exceptions import TemplateError
from exceptions import OpenFileError
from exceptions import InputFileError
from exceptions import ConfigurationFileError
from file_handling import get_file_content
from input_configuration import *
from ast import literal_eval
import json

import logging
logger = logging.getLogger(__name__)

combine_call = {}
combine_parameter_identifier = 0

def get_test_cases(path):
    """
    Get list of test cases of a given file
    """
    logger.debug("Calling the get_test_cases with a following parameter: " + path)  

    content = get_file_content(path)
    # change format of test_cases from string to array
    content_array = literal_eval(content)
    return content_array

def get_first_test_case(test_cases_array):
    """ 
    Retrieve the first test case from an array with all test cases
    """
    logger.debug("Calling the get_first_test_case with a following parameter:\n" + str(test_cases_array))
    return test_cases_array[0]

def get_header_from_file(header_path):
    """ 
    Get the headers from a input file
    """
    logger.debug("Calling the get_header_from_file method with following parameter: " + header_path)
    
    try:
        f = open(header_path, 'r')
    except:
        message = "Could not open a header file: " + header_path
        raise OpenFileError(__name__, "get_header_from_file", message)

    header_dict = {}
    for line in f:
        header = line.split(":", 1)
        head = header[0].rstrip(' ')
        value = header[1].rstrip('\n').lstrip()
        header_dict[head] = value
    f.close()
    return header_dict

def is_input_json_valid(dictionary):
    """ 
    Check if the input json is valid 
    """
    logger.debug("Calling the is_input_json_valid function")

    # the first level should contain only two keys: 'test_sequence' and 'global_params'
    first_level_keys = ['test_sequence', 'global_params']
    first_level_input_keys = dictionary.keys()
    if len(first_level_input_keys) != len(first_level_keys):
        message = "The number of keys at the first level of input json file is not correct"
        return False,message
    for element in first_level_keys:
        if element not in first_level_input_keys:
            message = "The '{}' element was not found in input json file".format(element) 
            return False,message

    """ test_case branch check """
    # the test_sequence should be an array
    if type(dictionary['test_sequence']) is not list:
        message = "The 'test_sequence' key in the input json file was expected to be a list, but the {} is given".format(type(dictionary['test_sequence']))
        return False,message

    """ check every element in 'test_sequence' array """
    test_case_array_length = len(dictionary['test_sequence'])
    if test_case_array_length == 0:
        message = "The test_sequence array is empty"
        return False,message
    # following keys have to exist in every call
    call_keys = ['endpoint', 'method', 'header', 'body']
    for idx in range(test_case_array_length):
        # is dict?
        if type(dictionary['test_sequence'][idx]) is not dict:
            message = "The test_sequence[{}] is not a dict".format(idx)
            return False,message
        # check call keys
        for element in call_keys:
            if element not in dictionary['test_sequence'][idx].keys():
                message = "The '{}' element was not found in call keys in input file".format(element) 
                return False,message
        # check endpoint keys
        endpoint_keys = ['url']
        if type(dictionary['test_sequence'][idx]['endpoint']) is not dict:
            message = "The endpoint element is not a dictionary"
            return False,message
        for element in endpoint_keys:
            if element not in dictionary['test_sequence'][idx]['endpoint'].keys():
                message = "The '{}' element was not found in endpoint dictionary".format(element) 
                return False,message
        # method
        method_keys = ['values']
        for element in method_keys:
            if element not in dictionary['test_sequence'][idx]['method'].keys():
                message = "The '{}' element was not found in method dictionary".format(element) 
                return False,message
        # header
        if type(dictionary['test_sequence'][idx]['header']) is not list:
            message = "The header is not an array"
            return False,message
        # body
        if type(dictionary['test_sequence'][idx]['body']) is not list:
            message = "The body is not an array"
            return False,message
    return True,None

def conf_variable_substring_evaluation(var1, var2):
    """
    Return a more important tag:
        if the first variable is the substring of the second one: return var2
        if the second variable is the substring of the first one: return var1
    Return None if none of them are substrings
    """
    if var1 is var2:
        message = "The tag beggining '{}' and it's end '{}' can not be the same".format(var1,var2)
        raise ConfigurationFileError(__name__, "conf_variable_substring_evaluation", message)
    elif var1 in var2:
        return var2
    elif var2 in var1:
        return var1
    else:
        None

def find_between(string, first, last):
    """ Return the substring + the original string without this substring """
    try:
        start = string.index(first) + len(first)
        end = string.index(last, start)
        # remove the start and end tag
        newstr = string[:(start-len(first))] + URL_PARAM_ENUM_START_TAG + URL_PARAM_ENUM_END_TAG + string[(end+len(last)):]
        # put the start and the end tag again (always ENUM is used)
        # newstr = newstr[:(start-len(first))] + URL_PARAM_ENUM_START_TAG + URL_PARAM_ENUM_END_TAG + newstr[(start-len(first)):]
        position = start-len(first) + len(URL_PARAM_ENUM_START_TAG) + len(URL_PARAM_ENUM_END_TAG)
        return (newstr, string[start:end], position)
    except ValueError:
        print(string, first, last)
        exit(1)

def  prepare_combine_call():
    return {
        "name": "SUT name",
        "t_strength": "2",
        "dont_care_values": "no",
        "parameters": [],
        "constraints": []
    }

def add_parameter_to_combine_call(data_type, value_array):
    global combine_parameter_identifier
    global combine_call
    new_param = {
        "identificator": combine_parameter_identifier,
        "type": data_type,
        "blocks": value_array
    }
    combine_parameter_identifier += 1
    combine_call['parameters'].append(new_param)
    return new_param

def get_the_values_of_global_parameter(variable):
    if variable in input_dict['global_params']:
        return input_dict['global_params'][variable]
    else:
        # TODO: Raise a proper exception
        exit(1)

def get_the_data_type_string(type):
    if type is int:
        return "integer"
    elif type is str:
        return "string"

def url_parser(url):
    parameters = []
    new_url = url
    global_var_list = {'user2': 12345, 'method': "GET"}

    # { variableName: CombineIdentifier }
    global_variables_to_set = {}

    url_param_set = {}  
    
    # find out which of the start tag is more important
    priority_tag = conf_variable_substring_evaluation(URL_PARAM_ENUM_START_TAG, URL_PARAM_VARIABLE_START_TAG)

    """
    repeat the finding process until no more parameters are found
    if the while is called more than the actual url lenght, the error is returned (just to be sure)
    """
    cnt_while = position = cnt_param = 0
    e_change = v_change = -1
    url_length = len(url)

    # the first search of start url tags
    enum_idx = url.find(URL_PARAM_ENUM_START_TAG)
    vari_idx = url.find(URL_PARAM_VARIABLE_START_TAG)
    while enum_idx != -1 or vari_idx != -1:       
        """
        If the ENUM and VARIABLE indexes were found in the same index
        -> it means one of them is substring of another one
        It is neccessary to find out which one if them is only substring
        The non substring one has always the priority (priority_tag)
        """
        # Relation between 'enum_idx' and 'vari_idx'
        if enum_idx == vari_idx:
            if priority_tag is URL_PARAM_ENUM_START_TAG:
                url_tuple = find_between(url[position:], URL_PARAM_ENUM_START_TAG, URL_PARAM_ENUM_END_TAG)
                temp = url
            
                url = url[:position] + url_tuple[0]
                content = url_tuple[1]
                position = len(temp[:position]) + url_tuple[2]

                p = {"type": "enumerate", "content": content, "id": cnt_param}
                parameters.append(p)

                # this idx is solved for both of them
                e_change = enum_idx
                v_change = vari_idx
            elif priority_tag is URL_PARAM_VARIABLE_START_TAG:
                # Get the variable name
                url_tuple = find_between(url[position:], URL_PARAM_VARIABLE_START_TAG, URL_PARAM_VARAIBLE_END_TAG)
                temp = url
                url = url[:position] + url_tuple[0]
                variable = url_tuple[1]
                position = len(temp[:position]) + url_tuple[2]

                p = {"type": "variable", "content": variable, "id": cnt_param}
                parameters.append(p)

                # this idx is solved for both of them
                v_change = vari_idx
                e_change = enum_idx
            else:
                # TODO: raise a proper exception
                exit(1)
        else:
            if enum_idx < vari_idx:
                if enum_idx == -1:
                    url_tuple = find_between(url[position:], URL_PARAM_VARIABLE_START_TAG, URL_PARAM_VARAIBLE_END_TAG)
                    temp = url
                    url = url[:position] + url_tuple[0]
                    variable = url_tuple[1]
                    position = len(temp[:position]) + url_tuple[2]

                    p = {"type": "variable", "content": variable, "id": cnt_param}
                    parameters.append(p)

                    v_change = vari_idx
                    e_change = vari_idx
                else:
                    url_tuple = find_between(url[position:], URL_PARAM_ENUM_START_TAG, URL_PARAM_ENUM_END_TAG)
                    temp = url
                    url = url[:position] + url_tuple[0]
                    content = url_tuple[1]
                    position = len(temp[:position]) + url_tuple[2]
                   
                    p = {"type": "enumerate", "content": content, "id": cnt_param}
                    parameters.append(p)
                    e_change = enum_idx
                    v_change = enum_idx
            elif vari_idx < enum_idx:
                if vari_idx == -1:
                    url_tuple = find_between(url[position:], URL_PARAM_ENUM_START_TAG, URL_PARAM_ENUM_END_TAG)
                    temp = url
                    url = url[:position] + url_tuple[0]
                    content = url_tuple[1]
                    position = len(temp[:position]) + url_tuple[2]

                    p = {"type": "enumerate", "content": content, "id": cnt_param}
                    parameters.append(p)
                    # TODO: do something with content
                    e_change = enum_idx
                    v_change = enum_idx
                else:
                    url_tuple = find_between(url[position:], URL_PARAM_VARIABLE_START_TAG, URL_PARAM_VARAIBLE_END_TAG)
                    temp = url
                    url = url[:position] + url_tuple[0]
                    variable = url_tuple[1]
                    position = len(temp[:position]) + url_tuple[2]

                    p = {"type": "variable", "content": variable, "id": cnt_param}
                    parameters.append(p)

                    v_change = vari_idx
                    e_change = vari_idx
            else:
                # TODO; raise proper exception
                exit(1)

        """
        WHILE EVALUATION
        Find the first occurence of ENUM start tag or VARIABLE start tag
        in the next iteration of while, the already evaluated part of url is ignored
        (enum_idx+1 and vari_idx+1 means it starts to search from this index)
        if nothing is found -> -1 is returned
        """
        enum_idx = url.find(URL_PARAM_ENUM_START_TAG, e_change+1)
        vari_idx = url.find(URL_PARAM_VARIABLE_START_TAG, v_change+1)
        cnt_param += 1

        if cnt_while > url_length:
            # TODO: Raise a proper exception
            exit(1)
        else:
            cnt_while += 1
    
    return url,parameters
    print(url)
    for idx in range(len(parameters)):
        print(parameters[idx])
    exit(9)

    e_idx = 0
    v_idx = 0
    cnt = 0
    while True:
        cnt += 1
        # find the first occurence of ENUM start tag or VARIABLE start tag
        enum_idx = url.find(URL_PARAM_ENUM_START_TAG, e_idx)
        vari_idx = url.find(URL_PARAM_VARIABLE_START_TAG, v_idx)
        print("Nasel jsem enum na {}".format(enum_idx))
        print("Nasel jsem vari na {}".format(vari_idx))
        
        # wnd of a while cycle - no more parameteres were found
        if enum_idx == -1 and vari_idx == -1:
            break

        # substring issue
        if enum_idx == vari_idx:
            # find out which of the start is more important
            priority_tag = conf_variable_substring_evaluation(URL_PARAM_ENUM_START_TAG,URL_PARAM_VARIABLE_START_TAG)
            print("priority is {}".format(priority_tag))

            # enum has priority
            if priority_tag is URL_PARAM_ENUM_START_TAG:
                print("ENUM")
                # TODO: check if there are some values specified or it is empty
                # TODO: EMPTY -> prepare the call with a local variables
                # TODO: NOT EMPTY -> retrieve the values and prepare the call to combine
            # variable has priority
            else:
                print("VAR")
                v_idx = vari_idx + 1
                e_idx = vari_idx + 1
                print(v_idx)
                # retrieve the variable out of this tag
                url_tuple = find_between(url, URL_PARAM_VARIABLE_START_TAG, URL_PARAM_VARAIBLE_END_TAG)
                old_url = url_tuple[0]
                variable = url_tuple[1]
                position = url_tuple[2]

                # check if the variable is already used previously
                if variable in global_var_list:
                    # YES -> replace this value (it is not part of the combinations)
                    # new_url = old_url[:position] + str(global_var_list[variable]) + old_url[position:]
                    new_url = old_url[:position] + URL_PARAM_ENUM_START_TAG + URL_PARAM_ENUM_END_TAG + old_url[position:]
                    print(new_url)
                    url_param_set[0] = global_var_list[variable]
                else:
                    # NO -> set the variable and prepare the values for combine (these values will be combined only here)
                    values = get_the_values_of_global_parameter(variable)
                    data_type = get_the_data_type_string(type(values[0]))
                    # TODO: check if all types in values are the same
                    param = add_parameter_to_combine_call(data_type, values)
                    print("------------")
                    print(param)
                    global_variables_to_set[variable] = param['identificator']
        elif enum_idx < vari_idx:
            print("ENUM 1 ")
            url_tuple = find_between(url[enum_idx:], URL_PARAM_ENUM_START_TAG, URL_PARAM_ENUM_END_TAG)
            print(url[enum_idx:])
            print(url_tuple)
            # TODO: add values to combine and remove it from new_url
            new_url = new_url[:position] + URL_PARAM_ENUM_START_TAG + URL_PARAM_ENUM_END_TAG + new_url[position:]
            print(new_url)
            # url_param_set[]
        elif enum_idx > vari_idx:
            None
        else:
            # TODO: raise proper error
            exit(1)
        if cnt == 2:
            exit(1)

    # for idx in range(len(url)):
    #     actual = url[idx]
    #     if actual is URL_PARAM_VARIABLE_START_TAG[0]:

    #     print(actual)

    # find all positions of VAR_TAG_START
    
    # find all positions of VAR_TAG_END
    # find all positions of ENUM_TAG_START
    # find all positions of ENUM_TAG_END




    exit(1)

    print(url)
    url_tuple = (url, "")
    while True:
        url_tuple = find_between(url_tuple[0], URL_PARAM_VARIABLE_START_TAG, URL_PARAM_VARAIBLE_END_TAG)
        # end of the while cycle
        if url_tuple is False:
            break
        print(url_tuple[1])


    # https://mydomain/addUser/<:user>/<a,b,c,d>
    # in this case we have to look for the <: first
    # is_substring = conf_variable_substring_evaluation(URL_PARAM_ENUM_START_TAG,URL_PARAM_VARIABLE_START_TAG)
    # if type(is_substring) is list:
    #     # one of them is substring of the second one 

    # else:
    #     None

    # url = 'https://mydomain/addUser/<:user:>/<1,2,3>/<:user2:>/<>/<9,8,7>'
    # print(url)
    # temp = find_enum_param(url, URL_PARAM_ENUM_START_TAG, URL_PARAM_ENUM_END_TAG)
    # print(temp)
    # import re

    # s = 'asdf=5;iwantthis123jasdasdf=5;iwantthis123jasd'
    # result = re.search('asdf=5;(.*)123jasd', s)
    # print(result.group(1))

    # print(url)
    # print(url.find("<:"))
    exit(1)

def get_endpoint_info(request):
    """
    https://mydomain/addUser/<:user:>/<a,b,c,d>/<:user1:>/<:user2:>
    https://mydomain/addUser/<a,b,c,s,d>
    https://mydomain/addUser/sdvsdvsdvsd
    """

    global combine_call
    combine_call = prepare_combine_call()
    url_parser(request['url'])

    
    # if (URL_PARAM_ENUM_START_TAG and URL_PARAM_ENUM_END_TAG) in request['url']
    exit(1)

def input_file_parser(file_path):
    """ 
    Parse the input file 
    """
    logging.debug('Calling the input_file_parser function with a following parameter: {}'.format(file_path))

    global input_dict
    # open input json file and load its content
    try:
        with open(file_path) as json_file:
            input_dict = json.load(json_file)
    except ValueError:
        message = "The given file is not a json: {}".format(file_path)
        raise InputFileError(__name__, "input_file_parser", message) 
    except:
        message = "Could not open a input json file: " + file_path
        raise OpenFileError(__name__, "input_file_parser", message) 

    # check if the input file is valid
    is_valid = is_input_json_valid(input_dict)
    if is_valid[0] == False:
        message = is_valid[1]
        raise InputFileError(__name__, "is_input_json_valid", message)

    # for each test sequence
    for element in input_dict['test_sequence']:
        # get information about endpoint
        endpoint = get_endpoint_info(element['endpoint'])
        print(endpoint)
    # print(URL_PARAM_ENUM_START_TAG)
    # URL_PARAM_ENUM_START_TAG='<'
    # URL_PARAM_ENUM_END_TAG='>'
    # URL_PARAM_ENUM_SEPARATOR=','
    # URL_PARAM_VARIABLE_START_TAG='<:'
    # URL_PARAM_VARAIBLE_END_TAG=':>'
    
    exit(1)