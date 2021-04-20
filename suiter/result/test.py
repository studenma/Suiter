from unittest import TestCase
from json import dumps
import requests


class ContextClass(object):
    def __init__(self, requests, endpoint_params, method_params, header_params, body_params):
        self.list_of_requests = []
        for req_idx in range(len(requests)):
            request = self.requestClass(requests[req_idx], endpoint_params[req_idx], method_params[req_idx], header_params[req_idx], body_params[req_idx])
            self.list_of_requests.append(request)
    class requestClass(object):
        def __init__(self, request, endpoint_params, method_params, header_params, body_params):
            # actual values
            self.endpoint = request[0]
            self.method = request[1]
            self.header = request[2]
            self.body = request[3]
            # parameters
            self.endpoint_params = endpoint_params
            self.method_params = method_params
            self.header_params = header_params
            self.body_params = body_params

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
    if test_case == "test_case_01":
        if request_id == "call_1":
            """ Test Case 01 request 1
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1 """
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_02":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_03":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_04":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_05":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_06":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_07":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_08":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_09":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_10":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_11":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_12":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_13":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_14":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_15":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_16":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_17":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_18":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_19":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_20":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_21":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_22":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_23":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_24":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_25":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_26":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_27":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_28":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_29":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_30":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_31":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_32":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_33":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_34":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_35":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_36":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            # method = GET
            # header = {"Content-type": "json"}
            # body = ./body_files/request_2_body_1
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    else:
        raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))    
    
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
    if test_case == "test_case_01":
        if request_id == "call_1":
            # request specification
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
            request = [url, method, header, body]
            # parameters
            endpoint_params = ["add", "0", "0"]
            method_params = []
            header_params = ["json", "12"]
            body_params = ['"ID": "SGML"']

            moje_classa = ContextClass(request,endpoint_params,method_params,header_params,body_params)
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_02":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_03":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_04":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_05":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_06":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_07":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_08":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_09":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_10":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_11":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_12":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_13":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_14":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_15":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_16":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_17":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_18":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_19":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_20":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_21":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_22":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_23":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_24":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_25":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_26":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_27":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_28":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_29":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_30":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_31":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_32":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_33":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_34":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_35":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_36":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    else:
        raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))

    return (url, method, header, body)

class TestClass(TestCase): 
    def test_sequence_01(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_01", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_01", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_01", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_01", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_02(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_02", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_02", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_02", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_02", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_03(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_03", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_03", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_03", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_03", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_04(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_04", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_04", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_04", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_04", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_05(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_05", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_05", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_05", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_05", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_06(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_06", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_06", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_06", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_06", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_07(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_07", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_07", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_07", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_07", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_08(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_08", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_08", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_08", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_08", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_09(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_09", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_09", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_09", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_09", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_10(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_10", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_10", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_10", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_10", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_11(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_11", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_11", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_11", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_11", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_12(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_12", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_12", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_12", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_12", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_13(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_13", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_13", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_13", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_13", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_14(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_14", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_14", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_14", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_14", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_15(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_15", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_15", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_15", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_15", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_16(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_16", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_16", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_16", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_16", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_17(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_17", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_17", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_17", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_17", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_18(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_18", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_18", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_18", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_18", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_19(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_19", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_19", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_19", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_19", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_20(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_20", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_20", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_20", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_20", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_21(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_21", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_21", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_21", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_21", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_22(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_22", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_22", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_22", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_22", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_23(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_23", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_23", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_23", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_23", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_24(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_24", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_24", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_24", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_24", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_25(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_25", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_25", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_25", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_25", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_26(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_26", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_26", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_26", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_26", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_27(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_27", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_27", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_27", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_27", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_28(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_28", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_28", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_28", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_28", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_29(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_29", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_29", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_29", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_29", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_30(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_30", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_30", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_30", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_30", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_31(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_31", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_31", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_31", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_31", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_32(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_32", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_32", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_32", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_32", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_33(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_33", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_33", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_33", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_33", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_34(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_34", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_34", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_34", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_34", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_35(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_35", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_35", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_35", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_35", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_36(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_36", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_36", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_36", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_36", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

