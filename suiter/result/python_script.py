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
    if test_case == "test_case_1":
        assert response.status_code == 200
    
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
    if test_case == "test_case_1":
        url = "https://mydomain/addUser/"
        method = "GET"
        header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
        body = "./body_files/request_1_body_1"

    # DO NOT TOUCH THIS </DUPLICATE>
    return (url, method, header, body)

class TestClass(TestCase): 
    def test_sequence_1(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_1", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_1", "call_1", response, call)
        ### SUT Teardown ###
        teardown()

