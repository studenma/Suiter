"""
Module provides a generator of test suits
"""

# import sys
# import os
# import stat
# import json
# import simplejson
# import yaml
# import requests
# import logging
# import subprocess
# import copy
# import argparse
# import importlib
# import inspect
# from ast import literal_eval

# from exceptions import LimitExceededError
# from pprint import pprint


# """
# Global variables
# """
# COMBINE_LOCAL = "http://127.0.0.1:3000" 
# COMBINE_URL = "https://combine.testos.org"
# test_script_language = "Python"
# file_path = "../test_suite_output/"
# file_name_base = "test_suite-"
# template_file_path = "../test_suite_templates/"
# # template_file_name = "pytest.template"
# template_file_name = "test_pytest.py"
# test_case_name = "test_case"
# sut_api_url = "http://127.0.0.1:5000/api/v1/calculator"
# test_case_identificator = "__test_case_id__"
# test_case_identificator_replacement = "tc"
# test_case_name_id = "def test_case(self):"
# tab = "    "
# config_path = '../config.ini'

# from template_picker import get_executable_template
# from input_parser import get_test_cases
# from input_parser import get_first_test_case
# from input_parser import input_file_parser

# from input_configuration import create_default_config
# from input_configuration import read_config_file

# full_template = True

""" general """
import logging
import argparse
""" Suiter modules """
from input_parser import read_config_file, open_input_json_file, input_json_structure_validator
from exceptions import *
from suiter_classes_and_globals import InputDataClass
from preparator import get_endpoint_info, get_method_info, get_header_info, get_body_info
import suiter_classes_and_globals as globe
from combine_request import create_combine_call, add_array_to_a_combine_call, add_parameter_to_combine_call, api_call_combine, evaluate_combine_response
from general import replace_the_tag_with_value
def logger_config():
    """
    Logger configuration
    """
    # log format with method name
    log_format_modules = '[%(asctime)s.%(msecs)d]-%(name)s-%(levelname)s: %(module)s.%(funcName)s: %(message)s'
    # log format without method name
    log_format = '[%(asctime)s.%(msecs)d]-%(name)s-%(levelname)s: %(message)s'
    # log configuration
    logging.basicConfig(level=logging.DEBUG, format=log_format, datefmt='%H:%M:%S')
    logging.basicConfig(level=logging.ERROR, format=log_format, datefmt='%H:%M:%S')

def argument_parser():
    """ The Suiter is an application to generate a test suite for a testing of API with usage of combinatory testing\n 
    How to use:
    1. The suiter creates a test suite for all inputs in a single application pass
        ./suiter input.json
    2. The Suiter creates only the test suite for the first input (-f argument). A user can modify what he needs and the other inputs are generated in the second pass of a Suiter (with a -d argument)
        a) ./suiter input.json -f
        b) ./suiter input.json -d 
    """
    logging.debug('Parsing the arguments')
    parser = argparse.ArgumentParser()
    # input file path
    parser.add_argument('filename', help='the input json file path', nargs='?', default=globe.config.default_input_file)
    # Framework
    framework_choices = ['Pytest', 'Nodejs', 'C#']
    parser.add_argument('--framework', help='the framework of a resulted test suite ({} is default)'.format(globe.config.default_framework), choices=framework_choices,
    default=globe.config.default_framework)
    # output folder
    parser.add_argument('--output', help='the output folder location ({} is default)'.format(globe.config.default_output_folder), 
    default=globe.config.default_output_folder, metavar='output_folder')	
    # configuration file

    """ Two application pass mode """
    group = parser.add_argument_group('two pass mode')
    group.add_argument('-f', '--first', help='create a test suite with only the first test case', action='store_true')
    group.add_argument('-d', '--duplicate', help='complete the test suite generated with --first argument', action='store_true')
    args = parser.parse_args()

    if args.first and args.duplicate:
        parser.error('--first and --duplicate cannot be given together')
    return args
    
if __name__ == "__main__":
    """ 
    The entry point of Suiter application 
    """

    """ LOGGER
    Setup the logging messages 
    """
    try:
        logger_config()
        logging.debug('The logging configuration was done succesfully')
    except:
        message = 'Something went wrong with a logging message configuration'
        raise LoggerError(__name__, "main", message)

    """ CONFIG
    * Read configuration file
    * Create a ConfigDataClass out of it (see suiter_classes module) 
    * Store this class into a 'config' global variable stored in suiter_classes_and_globals module
    * Extend the config class of a priority and non priority tags
    ** for cases where one tag is substring of another one (the priority ones are searched first)
    """
    globe.config = read_config_file(globe.config_path)
    globe.config.extend_of_priority_tags()

    """ ARGUMENT
    * Parse the arguments
    * Store following arguments into variable:
    ** file path a to an input json file
    ** what framework should be used
    ** the path to a dir where the output should be stored
    """
    try:
        args = argument_parser()
        # store 
        input_file_path = args.filename
        framework = args.framework
        output_path = args.output
        logging.debug('Parsing the arguments was succeful')
    except:
        message = 'Something went wrong with parsing of arguments'
        raise ArgumentError(__name__, "main", message)

    """ INPUT FILE PARSER
    Check if the given input file is valid (has to be json with a specific structure)
    Retrieve the data from input json file
    Create an object 'inputClass' store these data into it
    """
    # open
    file_content = open_input_json_file(input_file_path)
    # validate
    is_valid = input_json_structure_validator(file_content)
    if is_valid[0] == False:
        message = is_valid[1]
        raise InputFileError(__name__, "main", message)
    # store
    logging.debug('Creating the InputDataClass')
    globe.inputData = InputDataClass(file_content)



    """ CREATE FILE FOR TEMPLATOR
    Go through all calls in test sequence
    Get the information about each mandatory key (endpoint, method, header, body)
    Get the values of optional keys
    """

    call_idx = -1
    super_duper_result = []
    for call in globe.inputData.test_sequence:
        call_idx+=1
        logging.debug('Getting info about call')

        print("**************************************")
        print("**************************************")
        print("Call number {} in sequence".format(call_idx))
        print("**************************************")
        print("**************************************")

        """ create a combine request for this 'call' layer """
        combine_call = globe.CombineCallClass()
        combine_call.body['t_strength'] = call['t-way']

        endpoint,was_called_combine_in_endpoint = get_endpoint_info(call['endpoint'])
        method,was_called_combine_in_method = get_method_info(call['method'])
        header,was_called_combine_in_header = get_header_info(call['header'])
        body,was_called_combine_in_body = get_body_info(call['body'])

        info_about_combine_blocks = []
        """
        Add values to combine request body
        """
        """ ENDPOINT """
        if was_called_combine_in_endpoint:
            # -> pridava se do combine indexy v array (i s globalnimi promennymi) 
            list_of_indexes = []
            for idx in range(len(endpoint)):
                list_of_indexes.append(str(idx))
            add_array_to_a_combine_call(list_of_indexes, combine_call, "URL")
            info_about_combine_blocks.append({'location': 'endpoint', 'type': 'indexes'})
        else:
            # all parameters should be added to a combine call
            for parameter in endpoint[1]:
                add_parameter_to_combine_call(parameter, combine_call)
                info_about_combine_blocks.append({'location': 'endpoint', 'type': 'parameters'})

        """ METHOD """
        if was_called_combine_in_method:
            # DEAD CODE - nikdy se sem nemuze dostat
            print("Raise proper exception")
            exit(4)
        else:
            # if the method was filled already
            if len(method[1]) == 0:
                method = method[0]
                method_is_ready = True # indicates that the values is set alredy
            else:
                for parameter in method[1]:
                    # vzdycky tu bude jen jeden parameter - TODO: pridat kontrolu na to
                    add_parameter_to_combine_call(parameter, combine_call)
                    info_about_combine_blocks.append({'location': 'method', 'type': 'parameters'})
        
        """ HEADER """
        if was_called_combine_in_header:
            # get an array of BODY values
            array_values = []
            for element in header:
                array_values.append(element[0])
            add_array_to_a_combine_call(array_values, combine_call, "HEADER")
            info_about_combine_blocks.append({'location': 'header', 'type': 'indexes'})
        else:
            # pridaji se pouze informace o parametru
            for element in header[1]:
                add_parameter_to_combine_call(element, combine_call)
                info_about_combine_blocks.append({'location': 'header', 'type': 'parameters'})

        """ BODY """
        if was_called_combine_in_body:
            # get an array of BODY values
            list_of_indexes = []
            for idx in range(len(body)):
                list_of_indexes.append(str(idx))
            add_array_to_a_combine_call(list_of_indexes, combine_call, "BODY")
            info_about_combine_blocks.append({'location': 'body', 'type': 'indexes'})
        else:
            # pridaji se pouze informace o parametru
            for element in body[1]:
                add_parameter_to_combine_call(element, combine_call)
                info_about_combine_blocks.append({'location': 'body', 'type': 'parameters'})

        print("------ MAIN COMBINE CALLS ----")
        for element in combine_call.body['parameters']:
            print(element)

        print("------ INFO ABOUT BLOCKS -----")
        for element in info_about_combine_blocks:
            print(element)
        
        """
        COMBINE CALL
        """
        combine_response = api_call_combine(combine_call)

        print("----------COMBINE MAIN RESPONSE-----------")
        for element in combine_response:
            print(element)

        """
        check if the number of values for the first case is equal to the number of it's descriptions
        """
        if len(info_about_combine_blocks) != len(combine_response[0]):
            print("Proper exception is raised")
            exit(4)



        """
        Evaluate the combine response
        Look into endooint taged url 
            -> are there any tags? Or is it fulfiled? Should I have some toggle to indicate that?
            -> fill the tags with values -> what with a global variables behaviour -> should be similiar 
                algorithm to the one before -> but it has to support global variables across the all parts
        Look into method taged string 
            -> should it be skiped? Or should the value be taken
        Look into header taged string
        Look into body taged string
        """
        globes = []

        
        """
        result = [
            ([URL, method, header, body], {GLOBALS}),
            ([URL, method, header, body], {GLOBALS})
            ....
        ]
        """
        result = []

        print("------------")
        # print(endpoint[0])
        # print(endpoint[1])
        # print(endpoint[2])
        # print(endpoint[3])
        # print(endpoint[4])
        print("------------")


        print("----------INFO ABOUT COMBINE BLOCKS-----------")
        for element in info_about_combine_blocks:
            print(element)

        endpoint_is_evaluated = False

        header_param_array = []
        body_param_array = []
        endpoint_test_cases = []
        body_test_cases = []
        case_cnt = 0
        # Projdi jednotlive pripady z combine response
        for case in combine_response:
            test_case_parts = []
            headers = []
            bodies = []
            # projdi vsechny jeho hodnoty
            for value_idx in range(len(case)):
                # get the infromation about this value
                info_about_current_block = info_about_combine_blocks[value_idx]
                if info_about_current_block['location'] == 'endpoint':
                    """ ENDPOINT """
                    if info_about_current_block['type'] == 'indexes':
                        value_of_case = endpoint[int(case[value_idx])]
                        endpoint_test_cases.append(value_of_case)
                    else:
                        None
                    endpoint_is_evaluated = True
                elif info_about_current_block['location'] == 'method':
                    """ METHOD """
                    if info_about_current_block['type'] == 'indexes':
                        None
                    else:
                        None
                elif info_about_current_block['location'] == 'header':
                    if info_about_current_block['type'] == 'indexes':
                        None
                    else:
                        value_of_case = case[value_idx]
                        headers.append(value_of_case)
                        
                elif info_about_current_block['location'] == 'body':
                    if info_about_current_block['type'] == 'indexes':
                        value_of_case = body[int(case[value_idx])]
                        body_test_cases.append(value_of_case)
                    else:
                        value_of_case = case[value_idx]
                        bodies.append(value_of_case)
                else:
                    None
            header_param_array.append(headers)
            body_param_array.append(bodies)
            case_cnt+=1


        """
        IT ALREADY HAS A VALUE -> DUPLICATE IT FOR ALL TEST CASES
        """
        if endpoint_is_evaluated == False:
            for _ in range(len(header_param_array)):
                endpoint_tuple = (endpoint[0], {})
                endpoint_test_cases.append(endpoint_tuple) 

        # METHOD duplicate
        method_test_cases = []
        for _ in range(len(header_param_array)):
            method_tuple = (method, {})
            method_test_cases.append(method_tuple)       

        endpoint_test_cases = endpoint_test_cases
        method_test_cases = method_test_cases
        header_test_cases = evaluate_combine_response(header_param_array, header, '<>', 'header', [])
        body_test_cases = evaluate_combine_response(body_param_array, body, '<>', 'body', [])

        print(body)
        if call_idx == 1:
            print("jsem tady")
            print("TODO: Proc ma body stale hodnotu z minuleho pruchodu? Proc je body_param_array empty?")
            print(call_idx)
            exit(1)

        print("---------- MAIN COMBINE RESPONSE EVALUATION -----------")
        print("---------- endpoint_test_cases -----------")
        for element in endpoint_test_cases:
            print(element)
        print("---------- method_test_cases -----------")
        for element in method_test_cases:
            print(element)
        print("---------- header_test_cases -----------")
        for element in header_test_cases:
            print(element)
        print("---------- body_test_cases -----------")
        for element in body_test_cases:
            print(element)

        

        print("-----")
        print(len(endpoint_test_cases))
        print(len(method_test_cases))
        print(len(header_test_cases))
        print(len(body_test_cases))

        print("---------------")
        for test_case_idx in range(len(endpoint_test_cases)):
            endpoint,endpoint_globals = endpoint_test_cases[test_case_idx]
            method,method_globals = method_test_cases[test_case_idx]
            header,header_globals = header_test_cases[test_case_idx]
            body,body_globals = body_test_cases[test_case_idx]

            print("-----")
            print(endpoint)
            print(method)
            print(header)
            print(body)
            print("-----")
            all_globals = {}
            all_globals.update(endpoint_globals)
            all_globals.update(method_globals)
            all_globals.update(header_globals)
            all_globals.update(body_globals)
            print(all_globals)

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

            print("-----")
            print(endpoint)
            print(method)
            print(header)
            print(body)
            print("-----")

            test_case = [endpoint, method, header, body]
            resulted_tuple = (test_case, all_globals)
            result.append(resulted_tuple)

        

        for element in result:
            print(element)  

        super_duper_result.append(result)

    #     resulted_array = []
    #     # go through all test cases returned from combine
    #     for case in combine_response:
    #         temp_info_array = info_about_combine_blocks.copy()
    #         result_body = body[0]
    #         # while it has some value (they are poped one by one)
    #         while len(case) != 0:
    #             case_value = case.pop(0)
    #             block_info = temp_info_array.pop(0)
    #             local_globes = {}
    #             if block_info['location'] == 'endpoint':
    #                 if block_info['type'] == 'indexes':
    #                     case_idx = int(case_value)
    #                     # update the local_globes with a globals retreived from endpoint
    #                     local_globes.update(endpoint[case_idx][1])
    #                     # projdi vsechny promenne a podivej se, jestli nejsou obsazeny ve stringu
    #                     for key in local_globes.keys():
    #                         lookfor = '<' + key + '>'
    #                         if lookfor in endpoint[case_idx][0]:
    #                             tmp_tag_string = replace_the_tag_with_value(endpoint[case_idx][0], lookfor, str(local_globes[key]), 0)
    #                 else:
    #                     """ type = 'parameters' """
    #                     None
    #             elif block_info['location'] == 'method':
    #                 if block_info['type'] == 'indexes':
    #                     None
    #                 else:
    #                     """ type = 'parameters' """
    #                     None
    #             elif block_info['location'] == 'header':
    #                 if block_info['type'] == 'indexes':
    #                     None
    #                 else:
    #                     """ type = 'parameters' """
    #                     None
    #             elif block_info['location'] == 'body':
    #                 if block_info['type'] == 'indexes':
    #                     None
    #                 else:
    #                     """ type = 'parameters' """
    #                     print("Jsem tady a budu upravovat body parametry")
    #                     result_body = replace_the_tag_with_value(result_body, '<>', str(case_value), 0)
    #                     print(result_body)
    #                     # tag = '<>'
    #                     # evaluate_combine_response_parameter(case_value)
    #                     # test_cases_endpoint = evaluate_combine_response(combine_response, endpoint, tag, 'endpoint', [])
    #             else:
    #                 print("exception")
    #                 exit(1)
    #         exit(1)
        

    #     """
    #     The evaluation is based on fact if the array indexes are combined, or actual values are combined
    #     """
    #     """ ENDPOINT """
    #     if was_called_combine_in_endpoint:
    #         for idx in range(len(endpoint)):
    #             # find the value of this index with it's global variables

    #             # for variable in endpoint[idx][1]:
    #                 # globes[idx][variable] = endpoint[idx][1][variable]
    #             endpoint_values = endpoint[idx][0]
    #             endpoint_globals = endpoint[idx][1]
    #             print(endpoint_values, endpoint_globals)

    #         exit(41)
    #     else:
    #         tag = globe.config.url.non_priority_start + globe.config.url.non_priority_end
    #         test_cases_endpoint = evaluate_combine_response(combine_response, endpoint, tag, 'endpoint', [])
    #         print("------------------")
    #         for tc in test_cases_endpoint:
    #             print(tc) # (filled string, global_params)
    #         # get the global variables from endpoint
    #         for element in test_cases_endpoint:
    #             globes.append(element[1])


    #     for element in globes:
    #         print(element)
    #     exit(1)

    #     if not was_called_combine_in_method:
    #         # check the globals in endpoint
    #         tag = globe.config.method.non_priority_start + globe.config.method.non_priority_end
    #         test_cases_method = evaluate_combine_response(combine_response, method, tag, 'method', globes) 
    #         print("------------------")
    #         for tc in test_cases_method:
    #             print(tc)
    #         for element in test_cases_method:
    #             globes.append(element[1])

    #     if not was_called_combine_in_header:
    #         tag = globe.config.header.non_priority_start + globe.config.header.non_priority_end
    #         test_cases_header = evaluate_combine_response(combine_response, header, tag, 'header', globes) 
    #         print("------------------")
    #         for tc in test_cases_header:
    #             print(tc)
    #         for element in test_cases_header:
    #             globes.append(element[1])
        
    #     if not was_called_combine_in_body:
    #         tag = globe.config.body.non_priority_start + globe.config.body.non_priority_end
    #         test_cases_body = evaluate_combine_response(combine_response, body, tag, 'body', globes) 
    #         print("------------------")
    #         for tc in test_cases_body:
    #             print(tc)
    #         for element in test_cases_body:
    #             globes.append(element[1])

    #     for element in combine_response:
    #         print(element)
    #         if len(element) != 0:
    #             print("raise proper exception")
    #             exit(99)

    #     e_len = len(test_cases_endpoint)
    #     m_len = len(test_cases_method)
    #     h_len = len(test_cases_header)
    #     b_len = len(test_cases_body)
        
    #     if not (e_len == m_len == h_len == b_len):
    #         print("TODO exception")
    #         exit(5)

    #     call_result = []
    #     for idx in range(e_len):
    #         call_result.append( [ test_cases_endpoint[idx][0], test_cases_method[idx][0], test_cases_header[idx][0], test_cases_body[idx][0] ] )

        
    #     print("----")
    #     for element in call_result:
    #         print(element)
            

    #     # endpoint_test_cases = evaluate_combine_response(combine_response, combine_params, tag, 'endpoint')
    #     exit(2)

    #     print("TODO: Je potreba vyzkouset volani combine na nulte urovni")
    #     print("TODO: Je potreba dodelat body a header")
      
        
        

    #     if endpoint[1] == True:
    #         # TODO: 
    #         # for endpoint combine was already called
    #         None
        
        
    #     # TODO: jsem tady po pauze: je potreba dodelat header a body get information
    #     # TODO: dodelat promennou v metode
    #     print("jsem tady po pauze")
    #     exit(5)
    
    # exit(1)


    # exit(1)

    # # get all test cases
    # test_cases = get_test_cases("./templator_input")
    # # test_cases = get_test_cases("../test_cases/calls_4/tests_100")

    # """
    # First test case only / All test cases
    # """
    # if full_template == False:
    #     # get first test case
    #     first_test_case = get_first_test_case(test_cases)
    #     # create a executable template based on a first test case
    #     template = get_executable_template(framework, first_test_case)
    # else:
    #     # create a executable template based on all test cases
    #     template = get_executable_template(framework, test_cases)


    