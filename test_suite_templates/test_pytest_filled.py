from unittest import TestCase
from json import dumps
import requests

def setup():
    """
    TODO: Insert your additional code to define prerequisities of SUT
    """
    # databaze
    # nastaveni aplikace

def verify(test_case, request):
    """
    TODO: Modify following code or insert your own to define expected results
    """

    # expected headers are the same for all test cases
    headers = {
        'Content-Type': 'application/json', 
        'Access-Control-Allow-Origin': '*', 
    }

    if test_case == "tc1":
        if request == "request1":
            # TODO: Define outcome for this test case
            statusCode = None
            json = {'Result': None}
        elif request == "request2":
            # TODO: Define outcome for this test case
            statusCode = None
            json = {'Result': None}
        elif request == "request3":
            # TODO: Define outcome for this test case
            statusCode = None
            json = {'Result': None}
        else:
            raise Exception("Following test case does not exist)
    elif test_case == "tc2":
        tc2 = {"operation": "add", "num1": -1, "num2": -1}
        # TODO: Define outcome for this test case
        statusCode = 200
        json = {'Result': -2}
    elif test_case == "tc3":
        tc3 = {"operation": "add", "num1": 0, "num2": 0}
        # TODO: Define outcome for this test case
        statusCode = 200
        json = {'Result': -2}

    return (statusCode, json, headers)
    

def teardown():
    """
    TODO: Insert your code to set the SUT to the original state
    """
    return "TEARDOWN"

class MojeClassa(TestCase): 
    def MujTest(self):
        # SETUP
        setup()

        # request 1 execution
        url = "http://127.0.0.1:5000/api/v1/calculator"
        method = "GET"
        header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
        body = {"operation": "add", "num1": 1, "num2": 1}
        response = requests.request(method, url, headers=header, data=dumps(body))
        # request 1 verification
        expected = verify("tc1", "request1") # (statusCode, json, headers) tupple is returned
        assert response.status_code == expected[0] 
        assert response.json() == expected[1]
        assert response.headers['Access-Control-Allow-Origin'] == expected[2]['Access-Control-Allow-Origin']
        assert response.headers['Content-Type'] == expected[2]['Content-Type']

        # request 2 execution
        url = "http://127.0.0.1:5000/api/v1/calculator"
        method = "GET"
        header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
        body = {"operation": "add", "num1": 1, "num2": 1}
        response = requests.request(method, url, headers=header, data=dumps(body))
        # request 2 verification
        expected = verify("tc1", "request2") # (statusCode, json, headers) tupple is returned
        assert response.status_code == expected[0] 
        assert response.json() == expected[1]
        assert response.headers['Access-Control-Allow-Origin'] == expected[2]['Access-Control-Allow-Origin']
        assert response.headers['Content-Type'] == expected[2]['Content-Type']

        # request 3 execution
        url = "http://127.0.0.1:5000/api/v1/calculator"
        method = "GET"
        header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
        body = {"operation": "add", "num1": 1, "num2": 1}
        response = requests.request(method, url, headers=header, data=dumps(body))
        # request 3 verification
        expected = verify("tc1", "request3") # (statusCode, json, headers) tupple is returned
        assert response.status_code == expected[0] 
        assert response.json() == expected[1]
        assert response.headers['Access-Control-Allow-Origin'] == expected[2]['Access-Control-Allow-Origin']
        assert response.headers['Content-Type'] == expected[2]['Content-Type']

        # VERIFY
        expected = verify("tc1") # (statusCode, json, headers) tupple is returned
        assert response.status_code == expected[0] 
        assert response.json() == expected[1]
        assert response.headers['Access-Control-Allow-Origin'] == expected[2]['Access-Control-Allow-Origin']
        assert response.headers['Content-Type'] == expected[2]['Content-Type']

        # TEARDOWN
        teardown()