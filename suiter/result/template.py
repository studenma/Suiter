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
    if test_case == "test_case_001":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_002":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_003":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_004":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_005":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_006":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_007":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_008":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_009":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_010":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_011":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_012":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_013":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_014":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_015":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_016":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_017":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_018":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_019":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_020":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_021":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_022":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_023":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_024":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_025":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_026":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_027":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_028":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_029":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_030":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_031":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_032":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_033":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_034":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_035":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_036":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_037":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_038":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_039":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_040":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_041":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_042":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_043":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_044":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_045":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_046":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_047":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_048":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_049":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_050":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_051":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_052":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_053":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_054":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_055":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_056":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_057":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_058":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_059":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_060":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_061":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_062":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_063":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_064":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_065":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_066":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_067":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_068":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_069":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_070":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_071":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_072":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_073":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_074":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_075":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_076":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_077":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_078":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_079":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_080":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_081":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_082":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_083":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_084":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_085":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_086":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_087":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_088":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_089":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_090":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_091":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_092":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_093":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_094":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_095":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_096":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_097":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_098":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_099":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
            assert response.status_code == 200
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_100":
        if request_id == "call_1":
            assert response.status_code == 200
        elif request_id == "call_2":
            assert response.status_code == 200
        elif request_id == "call_3":
            assert response.status_code == 200
        elif request_id == "call_4":
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
    if test_case == "test_case_001":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_002":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_003":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_004":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_005":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_006":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_007":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_008":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_009":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_010":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_011":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_012":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_013":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_014":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_015":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_016":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_017":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_018":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_019":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_020":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_021":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_022":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_023":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_024":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_025":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_026":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_027":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_028":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_029":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_030":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_031":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_032":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_033":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_034":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_035":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_036":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_037":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_038":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_039":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_040":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_041":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_042":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_043":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_044":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_045":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_046":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_047":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_048":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_049":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_050":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_051":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_052":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_053":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_054":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_055":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_056":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_057":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_058":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_059":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_060":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_061":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_062":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_063":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_064":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_065":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_066":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_067":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_068":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_069":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_070":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_071":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_072":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_073":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_074":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_075":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_076":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_077":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_078":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_079":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_080":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_081":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_082":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_083":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_084":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_085":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_086":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_087":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_088":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_089":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_090":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_091":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_092":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_093":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_094":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_095":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_096":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_097":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body2.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_098":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body3.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_099":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        else:
            raise Exception("Should have never gotten here: [{},{}]".format(test_case,request_id))
    elif test_case == "test_case_100":
        if request_id == "call_1":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_2":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_3":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
        elif request_id == "call_4":
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide"
            method = "GET"
            header = {'Content-Type': 'application/json', 'Test': 'TestValue'}
            body = "../input/body1.json"
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
        call = list_of_all_cases("test_case_001", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_001", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_001", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_001", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_001", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_001", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_001", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_001", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_002(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_002", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_002", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_002", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_002", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_002", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_002", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_002", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_002", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_003(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_003", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_003", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_003", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_003", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_003", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_003", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_003", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_003", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_004(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_004", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_004", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_004", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_004", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_004", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_004", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_004", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_004", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_005(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_005", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_005", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_005", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_005", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_005", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_005", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_005", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_005", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_006(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_006", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_006", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_006", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_006", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_006", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_006", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_006", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_006", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_007(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_007", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_007", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_007", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_007", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_007", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_007", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_007", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_007", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_008(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_008", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_008", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_008", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_008", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_008", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_008", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_008", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_008", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_009(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_009", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_009", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_009", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_009", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_009", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_009", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_009", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_009", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_010(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_010", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_010", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_010", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_010", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_010", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_010", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_010", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_010", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_011(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_011", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_011", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_011", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_011", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_011", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_011", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_011", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_011", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_012(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_012", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_012", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_012", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_012", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_012", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_012", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_012", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_012", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_013(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_013", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_013", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_013", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_013", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_013", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_013", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_013", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_013", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_014(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_014", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_014", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_014", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_014", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_014", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_014", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_014", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_014", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_015(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_015", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_015", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_015", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_015", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_015", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_015", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_015", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_015", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_016(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_016", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_016", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_016", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_016", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_016", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_016", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_016", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_016", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_017(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_017", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_017", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_017", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_017", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_017", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_017", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_017", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_017", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_018(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_018", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_018", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_018", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_018", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_018", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_018", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_018", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_018", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_019(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_019", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_019", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_019", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_019", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_019", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_019", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_019", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_019", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_020(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_020", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_020", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_020", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_020", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_020", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_020", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_020", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_020", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_021(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_021", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_021", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_021", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_021", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_021", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_021", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_021", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_021", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_022(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_022", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_022", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_022", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_022", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_022", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_022", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_022", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_022", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_023(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_023", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_023", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_023", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_023", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_023", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_023", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_023", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_023", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_024(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_024", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_024", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_024", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_024", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_024", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_024", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_024", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_024", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_025(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_025", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_025", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_025", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_025", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_025", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_025", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_025", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_025", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_026(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_026", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_026", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_026", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_026", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_026", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_026", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_026", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_026", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_027(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_027", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_027", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_027", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_027", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_027", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_027", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_027", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_027", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_028(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_028", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_028", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_028", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_028", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_028", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_028", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_028", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_028", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_029(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_029", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_029", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_029", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_029", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_029", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_029", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_029", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_029", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_030(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_030", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_030", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_030", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_030", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_030", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_030", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_030", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_030", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_031(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_031", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_031", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_031", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_031", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_031", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_031", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_031", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_031", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_032(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_032", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_032", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_032", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_032", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_032", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_032", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_032", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_032", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_033(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_033", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_033", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_033", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_033", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_033", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_033", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_033", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_033", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_034(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_034", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_034", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_034", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_034", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_034", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_034", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_034", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_034", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_035(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_035", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_035", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_035", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_035", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_035", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_035", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_035", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_035", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_036(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_036", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_036", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_036", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_036", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_036", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_036", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_036", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_036", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_037(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_037", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_037", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_037", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_037", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_037", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_037", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_037", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_037", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_038(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_038", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_038", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_038", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_038", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_038", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_038", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_038", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_038", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_039(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_039", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_039", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_039", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_039", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_039", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_039", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_039", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_039", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_040(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_040", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_040", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_040", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_040", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_040", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_040", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_040", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_040", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_041(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_041", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_041", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_041", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_041", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_041", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_041", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_041", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_041", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_042(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_042", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_042", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_042", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_042", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_042", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_042", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_042", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_042", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_043(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_043", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_043", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_043", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_043", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_043", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_043", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_043", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_043", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_044(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_044", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_044", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_044", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_044", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_044", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_044", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_044", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_044", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_045(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_045", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_045", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_045", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_045", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_045", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_045", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_045", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_045", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_046(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_046", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_046", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_046", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_046", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_046", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_046", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_046", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_046", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_047(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_047", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_047", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_047", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_047", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_047", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_047", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_047", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_047", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_048(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_048", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_048", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_048", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_048", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_048", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_048", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_048", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_048", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_049(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_049", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_049", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_049", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_049", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_049", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_049", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_049", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_049", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_050(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_050", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_050", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_050", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_050", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_050", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_050", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_050", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_050", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_051(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_051", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_051", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_051", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_051", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_051", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_051", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_051", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_051", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_052(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_052", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_052", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_052", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_052", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_052", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_052", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_052", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_052", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_053(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_053", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_053", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_053", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_053", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_053", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_053", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_053", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_053", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_054(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_054", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_054", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_054", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_054", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_054", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_054", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_054", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_054", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_055(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_055", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_055", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_055", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_055", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_055", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_055", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_055", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_055", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_056(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_056", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_056", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_056", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_056", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_056", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_056", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_056", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_056", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_057(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_057", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_057", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_057", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_057", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_057", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_057", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_057", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_057", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_058(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_058", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_058", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_058", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_058", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_058", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_058", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_058", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_058", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_059(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_059", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_059", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_059", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_059", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_059", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_059", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_059", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_059", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_060(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_060", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_060", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_060", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_060", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_060", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_060", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_060", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_060", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_061(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_061", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_061", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_061", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_061", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_061", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_061", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_061", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_061", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_062(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_062", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_062", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_062", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_062", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_062", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_062", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_062", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_062", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_063(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_063", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_063", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_063", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_063", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_063", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_063", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_063", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_063", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_064(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_064", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_064", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_064", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_064", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_064", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_064", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_064", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_064", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_065(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_065", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_065", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_065", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_065", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_065", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_065", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_065", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_065", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_066(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_066", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_066", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_066", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_066", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_066", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_066", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_066", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_066", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_067(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_067", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_067", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_067", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_067", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_067", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_067", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_067", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_067", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_068(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_068", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_068", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_068", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_068", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_068", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_068", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_068", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_068", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_069(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_069", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_069", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_069", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_069", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_069", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_069", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_069", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_069", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_070(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_070", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_070", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_070", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_070", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_070", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_070", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_070", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_070", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_071(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_071", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_071", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_071", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_071", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_071", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_071", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_071", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_071", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_072(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_072", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_072", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_072", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_072", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_072", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_072", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_072", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_072", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_073(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_073", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_073", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_073", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_073", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_073", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_073", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_073", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_073", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_074(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_074", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_074", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_074", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_074", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_074", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_074", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_074", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_074", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_075(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_075", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_075", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_075", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_075", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_075", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_075", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_075", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_075", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_076(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_076", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_076", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_076", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_076", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_076", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_076", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_076", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_076", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_077(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_077", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_077", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_077", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_077", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_077", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_077", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_077", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_077", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_078(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_078", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_078", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_078", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_078", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_078", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_078", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_078", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_078", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_079(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_079", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_079", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_079", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_079", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_079", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_079", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_079", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_079", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_080(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_080", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_080", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_080", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_080", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_080", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_080", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_080", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_080", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_081(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_081", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_081", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_081", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_081", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_081", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_081", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_081", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_081", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_082(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_082", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_082", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_082", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_082", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_082", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_082", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_082", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_082", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_083(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_083", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_083", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_083", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_083", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_083", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_083", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_083", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_083", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_084(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_084", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_084", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_084", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_084", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_084", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_084", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_084", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_084", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_085(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_085", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_085", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_085", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_085", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_085", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_085", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_085", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_085", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_086(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_086", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_086", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_086", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_086", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_086", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_086", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_086", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_086", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_087(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_087", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_087", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_087", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_087", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_087", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_087", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_087", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_087", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_088(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_088", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_088", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_088", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_088", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_088", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_088", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_088", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_088", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_089(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_089", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_089", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_089", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_089", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_089", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_089", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_089", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_089", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_090(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_090", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_090", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_090", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_090", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_090", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_090", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_090", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_090", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_091(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_091", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_091", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_091", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_091", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_091", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_091", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_091", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_091", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_092(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_092", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_092", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_092", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_092", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_092", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_092", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_092", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_092", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_093(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_093", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_093", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_093", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_093", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_093", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_093", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_093", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_093", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_094(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_094", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_094", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_094", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_094", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_094", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_094", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_094", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_094", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_095(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_095", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_095", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_095", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_095", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_095", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_095", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_095", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_095", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_096(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_096", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_096", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_096", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_096", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_096", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_096", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_096", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_096", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_097(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_097", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_097", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_097", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_097", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_097", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_097", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_097", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_097", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_098(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_098", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_098", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_098", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_098", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_098", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_098", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_098", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_098", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_099(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_099", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_099", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_099", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_099", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_099", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_099", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_099", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_099", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

    def test_sequence_100(self):
        ### SUT Setup ###
        setup()
        ### 1. Request ###
        call = list_of_all_cases("test_case_100", "call_1")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_100", "call_1", response, call)
        ### 2. Request ###
        call = list_of_all_cases("test_case_100", "call_2")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_100", "call_2", response, call)
        ### 3. Request ###
        call = list_of_all_cases("test_case_100", "call_3")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_100", "call_3", response, call)
        ### 4. Request ###
        call = list_of_all_cases("test_case_100", "call_4")
        with open(call[3],'rb') as payload:
            response = requests.request(call[1], call[0], headers=call[2], data=payload)
        verify("test_case_100", "call_4", response, call)
        ### SUT Teardown ###
        teardown()

