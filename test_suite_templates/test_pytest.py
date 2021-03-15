from unittest import TestCase
from json import dumps
import requests

def setup():
    """
    TODO: Insert your additional code to define prerequisities of SUT
    """
    # HERE IS YOUR CODE
    # ...
    # ...
    # ...

def verify(test_case):
    """
    TODO: Modify following code or insert your own to define expected results
    """
    # <TEST_CASES>
    return None
    

def teardown():
    """
    TODO: Insert your code to set the SUT to the original state
    """
    # HERE IS YOUR CODE
    # ...
    # ...
    # ...

class test_class_name(TestCase): 
    def test_cases_name(self):
        # ENVIRNOMENT SETUP
        setup()
        
        # REQUEST setup
        url = "http://example.com/api/v1/exampleEndPoint"
        headers = {
            'Content-Type': 'application/json', 
            'Example-header-name': 'Example-header-value'
        }
        # REQUEST EXERCISE
        payload = {"operation": "add", "num1": 1, "num2": 1}
        response = requests.request("GET", url, headers=headers, data=dumps(payload))
        
        # VERIFY
        expected = verify("tc1") # (statusCode, json, headers) tupple is returned
        assert response.status_code == expected 
        assert response.json() == expected
        # assert response.headers['Access-Control-Allow-Origin'] == expected[2]['Access-Control-Allow-Origin']
        # assert response.headers['Content-Type'] == expected[2]['Content-Type']

        # TEARDOWN
        teardown()