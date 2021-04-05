"""
This module reads and do an analysis of an input file
The goal is to create an unified input file for suiter module
"""

from exceptions import TemplateError
from exceptions import OpenFileError
from exceptions import InputFileError
from exceptions import ConfigurationFileError
from exceptions import EndpointSemanticError
from file_handling import get_file_content
# from input_configuration import *
from ast import literal_eval
import json
import requests

import logging
logger = logging.getLogger(__name__)

combine_call = {}
combine_parameter_identifier = 0
global_params = {}
global_params_with_one_value = {}
cnt_param = 0
tab = "    "

templator_file_input = []

def api_call_combine(combine_body):
    """
    REST API call to combine
    """
    headers = {
        'content-type':'application/json'
    }
    combine_url = 'https://combine.testos.org/generate'

    print("SEND TO COMBINE:")
    print(combine_url)
    print(headers)
    print(combine_body)
    
    # Send REST API request
    try:
        response = requests.request("GET", combine_url, headers=headers, json=combine_body)
        print("RESPONSE FROM COMBINE:")
        print(response)
        print(response.content)
        # if proxy error
        if response.status_code == 502:
            # try to call it 5 more times
            for _ in range(5):
                response = requests.request("GET", combine_url, headers=headers, json=combine_body)
                print("RESPONSE FROM COMBINE:")
                print(response)
                print(response.content)
                # if some of the request is not Proxy error, break this loop and do not call combine anymore
                if response.status_code != 502:
                    break
        return response.json()
    except ValueError: # includes json.decoder.JSONDecodeError
        logging.error('Response from Combine is not in a valid JSON format 2')
        exit(9)

# https://stackoverflow.com/questions/35091557/replace-nth-occurrence-of-substring-in-string
def nth_repl(s, sub, repl, n):
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        return s[:find] + repl + s[find+len(sub):]
    return s

def remove_single_values_params(all_calls):
    combine_calls = []
    single_calls = []
    for element_idx in range(len(all_calls)):
        content = all_calls[element_idx]['content']
        # if is list with more then one value
        if (type(content) is list) and (len(content) != 1):
            combine_calls.append(all_calls[element_idx])
        # single value param
        else:
            single_calls.append(all_calls[element_idx])
    #         nth_repl(all_calls[element_idx], )

    #         global priority_tag
    # global not_priority_tag
    # global not_priority_tag_end
    return single_calls,combine_calls
    # """ ENDPOINT """
    # for element_idx in range(len(endpoint[1])):   
    #     
    #     if type(content) is not list:
    #         endpoint[1].pop(element_idx)
    #     else:
    #         # if it is list with only one value
    #         # should have never gotten here, but just to make sure
    #         if len(content) == 1:
    #             endpoint[1].pop(element_idx)

    # # store all params for combine in one array
    # for element in endpoint[1]:
    #     all_calls.append(element)

    
    # """ METHOD """
    # if type(method['content']) is not list:
    #     method = []
    # else:
    #     # check if it is an list with a single value or not
    #     if len(method['content']) == 1:
    #         method = []
    #     else:
    #         method = [method]
    # # store method to all_calls if there is more then one value
    # for element in method:
    #     all_calls.append(element)

    # """ HEADER """
    # # TODO:


    # """ BODY """
    # # TODO:

    return all_calls

def get_header_info(header, config):
    global cnt_param
    print("TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO")
    result = {"location": "header", 'type': 'header', 'content': header[0], 'id': cnt_param}
    cnt_param += 1
    return result

def get_body_info(body, config):
    global cnt_param
    print("TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO")
    result = {"location": "body", 'type': 'body', 'content': '', 'id': cnt_param}
    cnt_param += 1
    return result

def get_method_info(method, config):
    global cnt_param
    # if there is more then one value in array
    arr_size = len(method['values'])
    if arr_size == 1:
        result = {"location": "method", 'type': 'method', 'content': method['values'][0], 'id': cnt_param}
        cnt_param += 1
    elif arr_size > 1:
        result = {"location": "method", 'type': 'method', 'content': method['values'], 'id': cnt_param}
        cnt_param += 1
    else:
        message = "Should have never gotten here"
        raise EndpointSemanticError(__name__, "get_method_info", message) 
    return result

def replace_param_in_url(url, value, config):  
    url = url.replace(not_priority_tag+not_priority_tag_end, str(value), 1)
    return url

def complete_all_params(endpoint, method, header, body):
    all_calls = []
    """ ENDPOINT """
    for element in endpoint[1]:   
        all_calls.append(element)
    """ METHOD """
    all_calls.append(method)
    """ HEADER """
    all_calls.append(header)
    """ BODY """
    all_calls.append(body)

    for element in all_calls:
        print(element)
    return all_calls

def translate_response_case(tc_values, url, single_params, combine_params, response, config):
    # translate the reply
    # go through all params (including the single valued)
    # param id has to be sequencive
    # TODO: make for all combine response (so far just for one)
    # gradually pop all the elements in sinlge param and combine param array
    idx_counter = 0
    """ first pops """
    # single
    try:
        single = single_params.pop(0)
    except IndexError:
        single = None
    # combine
    try:
        comb = combine_params.pop(0)
    except IndexError:
        comb = None
    """ while """
    while (single != None) or (comb != None):
        if idx_counter == single['id']:
            # TODO: do somehing with it 
            # print("single {}".format(idx_counter))
            if single['location'] == 'endpoint':
                url = replace_param_in_url(url, single['content'], config)
            elif single['location'] == 'method':
                method = single['content']
            elif single['location'] == 'header':
                header = single['content']
            elif single['location'] == 'body':
                body = single['content']
            else:
                print("Dalse locations nejsou podporovany jeste single")
                break
            # pop next value
            try:
                single = single_params.pop(0)
            except IndexError:
                single = None
        elif idx_counter == comb['id']:
            next_response_value = response[0].pop(0)
            # TODO: do something with it 
            # print("combine {}".format(idx_counter))
            if comb['location'] == 'endpoint':
                url = replace_param_in_url(url, next_response_value, config)
            elif comb['location'] == 'method':
                method = next_response_value
            else:
                print("Dalse locations nejsou podporovany jeste combine")
                break
            # pop next value 
            try:
                comb = combine_params.pop(0)
            except IndexError:
                comb = None
        else:
            # TODO: raise proper exception
            print(single['id'])
            print(comb['id'])
            print("Indexy v sinlge param a combine param nejsou sekvencni, spadlo to na: {}".format(idx_counter))
            exit(1)
        idx_counter += 1
    # response list is a deep copy -> change here is visible everywhere
    # it is neccasary to pop the empty list out
    if len(response[0]) == 0:
        response.pop(0) 
    else:
        print("Sem se to nemelo nikdy dostat")
        exit(1)
    return url, method, header, body

test_cnt = 0

def add_sequence_to_templator_input_file(url, method, header, body, seq_id, test_case):
    global templator_file_input
    global test_cnt

    print("*" + url)
    print(seq_id, test_case)

    # if test_cnt == 1:
    #     print("jsem tu 3")
    #     for element in templator_file_input:
    #         print(element)
    #     print("\n")

    if seq_id == 0:
        # vytvorit vrstvu pro kazdy test case
        templator_file_input.append([[url,method,header,body]])
    else:
        templator_file_input[test_case].append([url,method,header,body])

    # if test_cnt == 1:
    #     for element in templator_file_input:
    #         print(element)
    #     exit(1)


def crate_templator_input_file(templator_file_input):
    global test_cnt
    test_cnt += 1

    for element in templator_file_input:
        print(element)

    templator_file_input = [templator_file_input] 
    
    try:
        f = open('templator_input', 'w')
    except:
        message = "Could not open a templator input file: " + header_path
        raise OpenFileError(__name__, "crate_templator_input_file", message)
    
    f.write('[' + '\n')
    tc_cnt = 0
    last_tc = len(templator_file_input[0])-1
    for test_cases in templator_file_input[0]:
        seq_cnt = 0
        last_seq = len(test_cases)-1
        f.write(tab+'[' + '\n')
        for tc in test_cases:
            if seq_cnt == last_seq:
                f.write(2*tab + str(tc) + '\n')
            else:
                f.write(2*tab + str(tc) + ',\n')
            seq_cnt+=1
        if tc_cnt == last_tc:
            f.write(tab+']' + '\n')
        else:
            f.write(tab+'],' + '\n')
            tc_cnt+=1

    f.write(']' + '\n')
    f.close()
    exit(4)

def get_data_from_input(content, config):
    global global_params
    # retrieve global variables
    global_params = content['global_params']

    global templator_file_input
    templator_file_input = []

    global seq_id
    seq_id = 0

    # retreive calls
    for element in content['test_sequence']:
        global cnt_param
        cnt_param = 0
        global test_case
        test_case = 0
        
        endpoint = get_endpoint_info(element['endpoint'], config)
        method = get_method_info(element['method'], config)
        header = get_header_info(element['header'], config)
        body = get_body_info(element['body'], config)

        # all_params together in one array
        all_params = complete_all_params(endpoint,method,header,body)

        # remove the parameteres with only single value (these are not called to combine)
        single_params,combine_params = remove_single_values_params(all_params)
        
        # append all parameters to a combine call
        for el in combine_params:
            if type(el['content'][0]) is int:
                el_type = 'integer'
            else:
                el_type = 'enum'
            add_parameter_to_combine_call(el_type, el['content'], el['id'])

        # TODO: get the t-wise 
        combine_call['t_strength'] = str(element['t-way'])

        print("*** ALL PARAMS ***")
        for element in all_params:
            print(element)
        print("******************")

        print("*** SINGLE PARAMS ***")
        for element in single_params:
            print(element)
        print("******************")

        print("*** COMBINE PARAMS ***")
        for element in combine_params:
            print(element)
        print("******************")

        print("*** POSLANO DO COMBINE ***")
        for element in combine_call['parameters']:
            print(element)
        print("*************************")
        
        # send request to combine
        response = api_call_combine(combine_call)

        print("*** COMBINE RESPONSE ***")
        for element in response:
            print(element)
        print("*************************")

        # go through all test cases
        url = endpoint[0]
        for element in response.copy():
            result_url,method,header,body = translate_response_case(element, url, single_params.copy(), combine_params.copy(), response, config)
            add_sequence_to_templator_input_file(result_url, method, header, body, seq_id, test_case)
            test_case+=1
        
        seq_id+=1
    crate_templator_input_file(templator_file_input)
        # so far, the first call in test case 0 is done
        # TODO: add this layer to resulted input file for template creator


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
    first_level_keys = ['test_sequence', 'global_params', 't-way']
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
    call_keys_optional = ['t-way', 'allow_duplicities', 'all-in-one-test']
    call_keys_mandatory = ['endpoint', 'method', 'header', 'body']
    allowed_methods = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE"]
    for idx in range(test_case_array_length):
        # is dict?
        if type(dictionary['test_sequence'][idx]) is not dict:
            message = "The test_sequence[{}] is not a dict".format(idx)
            return False,message
        # check mandatory call keys
        for element in call_keys_mandatory:
            if element not in dictionary['test_sequence'][idx].keys():
                message = "The '{}' element was not found in call keys in input file".format(element) 
                return False,message
        # check any other call keys
        for element in dictionary['test_sequence'][idx].keys():
            if (element not in call_keys_mandatory) and (element not in call_keys_optional):
                message = "The '{}' element is not supported".format(element) 
                return False,message
            if element in call_keys_optional:
                el_type = type(dictionary['test_sequence'][idx][element])
                if el_type is not int:
                    message = "The '{}' element is expected to be a integer, {} is given".format(element,el_type) 
                    return False,message
        # check if endpoint is a dict
        if type(dictionary['test_sequence'][idx]['endpoint']) is not dict:
            message = "The endpoint element is not a dictionary"
            return False,message
        # check mandatory endpoint keys
        endpoint_keys_mandatory = ['url', 'local_params']
        endpoint_keys_optional = ['t-way', 'allow-duplicities']
        for element in endpoint_keys_mandatory:
            if element not in dictionary['test_sequence'][idx]['endpoint'].keys():
                message = "The '{}' element was not found in endpoint dictionary".format(element) 
                return False,message
        # check all endpoint keys
        for element in dictionary['test_sequence'][idx]['endpoint'].keys():
            if (element not in endpoint_keys_mandatory) and (element not in endpoint_keys_optional):
                message = "The '{}' element is not supported".format(element) 
                return False,message
            # all optional keys should be integers
            if element in endpoint_keys_optional:
                el_type = type(dictionary['test_sequence'][idx]['endpoint'][element])
                if el_type is not int:
                    message = "The '{}' element does not have a valid type: expected: integer, {} is given".format(element, el_type) 
                    return False,message         
        # check local_param is array
        local_params_type = type(dictionary['test_sequence'][idx]['endpoint']['local_params'])
        if local_params_type is not list:
            message = "The local_params element is not a dictionary, but {}".format(local_params_type) 
            return False,message
        # check if url is string
        url_type = type(dictionary['test_sequence'][idx]['endpoint']['url'])
        if url_type is not str:
            message = "The url element is not a string, but {}".format(url_type) 
            return False,message
        # check if method is a dict
        method_type = type(dictionary['test_sequence'][idx]['method'])
        if method_type is not dict:
            message = "The method element is not a dictionary, but {}".format(method_type)
            return False,message
        # method content
        method_keys = ['values']
        for element in dictionary['test_sequence'][idx]['method'].keys():
            if element not in method_keys:
                message = "The '{}' element was not found in method dictionary".format(element) 
                return False,message
        # method value type check
        method_val_type = type(dictionary['test_sequence'][idx]['method']['values'])
        if method_val_type is not list:
            message = "The value element in method is not an array, but {}".format(method_val_type) 
            return False,message
        # method value content type check 
        for element in dictionary['test_sequence'][idx]['method']['values']:
            if element not in allowed_methods:
                message = "The element '{}' in method values array is not in allowed http methods".format(element) 
                return False,message    
        # header
        header_type = type(dictionary['test_sequence'][idx]['header'])
        if header_type is not list:
            message = "The header is not an array, but {}".format(header_type)
            return False,message
        # header content
        for element in dictionary['test_sequence'][idx]['header']:
            if type(element) is not str:
                message = "The header content is not a string, but {}".format(type(element))
                return False,message
        # body
        body_type = type(dictionary['test_sequence'][idx]['body'])
        if body_type is not list:
            message = "The body is not an array, but {}".format(body_type)
            return False,message
        # body content 
        for element in dictionary['test_sequence'][idx]['body']:
            if type(element) is not str:
                message = "The body content is not a string, but {}".format(type(element))
                return False,message
    """ check global_params element """
    global_params_type = type(dictionary['global_params'])
    if global_params_type is not dict:
        message = "The global_params is not a dictionary, but {}".format(global_params_type)
        return False,message
    for element in dictionary['global_params']:
        el_type = type(dictionary['global_params'][element])
        if el_type is not list:
            message = "The global_params's element {} is not a array, but {}".format(element, el_type)
            return False,message
    for element in dictionary['global_params']:
        # empty array is not allowed
        variable_array_len = len(dictionary['global_params'][element])
        if variable_array_len == 0:
            message = "The global_params's element {} is empty".format(element)
            return False,message
            
    """ TODO: check the t-way in first level """
    
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

def find_between(string, first, last, conf):
    """ Return the substring + the original string without this substring """
    try:
        start = string.index(first) + len(first)
        end = string.index(last, start)
        # remove the start and end tag
        newstr = string[:(start-len(first))] + conf.url_enum_start + conf.url_enum_end + string[(end+len(last)):]
        # put the start and the end tag again (always ENUM is used)
        # newstr = newstr[:(start-len(first))] + conf.url_enum_start + conf.url_enum_end + newstr[(start-len(first)):]
        position = start-len(first) + len(conf.url_enum_start) + len(conf.url_enum_end)
        name = string[start:end]
        if (conf.url_enum_start in name) or (conf.url_enum_end in name) or (conf.url_variable_start in name) or (conf.url_variable_end in name):
            message = "The url contains nested tags"
            raise EndpointSemanticError(__name__, "find_between", message)
        return (newstr, string[start:end], position)
    except ValueError:
        message = "Some of the tag was probably not ended"
        raise EndpointSemanticError(__name__, "find_between", message)

def prepare_combine_call():
    return {
        "name": "SUT name",
        "t_strength": "2",
        "dont_care_values": "no",
        "values":"values",
        "parameters": [],
        "constraints": []
    }

def add_parameter_to_combine_call(data_type, value_array, id):
    global combine_call

    # prepare identificator
    identificator = 'id_' + str(id)
    

    temp_array = []

    # prepare value_array (different for enum, integer,..)
    if data_type == 'enum':
        temp_array = value_array
    elif data_type == 'integer':
        for element in value_array:
            element = identificator + "=" + str(element)
            temp_array.append(element)
    else:
        print("Another data types are not supported yet")
        exit(2)

    new_param = {
        "identificator": identificator,
        "type": data_type,
        "blocks": temp_array
    }

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

def url_parser(url, conf):
    """ TODO: """
    logging.debug('Calling the url_parser function with a following parameter: {}'.format(url))
    # list of parameters in url
    # {'type': 'variable', 'name': 'user', 'id': 0}
    parameters = []

    # { variableName: CombineIdentifier }
    global_variables_to_set = {}

    url_param_set = {}  
    
    # find out which of the start tag is more important
    global priority_tag
    global not_priority_tag
    global not_priority_tag_end
    priority_tag = conf_variable_substring_evaluation(conf.url_enum_start, conf.url_variable_start)

    """
    repeat the finding process until no more parameters are found
    if the while is called more than the actual url lenght, the error is returned (just to be sure)
    """
    cnt_while = position = 0
    global cnt_param
    e_change = v_change = -1
    url_length = len(url)

    # the first search of start url tags
    enum_idx = url.find(conf.url_enum_start)
    vari_idx = url.find(conf.url_variable_start)
    while enum_idx != -1 or vari_idx != -1:       
        """
        If the ENUM and VARIABLE indexes were found in the same index
        -> it means one of them is substring of another one
        It is neccessary to find out which one if them is only substring
        The non substring one has always the priority (priority_tag)
        """
        # Relation between 'enum_idx' and 'vari_idx'
        if enum_idx == vari_idx:
            if priority_tag is conf.url_enum_start:
                not_priority_tag = conf.url_variable_start
                not_priority_tag_end = conf.url_variable_end
                url_tuple = find_between(url[position:], conf.url_enum_start, conf.url_enum_end, conf)
                temp = url
            
                url = url[:position] + url_tuple[0]
                content = url_tuple[1]
                position = len(temp[:position]) + url_tuple[2]

                p = {"location": "endpoint", "type": "enumerate", "content": content, "id": cnt_param}
                parameters.append(p)

                # this idx is solved for both of them
                e_change = enum_idx
                v_change = vari_idx
            elif priority_tag is conf.url_variable_start:
                not_priority_tag = conf.url_enum_start
                not_priority_tag_end = conf.url_enum_end
                # Get the variable name
                url_tuple = find_between(url[position:], conf.url_variable_start, conf.url_variable_end, conf)
                temp = url
                url = url[:position] + url_tuple[0]
                variable = url_tuple[1]
                position = len(temp[:position]) + url_tuple[2]

                p = {"location": "endpoint", "type": "variable", "content": '', "name": variable, "id": cnt_param}
                parameters.append(p)

                # this idx is solved for both of them
                v_change = vari_idx
                e_change = enum_idx
            else:
                message = "Should have never gotten here"
                raise EndpointSemanticError(__name__, "url_parser", message)
        else:
            if enum_idx < vari_idx:
                if enum_idx == -1:
                    url_tuple = find_between(url[position:], conf.url_variable_start, conf.url_variable_end, conf)
                    temp = url
                    url = url[:position] + url_tuple[0]
                    variable = url_tuple[1]
                    position = len(temp[:position]) + url_tuple[2]

                    p = {"location": "endpoint", "type": "variable", "content": '', "name": variable, "id": cnt_param}
                    parameters.append(p)

                    v_change = vari_idx
                    e_change = vari_idx
                else:
                    url_tuple = find_between(url[position:], conf.url_enum_start, conf.url_enum_end, conf)
                    temp = url
                    url = url[:position] + url_tuple[0]
                    content = url_tuple[1]
                    position = len(temp[:position]) + url_tuple[2]
                   
                    p = {"location": "endpoint", "type": "enumerate", "content": content, "id": cnt_param}
                    parameters.append(p)
                    e_change = enum_idx
                    v_change = enum_idx
            elif vari_idx < enum_idx:
                if vari_idx == -1:
                    url_tuple = find_between(url[position:], conf.url_enum_start, conf.url_enum_end, conf)
                    temp = url
                    url = url[:position] + url_tuple[0]
                    content = url_tuple[1]
                    position = len(temp[:position]) + url_tuple[2]

                    p = {"location": "endpoint", "type": "enumerate", "content": content, "id": cnt_param}
                    parameters.append(p)
                    # TODO: do something with content
                    e_change = enum_idx
                    v_change = enum_idx
                else:
                    url_tuple = find_between(url[position:], conf.url_variable_start, conf.url_variable_end, conf)
                    temp = url
                    url = url[:position] + url_tuple[0]
                    variable = url_tuple[1]
                    position = len(temp[:position]) + url_tuple[2]

                    p = {"location": "endpoint", "type": "variable", "content": '', "name": variable, "id": cnt_param}
                    parameters.append(p)

                    v_change = vari_idx
                    e_change = vari_idx
            else:
                message = "Should have never gotten here"
                raise EndpointSemanticError(__name__, "url_parser", message)

        """
        WHILE EVALUATION
        Find the first occurence of ENUM start tag or VARIABLE start tag
        in the next iteration of while, the already evaluated part of url is ignored
        (enum_idx+1 and vari_idx+1 means it starts to search from this index)
        if nothing is found -> -1 is returned
        """
        enum_idx = url.find(conf.url_enum_start, e_change+1)
        vari_idx = url.find(conf.url_variable_start, v_change+1)
        cnt_param += 1

        if cnt_while > url_length:
            message = "Should have never gotten here"
            raise EndpointSemanticError(__name__, "url_parser", message)
        else:
            cnt_while += 1
    
    return url,parameters

    # print(url)
    # for idx in range(len(parameters)):
    #     print(parameters[idx])
    # exit(9)

    # dictionary already set globals
    # global_var_list = {'user2': 12345, 'method': "GET"}
    # new_url = url

    # e_idx = 0
    # v_idx = 0
    # cnt = 0
    # while True:
    #     cnt += 1
    #     # find the first occurence of ENUM start tag or VARIABLE start tag
    #     enum_idx = url.find(conf.url_enum_start, e_idx)
    #     vari_idx = url.find(conf.url_variable_start, v_idx)
    #     print("Nasel jsem enum na {}".format(enum_idx))
    #     print("Nasel jsem vari na {}".format(vari_idx))
        
    #     # wnd of a while cycle - no more parameteres were found
    #     if enum_idx == -1 and vari_idx == -1:
    #         break

    #     # substring issue
    #     if enum_idx == vari_idx:
    #         # find out which of the start is more important
    #         priority_tag = conf_variable_substring_evaluation(conf.url_enum_start,conf.url_variable_start)
    #         print("priority is {}".format(priority_tag))

    #         # enum has priority
    #         if priority_tag is conf.url_enum_start:
    #             print("ENUM")
    #             # TODO: check if there are some values specified or it is empty
    #             # TODO: EMPTY -> prepare the call with a local variables
    #             # TODO: NOT EMPTY -> retrieve the values and prepare the call to combine
    #         # variable has priority
    #         else:
    #             print("VAR")
    #             v_idx = vari_idx + 1
    #             e_idx = vari_idx + 1
    #             print(v_idx)
    #             # retrieve the variable out of this tag
    #             url_tuple = find_between(url, conf.url_variable_start, conf.url_variable_end)
    #             old_url = url_tuple[0]
    #             variable = url_tuple[1]
    #             position = url_tuple[2]

    #             # check if the variable is already used previously
    #             if variable in global_var_list:
    #                 # YES -> replace this value (it is not part of the combinations)
    #                 # new_url = old_url[:position] + str(global_var_list[variable]) + old_url[position:]
    #                 new_url = old_url[:position] + conf.url_enum_start + conf.url_enum_end + old_url[position:]
    #                 print(new_url)
    #                 url_param_set[0] = global_var_list[variable]
    #             else:
    #                 # NO -> set the variable and prepare the values for combine (these values will be combined only here)
    #                 values = get_the_values_of_global_parameter(variable)
    #                 data_type = get_the_data_type_string(type(values[0]))
    #                 # TODO: check if all types in values are the same
    #                 param = add_parameter_to_combine_call(data_type, values)
    #                 print("------------")
    #                 print(param)
    #                 global_variables_to_set[variable] = param['identificator']
    #     elif enum_idx < vari_idx:
    #         print("ENUM 1 ")
    #         url_tuple = find_between(url[enum_idx:], conf.url_enum_start, conf.url_enum_end)
    #         print(url[enum_idx:])
    #         print(url_tuple)
    #         # TODO: add values to combine and remove it from new_url
    #         new_url = new_url[:position] + conf.url_enum_start + conf.url_enum_end + new_url[position:]
    #         print(new_url)
    #         # url_param_set[]
    #     elif enum_idx > vari_idx:
    #         None
    #     else:
    #         # TODO: raise proper error
    #         exit(1)
    #     if cnt == 2:
    #         exit(1)

    # for idx in range(len(url)):
    #     actual = url[idx]
    #     if actual is conf.url_variable_start[0]:

    #     print(actual)

    # find all positions of VAR_TAG_START
    
    # find all positions of VAR_TAG_END
    # find all positions of ENUM_TAG_START
    # find all positions of ENUM_TAG_END




    exit(1)

    print(url)
    url_tuple = (url, "")
    while True:
        url_tuple = find_between(url_tuple[0], conf.url_variable_start, conf.url_variable_end, conf)
        # end of the while cycle
        if url_tuple is False:
            break
        print(url_tuple[1])


    # https://mydomain/addUser/<:user>/<a,b,c,d>
    # in this case we have to look for the <: first
    # is_substring = conf_variable_substring_evaluation(conf.url_enum_start,conf.url_variable_start)
    # if type(is_substring) is list:
    #     # one of them is substring of the second one 

    # else:
    #     None

    # url = 'https://mydomain/addUser/<:user:>/<1,2,3>/<:user2:>/<>/<9,8,7>'
    # print(url)
    # temp = find_enum_param(url, conf.url_enum_start, conf.url_enum_end)
    # print(temp)
    # import re

    # s = 'asdf=5;iwantthis123jasdasdf=5;iwantthis123jasd'
    # result = re.search('asdf=5;(.*)123jasd', s)
    # print(result.group(1))

    # print(url)
    # print(url.find("<:"))
    exit(1)

def get_endpoint_info(request, config):
    """
    https://mydomain/addUser/<:user:>/<a,b,c,d>/<:user1:>/<:user2:>
    https://mydomain/addUser/<a,b,c,s,d>
    https://mydomain/addUser/sdvsdvsdvsd
    """
    global combine_call
    combine_call = prepare_combine_call()
    url_param_tuple = url_parser(request['url'], config)
    print(url_param_tuple)

    global_params_with_one_value['used'] = 456

    # replace the variable name with contnet
    # replace empty enumerate content with actual one
    for par_info in url_param_tuple[1]:
        if par_info['type'] == 'variable':
            # look in a list of global variables with already combined value
            if par_info['name'] in global_params_with_one_value:
                # replace the contnet with this value
                par_info['content'] = global_params_with_one_value[par_info['name']]
            # look in a list of global variables with enumerated values
            elif par_info['name'] in global_params:
                # replace variable name with values
                par_info['content'] = global_params[par_info['name']]
            else:
                message = "The global variable {} does not exist".format(par_info['content'])
                raise EndpointSemanticError(__name__, "get_endpoint_info", message)
        elif par_info['type'] == 'enumerate':
            if len(par_info['content']) == 0:
                print("Empty string")
                # get the first value in local_params
                print(request['local_params'])
                # replace the empty string with a values and remove element from local params (cannot be used anymore)
                par_info['content'] = request['local_params'].pop(0)['values']              
            else:
                print("Not empty string")
                # get the contnet in string format           
                # split the values and insert them into array
                # replace the content with this array
                par_info['content'] = par_info['content'].split(config.url_enum_separator)
        else:
            message = "Should have never gotten here"
            raise EndpointSemanticError(__name__, "get_endpoint_info", message)
    
    print(request)
    if 't-way' in request:
        # do combine call only for endpoint
        None
        print("jmflosdkfnmsaiodkfnmsakdlnfasdklnfc")
        print(request)
        exit(1)
    else:
        return url_param_tuple

def input_file_parser(file_path, config):
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

    get_data_from_input(input_dict, config)
    return

    # for each test sequence
    for element in input_dict['test_sequence']:
        # get information about endpoint
        endpoint = get_endpoint_info(element['endpoint'])
        print(endpoint)
        exit(42)
    # print(conf.url_enum_start)
    # conf.url_enum_start='<'
    # conf.url_enum_end='>'
    # URL_PARAM_ENUM_SEPARATOR=','
    # conf.url_variable_start='<:'
    # conf.url_variable_end=':>'
    
    exit(1)