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
    if test_case == "tc1":
        if request_id == "req1":
            statusCode = None
            json = {'Result': None}
        elif request_id == "req2":
            statusCode = None
            json = {'Result': None}
        elif request_id == "req3":
            statusCode = None
            json = {'Result': None}
    elif test_case == "tc2":
        if request_id == "req1":
            statusCode = None
            json = {'Result': None}
        elif request_id == "req2":
            statusCode = None
            json = {'Result': None}
        elif request_id == "req3":
            statusCode = None
            json = {'Result': None}
    elif test_case == "tc3":
        if request_id == "req1":
            statusCode = None
            json = {'Result': None}
        elif request_id == "req2":
            statusCode = None
            json = {'Result': None}
        elif request_id == "req3":
            statusCode = None
            json = {'Result': None}

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
    if test_case == "tc1":
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
    elif test_case == "tc2":
        if request_id == "req1":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'X-Pingback': 'https://example.com/xmlrpc.php', 'X-Powered-By': 'PHP/5.2.17', 'Clear-Site-Data': '"cache", "cookies"'}
            body = "body1.json"
        elif request_id == "req2":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'X-Pingback': 'https://example.com/xmlrpc.php', 'X-Powered-By': 'PHP/5.2.17', 'Clear-Site-Data': '"cache", "cookies"'}
            body = "body2.json"
        elif request_id == "req3":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'X-Pingback': 'https://example.com/xmlrpc.php', 'X-Powered-By': 'PHP/5.2.17', 'Clear-Site-Data': '"cache", "cookies"'}
            body = "body3.json"
    elif test_case == "tc3":
        if request_id == "req1":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'X-Pingback': 'https://example.com/xmlrpc.php', 'X-Powered-By': 'PHP/5.2.17', 'Clear-Site-Data': '"cache", "cookies"'}
            body = "body1.json"
        elif request_id == "req2":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'X-Pingback': 'https://example.com/xmlrpc.php', 'X-Powered-By': 'PHP/5.2.17', 'Clear-Site-Data': '"cache", "cookies"'}
            body = "body2.json"
        elif request_id == "req3":
            url = "http://127.0.0.1:5000/api/v1/calculator"
            method = "GET"
            header = {'X-Pingback': 'https://example.com/xmlrpc.php', 'X-Powered-By': 'PHP/5.2.17', 'Clear-Site-Data': '"cache", "cookies"'}
            body = "body3.json"
    
    return (url, method, header, body)


class TestClass(TestCase): 
    def test_sequence1(self):
        """
        SUT Setup
        """
        setup()

        """
        1. Request
        """
        # execution
        call = list_of_all_cases("tc1", "req1")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # request verification
        expected_response = verify("tc1", "req1")
        assert response.status_code == expected_response[0]
        assert response.json() == expected_response[1]

        """
        2. Request
        """
        # execution
        call = list_of_all_cases("tc1", "req2")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # verification
        expected_response = verify("tc1", "req2")
        assert response.status_code == expected_response[0]
        assert response.json() == expected_response[1]

        """
        3. Request
        """
        # execution
        call = list_of_all_cases("tc1", "req3")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # verification
        expected_response = verify("tc1", "req3")
        assert response.status_code == expected_response[0]
        assert response.json() == expected_response[1]


        """
        SUT asserts
        """
        assert response.status_code == expected_response[0]
        assert response.json() == expected_response[1]

        """
        SUT Teardown
        """
        teardown()

    def test_case2(self):
        """
        SUT Setup
        """
        setup()

        """
        1. Request
        """
        # execution
        call = list_of_all_cases("tc2", "req1")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # request verification
        expected_response = verify("tc2", "req1")
        assert response.status_code == expected_response[0]
        assert response.json() == expected_response[1]

        """
        2. Request
        """
        # execution
        call = list_of_all_cases("tc2", "req2")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # verification
        expected_response = verify("tc2", "req2")
        assert response.status_code == expected_response[0]
        assert response.json() == expected_response[1]

        """
        3. Request
        """
        # execution
        call = list_of_all_cases("tc2", "req3")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # verification
        expected_response = verify("tc2", "req3")
        assert response.status_code == expected_response[0]
        assert response.json() == expected_response[1]

        """
        SUT Teardown
        """
        teardown()

    def test_case3(self):
        """
        SUT Setup
        """
        setup()

        """
        1. Request
        """
        # execution
        call = list_of_all_cases("tc3", "req1")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # request verification
        expected_response = verify("tc3", "req1")
        assert response.status_code == expected_response[0]
        assert response.json() == expected_response[1]

        """
        2. Request
        """
        # execution
        call = list_of_all_cases("tc3", "req2")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # verification
        expected_response = verify("tc3", "req2")
        assert response.status_code == expected_response[0]
        assert response.json() == expected_response[1]

        """
        3. Request
        """
        # execution
        call = list_of_all_cases("tc3", "req3")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # verification
        expected_response = verify("tc3", "req3")
        assert response.status_code == expected_response[0]
        assert response.json() == expected_response[1]

        """
        SUT Teardown
        """
        teardown()

