from unittest import TestCase
from json import dumps
import requests

def setup():
    """
    How to setup
        1. Fill in the endpoint url (do not change name variable)
        2. Fill in the URL request headers (do not change name variable)
        3. Insert your additional code defining prerequisities of SUT
    """
    global url
    global headers

    # TODO: Fill in the endpoint URL
    url = "http://example.com/api/v1/exampleEndPoint"

    # TODO: Fill in the URL request headers
    headers = {
        'Content-Type': 'application/json', 
        'Example-header-name': 'Example-header-value'
    }

    """
    TODO: Insert your additional code to define prerequisities of SUT
    """
    # HERE IS YOUR CODE
    # ...
    # ...
    # ...

    return url, headers

def verify(test_case):
    """
    TODO: Modify following code or insert your own to define expected results
    """
    <TEST_CASES>
    

def teardown():
    """
    TODO: Insert your code to set the SUT to the original state
    """
    # HERE IS YOUR CODE
    # ...
    # ...
    # ...

# TODO: change test_class_name
class test_class_name(TestCase): 
    # TODO: change name of a test case
    def test_cases_name(stest_class_name::test_cases_nameelf):
        # SETUP
        setup()
        # EXERCISE
        payload = {"operation": "add", "num1": 1, "num2": 1}
        response = requests.request("GET", url, headers=headers, data=dumps(payload))
        # VERIFY
        expected = verify("tc1") # (statusCode, json, headers) tupple is returned
        assert response.status_code == expected[0] 
        assert response.json() == expected[1]
        assert response.headers['Access-Control-Allow-Origin'] == expected[2]['Access-Control-Allow-Origin']
        assert response.headers['Content-Type'] == expected[2]['Content-Type']

        # TEARDOWN
        teardown()