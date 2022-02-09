"""
Main Suiter module
Provides a entry point of this application (main function)
"""

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
    logging.debug('Parsing the arguments')
    parser = argparse.ArgumentParser()
    # input file path
    parser.add_argument('filename', help='the input json file path', nargs='?', default=globe.config.default_input_file)
    # Framework
    framework_choices = ['Pytest', 'JavaScript']
    parser.add_argument('--framework', help='the framework of a resulted test suite ({} is default)'.format(globe.config.default_framework), choices=framework_choices,
    default=globe.config.default_framework)
    # output folder
    parser.add_argument('--output', help='the output folder location ({} is default)'.format(globe.config.default_output_folder), 
    default=globe.config.default_output_folder, metavar='output_folder')	
    # configuration file
    args = parser.parse_args()
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
    # template = get_executable_template("JavaScript", preparator_output_file)
    template = get_executable_template(framework, preparator_output_file)