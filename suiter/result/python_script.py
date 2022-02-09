from unittest import TestCase
from json import dumps
import requests

class ContextClass(object):
    def __init__(self, request, endpoint_params, method_params, header_params, body_params):
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
    """
    if test_case == "test_case_001":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr1/4/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_002":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_003":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_004":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr2/4/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_005":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_006":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr2/4/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_007":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_008":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_009":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_1
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_010":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/B
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_2
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/GET/usr1/52/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_011":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/B
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_2
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/GET/usr2/52/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_012":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/B
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_2
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/POST/usr1/52/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_013":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/B
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_2
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/POST/usr2/52/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_014":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/B
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_2
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/DELETE/usr1/52/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_015":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/B
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_2
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/DELETE/usr2/52/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_016":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/B
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_2
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/GET/usr2/52/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_017":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/B
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_2
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/DELETE/usr1/52/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_018":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/B
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_2
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/POST/usr1/52/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_019":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_3
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/GET/usr1/3/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_020":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_3
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/GET/usr2/3/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_021":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_3
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/POST/usr1/3/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_022":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_3
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/POST/usr2/3/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_023":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_3
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/DELETE/usr1/3/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_024":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_3
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/DELETE/usr2/3/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_025":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_3
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/GET/usr2/3/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_026":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_3
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/DELETE/usr1/3/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_027":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_3
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/POST/usr1/3/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_028":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_4
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/GET/usr1/1/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_029":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_4
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/GET/usr2/1/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_030":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_4
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/POST/usr1/1/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_031":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_4
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/POST/usr2/1/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_032":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_4
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/DELETE/usr1/1/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_033":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_4
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/DELETE/usr2/1/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_034":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_4
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/GET/usr2/1/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_035":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_4
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/DELETE/usr1/1/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_036":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_4
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/POST/usr1/1/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_037":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/A
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_5
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr1/4/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_038":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/A
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_5
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_039":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/A
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_5
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_040":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/A
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_5
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr2/4/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_041":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/A
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_5
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_042":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/A
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_5
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr2/4/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_043":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/A
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_5
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_044":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/A
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_5
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_045":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/A
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_5
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_046":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_6
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/GET/usr1/77/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_047":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_6
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/GET/usr2/77/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_048":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_6
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/POST/usr1/77/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_049":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_6
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/POST/usr2/77/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_050":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_6
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/DELETE/usr1/77/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_051":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_6
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/DELETE/usr2/77/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_052":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_6
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/GET/usr2/77/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_053":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_6
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/DELETE/usr1/77/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_054":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_6
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/POST/usr1/77/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_055":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_7
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/GET/usr1/52/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_056":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_7
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/GET/usr2/52/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_057":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_7
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/POST/usr1/52/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_058":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_7
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/POST/usr2/52/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_059":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_7
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/DELETE/usr1/52/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_060":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_7
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/DELETE/usr2/52/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_061":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_7
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/GET/usr2/52/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_062":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_7
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/DELETE/usr1/52/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_063":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_7
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/POST/usr1/52/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_064":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/A
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_8
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr1/4/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_065":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/A
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_8
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_066":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/A
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_8
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_067":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/A
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_8
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr2/4/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_068":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/A
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_8
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_069":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/A
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_8
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr2/4/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_070":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/A
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_8
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_071":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/A
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_8
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_072":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/A
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_8
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_073":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/3/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_9
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/GET/usr1/77/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_074":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/3/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_9
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/GET/usr2/77/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_075":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/3/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_9
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/POST/usr1/77/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_076":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/3/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_9
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/POST/usr2/77/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_077":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/3/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_9
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/DELETE/usr1/77/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_078":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/3/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_9
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/DELETE/usr2/77/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_079":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/3/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_9
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/GET/usr2/77/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_080":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/3/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_9
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/DELETE/usr1/77/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_081":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/3/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_9
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/POST/usr1/77/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_082":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_10
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/GET/usr1/3/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_083":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_10
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/GET/usr2/3/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_084":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_10
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/POST/usr1/3/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_085":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_10
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/POST/usr2/3/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_086":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_10
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/DELETE/usr1/3/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_087":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_10
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/DELETE/usr2/3/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_088":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_10
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/GET/usr2/3/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_089":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_10
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/DELETE/usr1/3/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_090":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/2/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_10
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/POST/usr1/3/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_091":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_11
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/GET/usr1/1/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_092":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_11
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/GET/usr2/1/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_093":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_11
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/POST/usr1/1/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_094":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_11
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/POST/usr2/1/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_095":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_11
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/DELETE/usr1/1/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_096":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_11
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/DELETE/usr2/1/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_097":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_11
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/GET/usr2/1/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_098":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_11
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/DELETE/usr1/1/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_099":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/A
            # method = POST
            # header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_11
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/POST/usr1/1/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_100":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_12
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr1/4/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_101":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_12
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_102":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_12
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_103":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_12
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr2/4/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_104":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_12
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_105":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_12
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr2/4/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_106":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_12
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_107":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_12
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_108":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/C
            # method = GET
            # header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_12
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_109":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_13
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr1/4/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_110":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_13
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_111":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_13
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_112":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_13
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr2/4/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_113":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_13
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_114":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_13
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr2/4/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_115":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_13
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_116":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_13
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_117":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_13
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_118":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_14
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/GET/usr1/3/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_119":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_14
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/GET/usr2/3/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_120":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_14
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/POST/usr1/3/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_121":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_14
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/POST/usr2/3/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_122":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_14
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/DELETE/usr1/3/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_123":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_14
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/DELETE/usr2/3/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_124":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_14
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/GET/usr2/3/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_125":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_14
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/DELETE/usr1/3/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_126":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/1/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_14
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/POST/usr1/3/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_127":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_15
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/GET/usr1/52/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_128":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_15
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/GET/usr2/52/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_129":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_15
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/POST/usr1/52/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_130":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_15
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/POST/usr2/52/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_131":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_15
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/DELETE/usr1/52/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_132":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_15
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/DELETE/usr2/52/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_133":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_15
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/GET/usr2/52/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_134":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_15
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/DELETE/usr1/52/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_135":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            # body = ./body_files/request_1_body_15
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://52/POST/usr1/52/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_136":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_16
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/GET/usr1/77/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_137":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_16
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/GET/usr2/77/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_138":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_16
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/POST/usr1/77/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_139":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_16
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/POST/usr2/77/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_140":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_16
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/DELETE/usr1/77/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_141":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_16
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/DELETE/usr2/77/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_142":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_16
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/GET/usr2/77/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_143":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_16
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/DELETE/usr1/77/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_144":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_16
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/POST/usr1/77/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_145":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_17
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr1/4/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_146":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_17
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_147":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_17
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_148":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_17
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr2/4/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_149":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_17
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_150":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_17
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr2/4/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_151":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_17
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_152":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_17
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_153":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/DEF/3/C
            # method = POST
            # header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_17
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_154":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_18
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/GET/usr1/1/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_155":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_18
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/GET/usr2/1/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_156":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_18
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/POST/usr1/1/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_157":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_18
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/POST/usr2/1/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_158":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_18
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/DELETE/usr1/1/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_159":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_18
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/DELETE/usr2/1/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_160":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_18
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/GET/usr2/1/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_161":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_18
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/DELETE/usr1/1/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_162":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/G/2/C
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_18
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/POST/usr1/1/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_163":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_19
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr1/4/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_164":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_19
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_165":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_19
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_166":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_19
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr2/4/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_167":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_19
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_168":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_19
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr2/4/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_169":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_19
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/GET/usr2/4/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_170":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_19
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/DELETE/usr1/4/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_171":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            # body = ./body_files/request_1_body_19
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://4/POST/usr1/4/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_172":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_20
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/GET/usr1/3/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_173":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_20
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/GET/usr2/3/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_174":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_20
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/POST/usr1/3/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_175":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_20
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/POST/usr2/3/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_176":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_20
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/DELETE/usr1/3/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_177":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_20
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/DELETE/usr2/3/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_178":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_20
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/GET/usr2/3/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_179":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_20
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/DELETE/usr1/3/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_180":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/1/B
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            # body = ./body_files/request_1_body_20
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://3/POST/usr1/3/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_181":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_21
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/GET/usr1/1/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_182":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_21
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/GET/usr2/1/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_183":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_21
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/POST/usr1/1/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_184":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_21
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/POST/usr2/1/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_185":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_21
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/DELETE/usr1/1/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_186":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_21
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/DELETE/usr2/1/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_187":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_21
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/GET/usr2/1/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_188":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_21
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/DELETE/usr1/1/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_189":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/3/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            # body = ./body_files/request_1_body_21
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://1/POST/usr1/1/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_190":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_22
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/GET/usr1/77/a
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_191":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_22
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/GET/usr2/77/b
            # method = POST
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_192":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_22
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/POST/usr1/77/b
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_193":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_22
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/POST/usr2/77/a
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_194":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_22
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/DELETE/usr1/77/c
            # method = POST
            # header = {"Content-Type": "application/json"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_195":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_22
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/DELETE/usr2/77/a
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_196":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_22
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/GET/usr2/77/c
            # method = GET
            # header = {"Content-Type": "application/json", "Test": "test"}
            # body = body1.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_197":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_22
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/DELETE/usr1/77/b
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_198":
        if request_id == "call_1":
            # Test Case Information
            # endpoint = https://mydomain/addUser/ABC/2/A
            # method = GET
            # header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            # body = ./body_files/request_1_body_22
            assert response.status_code == 200
        elif request_id == "call_2":
            # Test Case Information
            # endpoint = https://77/POST/usr1/77/c
            # method = GET
            # header = {"Content-Type": "application/json"}
            # body = body2.json
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

def all_test_cases(test_case, request_id):
    """
    List of all test cases in this test suite
    """
    if test_case == "test_case_001":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "https://4/GET/usr1/4/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_002":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_003":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_004":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "https://4/POST/usr2/4/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_005":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_006":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr2/4/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_007":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_008":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_009":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_1"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_010":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/B"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            body = "./body_files/request_1_body_2"
        elif request_id == "call_2":
            url = "https://52/GET/usr1/52/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_011":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/B"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            body = "./body_files/request_1_body_2"
        elif request_id == "call_2":
            url = "https://52/GET/usr2/52/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_012":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/B"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            body = "./body_files/request_1_body_2"
        elif request_id == "call_2":
            url = "https://52/POST/usr1/52/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_013":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/B"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            body = "./body_files/request_1_body_2"
        elif request_id == "call_2":
            url = "https://52/POST/usr2/52/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_014":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/B"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            body = "./body_files/request_1_body_2"
        elif request_id == "call_2":
            url = "https://52/DELETE/usr1/52/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_015":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/B"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            body = "./body_files/request_1_body_2"
        elif request_id == "call_2":
            url = "https://52/DELETE/usr2/52/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_016":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/B"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            body = "./body_files/request_1_body_2"
        elif request_id == "call_2":
            url = "https://52/GET/usr2/52/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_017":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/B"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            body = "./body_files/request_1_body_2"
        elif request_id == "call_2":
            url = "https://52/DELETE/usr1/52/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_018":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/B"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "52"}
            body = "./body_files/request_1_body_2"
        elif request_id == "call_2":
            url = "https://52/POST/usr1/52/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_019":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            body = "./body_files/request_1_body_3"
        elif request_id == "call_2":
            url = "https://3/GET/usr1/3/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_020":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            body = "./body_files/request_1_body_3"
        elif request_id == "call_2":
            url = "https://3/GET/usr2/3/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_021":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            body = "./body_files/request_1_body_3"
        elif request_id == "call_2":
            url = "https://3/POST/usr1/3/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_022":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            body = "./body_files/request_1_body_3"
        elif request_id == "call_2":
            url = "https://3/POST/usr2/3/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_023":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            body = "./body_files/request_1_body_3"
        elif request_id == "call_2":
            url = "https://3/DELETE/usr1/3/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_024":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            body = "./body_files/request_1_body_3"
        elif request_id == "call_2":
            url = "https://3/DELETE/usr2/3/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_025":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            body = "./body_files/request_1_body_3"
        elif request_id == "call_2":
            url = "https://3/GET/usr2/3/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_026":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            body = "./body_files/request_1_body_3"
        elif request_id == "call_2":
            url = "https://3/DELETE/usr1/3/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_027":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "3"}
            body = "./body_files/request_1_body_3"
        elif request_id == "call_2":
            url = "https://3/POST/usr1/3/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_028":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            body = "./body_files/request_1_body_4"
        elif request_id == "call_2":
            url = "https://1/GET/usr1/1/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_029":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            body = "./body_files/request_1_body_4"
        elif request_id == "call_2":
            url = "https://1/GET/usr2/1/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_030":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            body = "./body_files/request_1_body_4"
        elif request_id == "call_2":
            url = "https://1/POST/usr1/1/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_031":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            body = "./body_files/request_1_body_4"
        elif request_id == "call_2":
            url = "https://1/POST/usr2/1/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_032":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            body = "./body_files/request_1_body_4"
        elif request_id == "call_2":
            url = "https://1/DELETE/usr1/1/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_033":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            body = "./body_files/request_1_body_4"
        elif request_id == "call_2":
            url = "https://1/DELETE/usr2/1/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_034":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            body = "./body_files/request_1_body_4"
        elif request_id == "call_2":
            url = "https://1/GET/usr2/1/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_035":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            body = "./body_files/request_1_body_4"
        elif request_id == "call_2":
            url = "https://1/DELETE/usr1/1/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_036":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "1"}
            body = "./body_files/request_1_body_4"
        elif request_id == "call_2":
            url = "https://1/POST/usr1/1/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_037":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/A"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_5"
        elif request_id == "call_2":
            url = "https://4/GET/usr1/4/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_038":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/A"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_5"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_039":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/A"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_5"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_040":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/A"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_5"
        elif request_id == "call_2":
            url = "https://4/POST/usr2/4/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_041":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/A"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_5"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_042":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/A"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_5"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr2/4/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_043":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/A"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_5"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_044":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/A"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_5"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_045":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/A"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_5"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_046":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_6"
        elif request_id == "call_2":
            url = "https://77/GET/usr1/77/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_047":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_6"
        elif request_id == "call_2":
            url = "https://77/GET/usr2/77/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_048":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_6"
        elif request_id == "call_2":
            url = "https://77/POST/usr1/77/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_049":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_6"
        elif request_id == "call_2":
            url = "https://77/POST/usr2/77/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_050":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_6"
        elif request_id == "call_2":
            url = "https://77/DELETE/usr1/77/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_051":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_6"
        elif request_id == "call_2":
            url = "https://77/DELETE/usr2/77/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_052":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_6"
        elif request_id == "call_2":
            url = "https://77/GET/usr2/77/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_053":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_6"
        elif request_id == "call_2":
            url = "https://77/DELETE/usr1/77/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_054":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_6"
        elif request_id == "call_2":
            url = "https://77/POST/usr1/77/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_055":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            body = "./body_files/request_1_body_7"
        elif request_id == "call_2":
            url = "https://52/GET/usr1/52/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_056":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            body = "./body_files/request_1_body_7"
        elif request_id == "call_2":
            url = "https://52/GET/usr2/52/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_057":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            body = "./body_files/request_1_body_7"
        elif request_id == "call_2":
            url = "https://52/POST/usr1/52/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_058":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            body = "./body_files/request_1_body_7"
        elif request_id == "call_2":
            url = "https://52/POST/usr2/52/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_059":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            body = "./body_files/request_1_body_7"
        elif request_id == "call_2":
            url = "https://52/DELETE/usr1/52/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_060":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            body = "./body_files/request_1_body_7"
        elif request_id == "call_2":
            url = "https://52/DELETE/usr2/52/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_061":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            body = "./body_files/request_1_body_7"
        elif request_id == "call_2":
            url = "https://52/GET/usr2/52/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_062":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            body = "./body_files/request_1_body_7"
        elif request_id == "call_2":
            url = "https://52/DELETE/usr1/52/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_063":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "52"}
            body = "./body_files/request_1_body_7"
        elif request_id == "call_2":
            url = "https://52/POST/usr1/52/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_064":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/A"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_8"
        elif request_id == "call_2":
            url = "https://4/GET/usr1/4/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_065":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/A"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_8"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_066":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/A"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_8"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_067":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/A"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_8"
        elif request_id == "call_2":
            url = "https://4/POST/usr2/4/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_068":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/A"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_8"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_069":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/A"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_8"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr2/4/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_070":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/A"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_8"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_071":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/A"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_8"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_072":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/A"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_8"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_073":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/3/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            body = "./body_files/request_1_body_9"
        elif request_id == "call_2":
            url = "https://77/GET/usr1/77/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_074":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/3/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            body = "./body_files/request_1_body_9"
        elif request_id == "call_2":
            url = "https://77/GET/usr2/77/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_075":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/3/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            body = "./body_files/request_1_body_9"
        elif request_id == "call_2":
            url = "https://77/POST/usr1/77/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_076":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/3/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            body = "./body_files/request_1_body_9"
        elif request_id == "call_2":
            url = "https://77/POST/usr2/77/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_077":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/3/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            body = "./body_files/request_1_body_9"
        elif request_id == "call_2":
            url = "https://77/DELETE/usr1/77/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_078":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/3/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            body = "./body_files/request_1_body_9"
        elif request_id == "call_2":
            url = "https://77/DELETE/usr2/77/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_079":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/3/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            body = "./body_files/request_1_body_9"
        elif request_id == "call_2":
            url = "https://77/GET/usr2/77/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_080":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/3/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            body = "./body_files/request_1_body_9"
        elif request_id == "call_2":
            url = "https://77/DELETE/usr1/77/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_081":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/3/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "77"}
            body = "./body_files/request_1_body_9"
        elif request_id == "call_2":
            url = "https://77/POST/usr1/77/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_082":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_10"
        elif request_id == "call_2":
            url = "https://3/GET/usr1/3/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_083":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_10"
        elif request_id == "call_2":
            url = "https://3/GET/usr2/3/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_084":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_10"
        elif request_id == "call_2":
            url = "https://3/POST/usr1/3/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_085":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_10"
        elif request_id == "call_2":
            url = "https://3/POST/usr2/3/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_086":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_10"
        elif request_id == "call_2":
            url = "https://3/DELETE/usr1/3/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_087":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_10"
        elif request_id == "call_2":
            url = "https://3/DELETE/usr2/3/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_088":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_10"
        elif request_id == "call_2":
            url = "https://3/GET/usr2/3/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_089":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_10"
        elif request_id == "call_2":
            url = "https://3/DELETE/usr1/3/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_090":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/2/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_10"
        elif request_id == "call_2":
            url = "https://3/POST/usr1/3/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_091":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            body = "./body_files/request_1_body_11"
        elif request_id == "call_2":
            url = "https://1/GET/usr1/1/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_092":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            body = "./body_files/request_1_body_11"
        elif request_id == "call_2":
            url = "https://1/GET/usr2/1/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_093":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            body = "./body_files/request_1_body_11"
        elif request_id == "call_2":
            url = "https://1/POST/usr1/1/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_094":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            body = "./body_files/request_1_body_11"
        elif request_id == "call_2":
            url = "https://1/POST/usr2/1/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_095":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            body = "./body_files/request_1_body_11"
        elif request_id == "call_2":
            url = "https://1/DELETE/usr1/1/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_096":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            body = "./body_files/request_1_body_11"
        elif request_id == "call_2":
            url = "https://1/DELETE/usr2/1/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_097":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            body = "./body_files/request_1_body_11"
        elif request_id == "call_2":
            url = "https://1/GET/usr2/1/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_098":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            body = "./body_files/request_1_body_11"
        elif request_id == "call_2":
            url = "https://1/DELETE/usr1/1/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_099":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/A"
            method = "POST"
            header = {"Content-type": "yaml", "testInt": "3", "dalsiTest": "1"}
            body = "./body_files/request_1_body_11"
        elif request_id == "call_2":
            url = "https://1/POST/usr1/1/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_100":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_12"
        elif request_id == "call_2":
            url = "https://4/GET/usr1/4/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_101":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_12"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_102":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_12"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_103":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_12"
        elif request_id == "call_2":
            url = "https://4/POST/usr2/4/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_104":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_12"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_105":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_12"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr2/4/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_106":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_12"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_107":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_12"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_108":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/C"
            method = "GET"
            header = {"Content-type": "yaml", "testInt": "2", "dalsiTest": "4"}
            body = "./body_files/request_1_body_12"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_109":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_13"
        elif request_id == "call_2":
            url = "https://4/GET/usr1/4/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_110":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_13"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_111":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_13"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_112":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_13"
        elif request_id == "call_2":
            url = "https://4/POST/usr2/4/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_113":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_13"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_114":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_13"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr2/4/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_115":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_13"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_116":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_13"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_117":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_13"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_118":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            body = "./body_files/request_1_body_14"
        elif request_id == "call_2":
            url = "https://3/GET/usr1/3/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_119":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            body = "./body_files/request_1_body_14"
        elif request_id == "call_2":
            url = "https://3/GET/usr2/3/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_120":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            body = "./body_files/request_1_body_14"
        elif request_id == "call_2":
            url = "https://3/POST/usr1/3/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_121":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            body = "./body_files/request_1_body_14"
        elif request_id == "call_2":
            url = "https://3/POST/usr2/3/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_122":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            body = "./body_files/request_1_body_14"
        elif request_id == "call_2":
            url = "https://3/DELETE/usr1/3/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_123":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            body = "./body_files/request_1_body_14"
        elif request_id == "call_2":
            url = "https://3/DELETE/usr2/3/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_124":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            body = "./body_files/request_1_body_14"
        elif request_id == "call_2":
            url = "https://3/GET/usr2/3/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_125":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            body = "./body_files/request_1_body_14"
        elif request_id == "call_2":
            url = "https://3/DELETE/usr1/3/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_126":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/1/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "3"}
            body = "./body_files/request_1_body_14"
        elif request_id == "call_2":
            url = "https://3/POST/usr1/3/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_127":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            body = "./body_files/request_1_body_15"
        elif request_id == "call_2":
            url = "https://52/GET/usr1/52/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_128":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            body = "./body_files/request_1_body_15"
        elif request_id == "call_2":
            url = "https://52/GET/usr2/52/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_129":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            body = "./body_files/request_1_body_15"
        elif request_id == "call_2":
            url = "https://52/POST/usr1/52/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_130":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            body = "./body_files/request_1_body_15"
        elif request_id == "call_2":
            url = "https://52/POST/usr2/52/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_131":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            body = "./body_files/request_1_body_15"
        elif request_id == "call_2":
            url = "https://52/DELETE/usr1/52/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_132":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            body = "./body_files/request_1_body_15"
        elif request_id == "call_2":
            url = "https://52/DELETE/usr2/52/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_133":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            body = "./body_files/request_1_body_15"
        elif request_id == "call_2":
            url = "https://52/GET/usr2/52/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_134":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            body = "./body_files/request_1_body_15"
        elif request_id == "call_2":
            url = "https://52/DELETE/usr1/52/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_135":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "52"}
            body = "./body_files/request_1_body_15"
        elif request_id == "call_2":
            url = "https://52/POST/usr1/52/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_136":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            body = "./body_files/request_1_body_16"
        elif request_id == "call_2":
            url = "https://77/GET/usr1/77/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_137":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            body = "./body_files/request_1_body_16"
        elif request_id == "call_2":
            url = "https://77/GET/usr2/77/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_138":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            body = "./body_files/request_1_body_16"
        elif request_id == "call_2":
            url = "https://77/POST/usr1/77/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_139":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            body = "./body_files/request_1_body_16"
        elif request_id == "call_2":
            url = "https://77/POST/usr2/77/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_140":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            body = "./body_files/request_1_body_16"
        elif request_id == "call_2":
            url = "https://77/DELETE/usr1/77/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_141":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            body = "./body_files/request_1_body_16"
        elif request_id == "call_2":
            url = "https://77/DELETE/usr2/77/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_142":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            body = "./body_files/request_1_body_16"
        elif request_id == "call_2":
            url = "https://77/GET/usr2/77/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_143":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            body = "./body_files/request_1_body_16"
        elif request_id == "call_2":
            url = "https://77/DELETE/usr1/77/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_144":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "2", "dalsiTest": "77"}
            body = "./body_files/request_1_body_16"
        elif request_id == "call_2":
            url = "https://77/POST/usr1/77/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_145":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_17"
        elif request_id == "call_2":
            url = "https://4/GET/usr1/4/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_146":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_17"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_147":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_17"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_148":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_17"
        elif request_id == "call_2":
            url = "https://4/POST/usr2/4/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_149":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_17"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_150":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_17"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr2/4/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_151":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_17"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_152":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_17"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_153":
        if request_id == "call_1":
            url = "https://mydomain/addUser/DEF/3/C"
            method = "POST"
            header = {"Content-type": "json", "testInt": "3", "dalsiTest": "4"}
            body = "./body_files/request_1_body_17"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_154":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_18"
        elif request_id == "call_2":
            url = "https://1/GET/usr1/1/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_155":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_18"
        elif request_id == "call_2":
            url = "https://1/GET/usr2/1/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_156":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_18"
        elif request_id == "call_2":
            url = "https://1/POST/usr1/1/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_157":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_18"
        elif request_id == "call_2":
            url = "https://1/POST/usr2/1/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_158":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_18"
        elif request_id == "call_2":
            url = "https://1/DELETE/usr1/1/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_159":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_18"
        elif request_id == "call_2":
            url = "https://1/DELETE/usr2/1/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_160":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_18"
        elif request_id == "call_2":
            url = "https://1/GET/usr2/1/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_161":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_18"
        elif request_id == "call_2":
            url = "https://1/DELETE/usr1/1/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_162":
        if request_id == "call_1":
            url = "https://mydomain/addUser/G/2/C"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_18"
        elif request_id == "call_2":
            url = "https://1/POST/usr1/1/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_163":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_19"
        elif request_id == "call_2":
            url = "https://4/GET/usr1/4/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_164":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_19"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_165":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_19"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_166":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_19"
        elif request_id == "call_2":
            url = "https://4/POST/usr2/4/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_167":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_19"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_168":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_19"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr2/4/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_169":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_19"
        elif request_id == "call_2":
            url = "https://4/GET/usr2/4/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_170":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_19"
        elif request_id == "call_2":
            url = "https://4/DELETE/usr1/4/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_171":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "4"}
            body = "./body_files/request_1_body_19"
        elif request_id == "call_2":
            url = "https://4/POST/usr1/4/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_172":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_20"
        elif request_id == "call_2":
            url = "https://3/GET/usr1/3/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_173":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_20"
        elif request_id == "call_2":
            url = "https://3/GET/usr2/3/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_174":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_20"
        elif request_id == "call_2":
            url = "https://3/POST/usr1/3/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_175":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_20"
        elif request_id == "call_2":
            url = "https://3/POST/usr2/3/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_176":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_20"
        elif request_id == "call_2":
            url = "https://3/DELETE/usr1/3/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_177":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_20"
        elif request_id == "call_2":
            url = "https://3/DELETE/usr2/3/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_178":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_20"
        elif request_id == "call_2":
            url = "https://3/GET/usr2/3/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_179":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_20"
        elif request_id == "call_2":
            url = "https://3/DELETE/usr1/3/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_180":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/1/B"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "3"}
            body = "./body_files/request_1_body_20"
        elif request_id == "call_2":
            url = "https://3/POST/usr1/3/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_181":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_21"
        elif request_id == "call_2":
            url = "https://1/GET/usr1/1/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_182":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_21"
        elif request_id == "call_2":
            url = "https://1/GET/usr2/1/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_183":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_21"
        elif request_id == "call_2":
            url = "https://1/POST/usr1/1/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_184":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_21"
        elif request_id == "call_2":
            url = "https://1/POST/usr2/1/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_185":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_21"
        elif request_id == "call_2":
            url = "https://1/DELETE/usr1/1/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_186":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_21"
        elif request_id == "call_2":
            url = "https://1/DELETE/usr2/1/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_187":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_21"
        elif request_id == "call_2":
            url = "https://1/GET/usr2/1/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_188":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_21"
        elif request_id == "call_2":
            url = "https://1/DELETE/usr1/1/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_189":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/3/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "1"}
            body = "./body_files/request_1_body_21"
        elif request_id == "call_2":
            url = "https://1/POST/usr1/1/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_190":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_22"
        elif request_id == "call_2":
            url = "https://77/GET/usr1/77/a"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_191":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_22"
        elif request_id == "call_2":
            url = "https://77/GET/usr2/77/b"
            method = "POST"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_192":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_22"
        elif request_id == "call_2":
            url = "https://77/POST/usr1/77/b"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_193":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_22"
        elif request_id == "call_2":
            url = "https://77/POST/usr2/77/a"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_194":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_22"
        elif request_id == "call_2":
            url = "https://77/DELETE/usr1/77/c"
            method = "POST"
            header = {"Content-Type": "application/json"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_195":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_22"
        elif request_id == "call_2":
            url = "https://77/DELETE/usr2/77/a"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_196":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_22"
        elif request_id == "call_2":
            url = "https://77/GET/usr2/77/c"
            method = "GET"
            header = {"Content-Type": "application/json", "Test": "test"}
            body = "body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_197":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_22"
        elif request_id == "call_2":
            url = "https://77/DELETE/usr1/77/b"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_198":
        if request_id == "call_1":
            url = "https://mydomain/addUser/ABC/2/A"
            method = "GET"
            header = {"Content-type": "json", "testInt": "1", "dalsiTest": "77"}
            body = "./body_files/request_1_body_22"
        elif request_id == "call_2":
            url = "https://77/POST/usr1/77/c"
            method = "GET"
            header = {"Content-Type": "application/json"}
            body = "body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    else:
        raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))

    return (url, method, header, body)

class TestClass(TestCase): 
    def test_sequence_001(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_001", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_001", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_001", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_001", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_002(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_002", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_002", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_002", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_002", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_003(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_003", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_003", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_003", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_003", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_004(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_004", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_004", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_004", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_004", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_005(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_005", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_005", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_005", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_005", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_006(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_006", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_006", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_006", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_006", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_007(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_007", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_007", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_007", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_007", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_008(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_008", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_008", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_008", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_008", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_009(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_009", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_009", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_009", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_009", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_010(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_010", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_010", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_010", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_010", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_011(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_011", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_011", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_011", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_011", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_012(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_012", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_012", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_012", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_012", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_013(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_013", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_013", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_013", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_013", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_014(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_014", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_014", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_014", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_014", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_015(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_015", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_015", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_015", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_015", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_016(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_016", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_016", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_016", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_016", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_017(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_017", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_017", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_017", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_017", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_018(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_018", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_018", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_018", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_018", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_019(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_019", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_019", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_019", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_019", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_020(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_020", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_020", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_020", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_020", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_021(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_021", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_021", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_021", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_021", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_022(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_022", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_022", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_022", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_022", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_023(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_023", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_023", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_023", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_023", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_024(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_024", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_024", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_024", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_024", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_025(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_025", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_025", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_025", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_025", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_026(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_026", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_026", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_026", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_026", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_027(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_027", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_027", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_027", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_027", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_028(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_028", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_028", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_028", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_028", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_029(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_029", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_029", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_029", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_029", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_030(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_030", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_030", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_030", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_030", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_031(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_031", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_031", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_031", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_031", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_032(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_032", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_032", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_032", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_032", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_033(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_033", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_033", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_033", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_033", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_034(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_034", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_034", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_034", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_034", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_035(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_035", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_035", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_035", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_035", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_036(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_036", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_036", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_036", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_036", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_037(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_037", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_037", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_037", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_037", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_038(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_038", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_038", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_038", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_038", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_039(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_039", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_039", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_039", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_039", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_040(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_040", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_040", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_040", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_040", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_041(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_041", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_041", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_041", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_041", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_042(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_042", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_042", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_042", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_042", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_043(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_043", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_043", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_043", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_043", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_044(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_044", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_044", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_044", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_044", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_045(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_045", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_045", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_045", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_045", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_046(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_046", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_046", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_046", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_046", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_047(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_047", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_047", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_047", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_047", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_048(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_048", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_048", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_048", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_048", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_049(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_049", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_049", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_049", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_049", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_050(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_050", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_050", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_050", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_050", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_051(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_051", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_051", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_051", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_051", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_052(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_052", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_052", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_052", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_052", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_053(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_053", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_053", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_053", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_053", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_054(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_054", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_054", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_054", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_054", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_055(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_055", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_055", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_055", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_055", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_056(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_056", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_056", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_056", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_056", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_057(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_057", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_057", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_057", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_057", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_058(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_058", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_058", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_058", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_058", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_059(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_059", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_059", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_059", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_059", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_060(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_060", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_060", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_060", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_060", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_061(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_061", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_061", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_061", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_061", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_062(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_062", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_062", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_062", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_062", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_063(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_063", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_063", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_063", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_063", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_064(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_064", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_064", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_064", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_064", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_065(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_065", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_065", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_065", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_065", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_066(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_066", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_066", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_066", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_066", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_067(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_067", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_067", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_067", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_067", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_068(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_068", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_068", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_068", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_068", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_069(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_069", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_069", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_069", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_069", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_070(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_070", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_070", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_070", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_070", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_071(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_071", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_071", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_071", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_071", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_072(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_072", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_072", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_072", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_072", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_073(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_073", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_073", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_073", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_073", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_074(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_074", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_074", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_074", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_074", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_075(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_075", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_075", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_075", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_075", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_076(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_076", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_076", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_076", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_076", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_077(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_077", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_077", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_077", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_077", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_078(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_078", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_078", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_078", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_078", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_079(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_079", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_079", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_079", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_079", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_080(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_080", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_080", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_080", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_080", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_081(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_081", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_081", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_081", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_081", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_082(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_082", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_082", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_082", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_082", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_083(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_083", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_083", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_083", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_083", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_084(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_084", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_084", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_084", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_084", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_085(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_085", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_085", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_085", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_085", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_086(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_086", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_086", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_086", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_086", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_087(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_087", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_087", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_087", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_087", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_088(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_088", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_088", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_088", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_088", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_089(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_089", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_089", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_089", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_089", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_090(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_090", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_090", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_090", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_090", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_091(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_091", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_091", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_091", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_091", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_092(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_092", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_092", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_092", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_092", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_093(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_093", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_093", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_093", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_093", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_094(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_094", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_094", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_094", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_094", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_095(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_095", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_095", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_095", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_095", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_096(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_096", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_096", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_096", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_096", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_097(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_097", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_097", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_097", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_097", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_098(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_098", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_098", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_098", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_098", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_099(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_099", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_099", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_099", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_099", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_100(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_100", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_100", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_100", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_100", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_101(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_101", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_101", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_101", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_101", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_102(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_102", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_102", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_102", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_102", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_103(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_103", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_103", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_103", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_103", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_104(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_104", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_104", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_104", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_104", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_105(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_105", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_105", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_105", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_105", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_106(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_106", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_106", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_106", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_106", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_107(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_107", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_107", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_107", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_107", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_108(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_108", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_108", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_108", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_108", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_109(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_109", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_109", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_109", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_109", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_110(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_110", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_110", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_110", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_110", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_111(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_111", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_111", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_111", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_111", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_112(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_112", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_112", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_112", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_112", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_113(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_113", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_113", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_113", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_113", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_114(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_114", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_114", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_114", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_114", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_115(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_115", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_115", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_115", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_115", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_116(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_116", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_116", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_116", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_116", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_117(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_117", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_117", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_117", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_117", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_118(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_118", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_118", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_118", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_118", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_119(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_119", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_119", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_119", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_119", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_120(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_120", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_120", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_120", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_120", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_121(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_121", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_121", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_121", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_121", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_122(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_122", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_122", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_122", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_122", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_123(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_123", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_123", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_123", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_123", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_124(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_124", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_124", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_124", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_124", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_125(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_125", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_125", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_125", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_125", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_126(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_126", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_126", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_126", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_126", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_127(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_127", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_127", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_127", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_127", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_128(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_128", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_128", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_128", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_128", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_129(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_129", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_129", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_129", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_129", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_130(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_130", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_130", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_130", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_130", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_131(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_131", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_131", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_131", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_131", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_132(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_132", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_132", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_132", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_132", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_133(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_133", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_133", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_133", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_133", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_134(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_134", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_134", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_134", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_134", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_135(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_135", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_135", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_135", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_135", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_136(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_136", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_136", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_136", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_136", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_137(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_137", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_137", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_137", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_137", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_138(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_138", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_138", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_138", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_138", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_139(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_139", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_139", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_139", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_139", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_140(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_140", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_140", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_140", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_140", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_141(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_141", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_141", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_141", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_141", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_142(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_142", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_142", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_142", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_142", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_143(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_143", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_143", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_143", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_143", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_144(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_144", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_144", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_144", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_144", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_145(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_145", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_145", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_145", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_145", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_146(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_146", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_146", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_146", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_146", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_147(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_147", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_147", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_147", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_147", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_148(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_148", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_148", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_148", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_148", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_149(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_149", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_149", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_149", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_149", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_150(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_150", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_150", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_150", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_150", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_151(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_151", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_151", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_151", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_151", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_152(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_152", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_152", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_152", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_152", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_153(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_153", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_153", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_153", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_153", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_154(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_154", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_154", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_154", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_154", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_155(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_155", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_155", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_155", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_155", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_156(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_156", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_156", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_156", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_156", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_157(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_157", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_157", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_157", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_157", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_158(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_158", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_158", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_158", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_158", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_159(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_159", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_159", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_159", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_159", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_160(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_160", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_160", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_160", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_160", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_161(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_161", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_161", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_161", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_161", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_162(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_162", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_162", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_162", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_162", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_163(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_163", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_163", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_163", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_163", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_164(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_164", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_164", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_164", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_164", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_165(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_165", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_165", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_165", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_165", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_166(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_166", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_166", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_166", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_166", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_167(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_167", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_167", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_167", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_167", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_168(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_168", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_168", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_168", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_168", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_169(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_169", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_169", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_169", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_169", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_170(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_170", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_170", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_170", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_170", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_171(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_171", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_171", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_171", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_171", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_172(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_172", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_172", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_172", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_172", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_173(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_173", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_173", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_173", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_173", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_174(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_174", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_174", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_174", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_174", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_175(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_175", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_175", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_175", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_175", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_176(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_176", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_176", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_176", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_176", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_177(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_177", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_177", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_177", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_177", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_178(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_178", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_178", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_178", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_178", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_179(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_179", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_179", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_179", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_179", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_180(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_180", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_180", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_180", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_180", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_181(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_181", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_181", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_181", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_181", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_182(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_182", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_182", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_182", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_182", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_183(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_183", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_183", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_183", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_183", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_184(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_184", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_184", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_184", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_184", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_185(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_185", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_185", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_185", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_185", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_186(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_186", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_186", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_186", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_186", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_187(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_187", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_187", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_187", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_187", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_188(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_188", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_188", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_188", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_188", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_189(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_189", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_189", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_189", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_189", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_190(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_190", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_190", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_190", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_190", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_191(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_191", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_191", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_191", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_191", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_192(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_192", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_192", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_192", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_192", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_193(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_193", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_193", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_193", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_193", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_194(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_194", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_194", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_194", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_194", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_195(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_195", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_195", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_195", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_195", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_196(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_196", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_196", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_196", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_196", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_197(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_197", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_197", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_197", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_197", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_198(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = all_test_cases("test_case_198", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_198", "call_1", response, call)
        ### 2. Request ###
        call = all_test_cases("test_case_198", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_198", "call_2", response, call)
        ### SUT Teardown ###
        teardown()

