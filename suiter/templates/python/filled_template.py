from unittest import TestCase
from json import dumps
import requests

# the '__test_case_id__' will be replaced for a specified string + test case id
__test_case_id__ = "tc"

def setup():
    #####################################
    # TODO: HERE IS YOUR CODE
    # Insert your code to define prerequisities of SUT
    print("Nastavuji SUT")

def verify(test_case, request_id):
    """
    Method to describe the expected values for all test cases
    Take into account that these if-else statements will be duplicated for all test cases
    You can also rewrite whole method from scretch and use [TODO:] argument while calling 
    suiter to avoid code duplicate 
    """
    # <duplicate>
    if test_case == __test_case_id__:
        if request_id == "req1":
            statusCode = None
            json = {'Result': None}
        elif request_id == "req2":
            statusCode = None
            json = {'Result': None}
        elif request_id == "req3":
            statusCode = None
            json = {'Result': None}
    # </duplicate>

    return (statusCode, json)
    
    

def teardown():
    #####################################
    # TODO: HERE IS YOUR CODE
    # Write a code to set the SUT to it's original state
    # if it is dependend on given test_case, add a 'test_case' parameter to this function
    # and write a code for all test_cases
    ## def teardown(test_case):
    print("Nastavuji SUT zpatky na puvodni stav")

def list_of_all_cases(test_case, request_id):
    """
    List of all test cases in this test suite
    """
    # <tc_extend>
    if test_case == __test_case_id__:
        if request_id == "req1":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = {"operation": "add", "num1": 1, "num2": 1}
        elif request_id == "req2":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = {"operation": "add", "num1": 2, "num2": 2}
        elif request_id == "req3":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = {"operation": "add", "num1": 3, "num2": 3}
    # </tc_extend>
    
    return (url, method, header, body)


class TestClass(TestCase): 
    # <duplicate>
    def test_case(self):
        """
        SUT Setup
        """
        setup()

        """
        1. Request
        """
        # execution
        call = list_of_all_cases(__test_case_id__, "req1")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # request verification
        expected_response = verify(__test_case_id__, "req1")
        assert response.status_code == expected_response[0]
        assert response.json() == expected_response[1]

        """
        2. Request
        """
        # execution
        call = list_of_all_cases(__test_case_id__, "req2")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # verification
        expected_response = verify(__test_case_id__, "req2")
        assert response.status_code == expected_response[0]
        assert response.json() == expected_response[1]

        """
        3. Request
        """
        # execution
        call = list_of_all_cases(__test_case_id__, "req3")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # verification
        expected_response = verify(__test_case_id__, "req3")
        assert response.status_code == expected_response[0]
        assert response.json() == expected_response[1]

        """
        SUT Teardown
        """
        teardown()

    # </duplicate>