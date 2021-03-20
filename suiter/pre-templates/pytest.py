from unittest import TestCase
from json import dumps
import requests

def setup():
    #####################################
    # TODO: HERE IS YOUR CODE
    # Insert your code to define prerequisities of SUT
    None

def verify(test_case, request_id, response, context):
    """
    Method to describe the expected values for all test cases
    Take into account that these if-else statements will be duplicated for all test cases
    You can also rewrite whole method from scretch and use [TODO:] argument while calling 
    suiter to avoid code duplicate 
    context[0] = URL (string)
    context[1] = METHOD (string)
    context[2] = HEADERS (list)
    context[3] = BODY (file path)
    """
    # DO NOT TOUCH THIS <DUPLICATE>
<VERIFY>    
    # DO NOT TOUCH THIS </DUPLICATE>
    
def teardown():
    #####################################
    # TODO: HERE IS YOUR CODE
    # Write a code to set the SUT to it's original state
    # if it is dependend on given test_case, add a 'test_case' parameter to this function
    # and write a code for all test_cases
    ## def teardown(test_case):
    None

def list_of_all_cases(test_case, request_id):
    """
    List of all test cases in this test suite
    """
    # DO NOT TOUCH THIS <DUPLICATE>
<TEST_CASE_LIST>
    # DO NOT TOUCH THIS </DUPLICATE>
    return (url, method, header, body)

class TestClass(TestCase): 
<TEST_SEQUENCE>