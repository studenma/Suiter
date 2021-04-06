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
from preparator import get_endpoint_info, get_method_info, get_header_info
import suiter_classes_and_globals as globe

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
    * Create a ConfigDataClass (see suiter_classes module) out of it
    * Store this class into a 'config' global variable stored in global_stuff module
    * Extend the config class of a priority and non priority tags
    ** for cases where one tag is substring of another one (the priority one is searched first)
    """
    globe.config = read_config_file(globe.config_path)
    # extend the config class of a priority and non priority tags
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
    
    # print(inputData.test_sequence)
    # print(inputData.global_params)
    # print(inputData.main_level_tway)

    """ CREATE FILE FOR TEMPLATOR
    Go through all calls in test sequence
    Get the information about each mandatory key (endpoint, method, header, body)
    Get the values of optional keys
    """
    for call in globe.inputData.test_sequence:
        logging.debug('Getting info about call')
        endpoint = get_endpoint_info(call['endpoint'])
        method = get_method_info(call['method'])
        header = get_header_info(call['header'])
        print("---------------------")
        for element in globe.all_parameters:
            print(element)
        exit(4)
        body = get_body_info(call['body'])
        # TODO: jsem tady po pauze: je potreba dodelat header a body get information
        # TODO: dodelat promennou v metode
        print("jsem tady po pauze")
        exit(5)

    #     method = get_method_info(element['method'], config)
    #     header = get_header_info(element['header'], config)
    #     body = get_body_info(element['body'], config)
    # input_file_parser(input_file_path, conf)
    
    exit(1)


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


    