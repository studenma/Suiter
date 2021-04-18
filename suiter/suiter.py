"""
Main Suiter module
Provides a entry point of this application (main function)

Functions:

logger_config()
argument_parser()
"""

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


import logging
import argparse

from suiter_input_parser import read_config_file, open_input_json_file, input_json_structure_validator
from suiter_exceptions import *
from suiter_preparator import get_endpoint_info, get_method_info, get_header_info, get_body_info, single_remove_global_from_string, create_input_file_for_templator
import suiter_classes_and_globals as globe
from suiter_combine_request import create_combine_call, add_array_to_a_combine_call, add_parameter_to_combine_call, api_call_combine, evaluate_combine_response
from suiter_general import replace_the_tag_with_value
from suiter_templator import get_test_cases, get_executable_template

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
    """ The entry point of Suiter application """

    """
    Setup the logging messages 
    """
    try:
        logger_config()
        logging.debug('The logging configuration was done succesfully')
    except:
        message = 'Something went wrong with a logging message configuration'
        raise LoggerError(__name__, "main", message)

    """
    Read configuration file
    * Create a ConfigDataClass out of it (see suiter_classes module) 
    * Store this class into a 'config' global variable
    * Extend the config class of a priority and non priority tags
    ** for cases where one tag is substring of another one (the priority ones are searched first)
    """
    globe.config = read_config_file(globe.config_path)
    globe.config.extend_of_priority_tags()

    """ 
    Parse the arguments
    * Store following arguments into variable:
    ** file path a to an input json file
    ** what framework should be used
    ** the path to a dir where the output should be stored
    """
    try:
        logging.debug('Parsing the arguments')
        args = argument_parser()
        input_file_path = args.filename
        framework = args.framework
        output_path = args.output
    except:
        message = 'Something went wrong with parsing of arguments'
        raise ArgumentError(__name__, "main", message)

    """
    Check the input json file structure
    * Retrieve the data from input json file
    * Create an object 'inputClass' and store those data into it
    """
    logging.debug('Checking the input json file structure')
    file_content = open_input_json_file(input_file_path)
    is_valid = input_json_structure_validator(file_content)
    if is_valid[0] == False:
        message = is_valid[1]
        raise InputFileError(__name__, "main", message)
    globe.inputData = globe.InputDataClass(file_content)

    """
    Create a input file for templator module
    * Go through all requests in test sequence
    ** Get the information about each mandatory key (endpoint, method, header, body)
    *** call a combine if the 't-way' element is inside
    ** Call a combine to get all requests with combined values of endpoint, method, header and body
    * Combine all the resulted requests together with other requests in sequence
    """
    preparator_output_file = './result/preparator_output'
    combined_requests = create_input_file_for_templator(file_content, preparator_output_file) 

    """
    Create a resulted test script
    """
    template = get_executable_template("Pytest", preparator_output_file)
    
    print("Jsem na uplnem konci")
    exit(1)

















    # from ast import literal_eval
    # from general import get_file_content
    # from decider import get_executable_template
    # content = get_file_content("./templator_input2")
    # content_array = literal_eval(content)
    # from suiter_pytest import create_template as create
    # create('./pre-templates/pytest.py', content_array)
    # template = get_executable_template('Pytest', content_array)
    exit(42)

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

    exit(1)

    
    
    


    

    # print('[' + '\n')
    # # projdi vsechny test cases
    # for test_case in final_result:
    #     for call in test_case:
    #         print(call)
    #     exit(1)

    # f.write('[' + '\n')
    # tc_cnt = 0
    # # get the length of a first test case
    # last_tc = len(final_result[0])-1
    # for test_cases in final_result[0]:
    #     print(test_cases)
    #     exit(1)
    #     seq_cnt = 0
    #     last_seq = len(test_cases)-1
    #     f.write(tab+'[' + '\n')
    #     for tc in test_cases:
    #         if seq_cnt == last_seq:
    #             f.write(2*tab + str(tc) + '\n')
    #         else:
    #             f.write(2*tab + str(tc) + ',\n')
    #         seq_cnt+=1
    #     if tc_cnt == last_tc:
    #         f.write(tab+']' + '\n')
    #     else:
    #         f.write(tab+'],' + '\n')
    #         tc_cnt+=1
    
    # global test_cnt
    # test_cnt += 1

    # for element in templator_file_input:
    #     print(element)

    # templator_file_input = [templator_file_input] 
    
    # try:
    #     f = open('templator_input', 'w')
    # except:
    #     message = "Could not open a templator input file: " + header_path
    #     raise OpenFileError(__name__, "crate_templator_input_file", message)
    
    # f.write('[' + '\n')
    # tc_cnt = 0
    # last_tc = len(templator_file_input[0])-1
    # for test_cases in templator_file_input[0]:
    #     seq_cnt = 0
    #     last_seq = len(test_cases)-1
    #     f.write(tab+'[' + '\n')
    #     for tc in test_cases:
    #         if seq_cnt == last_seq:
    #             f.write(2*tab + str(tc) + '\n')
    #         else:
    #             f.write(2*tab + str(tc) + ',\n')
    #         seq_cnt+=1
    #     if tc_cnt == last_tc:
    #         f.write(tab+']' + '\n')
    #     else:
    #         f.write(tab+'],' + '\n')
    #         tc_cnt+=1

    # f.write(']' + '\n')
    # f.close()
    # exit(4)

    print("JSEM NA UPLNEM KONCI")
    exit(42)

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


    