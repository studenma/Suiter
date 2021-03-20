"""
This module reads and do an analysis of an input file
The goal is to create an unified input file for suiter module
"""

from exceptions import TemplateError
from exceptions import OpenFileError
from file_handling import get_file_content
from ast import literal_eval
import json

import logging
logger = logging.getLogger(__name__)

def get_framework(user_input):
    """
    Get the name of a framework to use
    """
    logger.debug("Calling the get_framework with a following parameter: " + user_input)

    framework = ""
    if user_input == "Python":
        framework = "Python"
    elif user_input == "Pytest":
        framework = "Pytest"
    elif user_input == "JavaScript":
        framework = "JavaScript"
    else:
        message = "The following framework is not supprted: " + user_input
        raise TemplateError(__name__, "get_framework", message)

    return framework

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