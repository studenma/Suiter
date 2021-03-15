from unittest import TestCase
from json import dumps
import requests

def setup():
    #####################################
    # TODO: HERE IS YOUR CODE
    # Insert your code to define prerequisities of SUT

def verify(test_case, request_id):
    """
    Method to describe the expected values for all test cases
    Take into account that these if-else statements will be duplicated for all test cases
    You can also rewrite whole method from scretch and use [TODO:] argument while calling 
    suiter to avoid code duplicate 
    """
    if test_case == "test_case_1":
        if request_id == "call_1":
            #####################################
            # TODO: HERE IS YOUR CODE TO PREDEFINE ALL TEST CASE VERIFICATION
            # example:
            ## statusCode = None
            ## json = {'Result': None}
        elif request_id == "call_2":
            #####################################
            # TODO: HERE IS YOUR CODE TO PREDEFINE ALL TEST CASE VERIFICATION
            # example:
            ## statusCode = None
            ## json = {'Result': None}
    elif test_case == "test_case_2":
        if request_id == "call_1":
            #####################################
            # TODO: HERE IS YOUR CODE TO PREDEFINE ALL TEST CASE VERIFICATION
            # example:
            ## statusCode = None
            ## json = {'Result': None}
        elif request_id == "call_2":
            #####################################
            # TODO: HERE IS YOUR CODE TO PREDEFINE ALL TEST CASE VERIFICATION
            # example:
            ## statusCode = None
            ## json = {'Result': None}
    elif test_case == "test_case_3":
        if request_id == "call_1":
            #####################################
            # TODO: HERE IS YOUR CODE TO PREDEFINE ALL TEST CASE VERIFICATION
            # example:
            ## statusCode = None
            ## json = {'Result': None}
        elif request_id == "call_2":
            #####################################
            # TODO: HERE IS YOUR CODE TO PREDEFINE ALL TEST CASE VERIFICATION
            # example:
            ## statusCode = None
            ## json = {'Result': None}
    
    #####################################
    # TODO: HERE IS YOUR RETURN STATEMENT
    # example:
    ## return (statusCode, json)
    
def teardown():
    #####################################
    # TODO: HERE IS YOUR CODE
    # Write a code to set the SUT to it's original state
    # if it is dependend on given test_case, add a 'test_case' parameter to this function
    # and write a code for all test_cases
    ## def teardown(test_case):

def list_of_all_cases(test_case, request_id):
    """
    List of all test cases in this test suite
    """
    if test_case == "test_case_1":
        if request_id == "req1":
            url = "http://127.0.0.1:5000/api/v1/calculator1"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "body1.json"
        elif request_id == "req2":
            url = "http://127.0.0.1:5000/api/v1/calculator2"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "body2.json"
        elif request_id == "req3":
            url = "http://127.0.0.1:5000/api/v1/calculator3"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "body3.json"
    elif test_case == "test_case_2":
        if request_id == "req1":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "body1.json"
        elif request_id == "req2":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "body2.json"
        elif request_id == "req3":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "body3.json"
    elif test_case == "test_case_3":
        if request_id == "req1":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "body1.json"
        elif request_id == "req2":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "body2.json"
        elif request_id == "req3":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "body3.json"

    return (url, method, header, body)


class TestClass(TestCase): 
    def test_sequence(self):
        """
        SUT Setup
        """
        setup()

        """
        1. Request
        """
        # execution
        call = list_of_all_cases(test_case_id, "call1")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # request verification
        expected_response = verify(test_case_id, "call1")
        #####################################
        # TODO: HERE MAY BE YOUR ASSERTIONS
        # delete this part otherwise
        # the assertions have to be based on 'expected_response' variable
        # example:
        # assert response.status_code == expected_response.status_code
        # assert response.json() == expected_response.json

        """
        2. Request
        """
        # execution
        call = list_of_all_cases(test_case_id, "call2")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # request verification
        expected_response = verify(test_case_id, "call2")
        #####################################
        # TODO: HERE MAY BE YOUR ASSERTIONS
        # delete this part otherwise
        # the assertions have to be based on 'expected_response' variable
        # example:
        # assert response.status_code == expected_response.status_code
        # assert response.json() == expected_response.json

        """
        3. Request
        """
        # execution
        call = list_of_all_cases(test_case_id, "call3")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # request verification
        expected_response = verify(test_case_id, "call3")
        #####################################
        # TODO: HERE MAY BE YOUR ASSERTIONS
        # delete this part otherwise
        # the assertions have to be based on 'expected_response' variable
        # example:
        # assert response.status_code == expected_response.status_code
        # assert response.json() == expected_response.json


        """
        SUT Verification
        """
        result = verify(test_case_id, "sut")
        #####################################
        # TODO: HERE MAY BE YOUR ASSERTIONS
        # delete this part otherwise
        # the assertions have to be based on 'result' variable


        """
        SUT Teardown
        """
        teardown()
