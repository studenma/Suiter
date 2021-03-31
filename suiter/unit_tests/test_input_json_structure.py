"""
TEST SCOPE
TestClassFileCheck
    test_valid_input_json
    test_not_valid_input_json
    test_non_existing_input_json
TestClassFirstLevel
    test_not_valid_element
    test_mandatory_is_missing
    test_mandatory_is_missing_count_is_ok
TestClass_test_sequence
    test_sequence_empty_array
    test_sequence_dict
    test_sequence_calls_array
TestClass_test_endpoint
    test_endpoint_does_not_exist
    test_endpoint_is_not_dict
    test_endpoint_not_valid_element
    test_endpoint_only_mandatory
    test_missing_endpoint_mandatory
    test_missing_endpoint_optional
    test_endpoint_local_params_not_array
    test_endpoint_optional_not_int
    test_endpoint_url_not_string
TestClass_test_method
    test_method_does_not_exist
    test_method_is_not_dict
    test_method_not_valid_element
    test_method_values_not_array
    test_method_values_content_not_string
TestClass_test_header
    test_header_does_not_exist
    test_header_is_not_array
    test_header_content_not_string
TestClass_test_body
    test_body_does_not_exist
    test_body_is_not_array
    test_body_content_not_string
TestClass_test_call_optional_elements
    test_call_optional_el_not_integer
TestClass_test_global_params
    test_global_params_not_list
    test_global_params_empty_list
    test_global_params_content_not_array
    test_global_params_content_empty_array
"""

import pytest
import json

""" import suiter package """ 
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from input_parser import input_file_parser
from input_parser import is_input_json_valid
from exceptions import *

mandatory_elements_array = ["test_sequence", "global_params"]

def sequence_indexes():
    input_file_path = './test_input/valid.json'
    # open input file and check if it is a json
    try:
        with open(input_file_path) as json_file:
            input_dict = json.load(json_file)        
    except:
        raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
    resulted_array = []
    for idx in range(len(input_dict['test_sequence'])):
        resulted_array.append(idx)
    return resulted_array

class TestClassFileCheck:
    @pytest.mark.parametrize("input_file_path", ["./test_input/valid.json"])
    def test_valid_input_json(self, input_file_path):
        # open input file
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)
        except OpenFileError:
            raise pytest.fail("Could not open the file: {}".format(input_file_path))
        except:
            raise pytest.fail("The given file is not a json: {}".format(input_file_path))

    @pytest.mark.parametrize("input_file_path", ["./test_input/notvalid.json"])
    def test_not_valid_input_json(self, input_file_path):
        # open input file
        with pytest.raises(InputFileError):
            assert input_file_parser(input_file_path)

    @pytest.mark.parametrize("input_file_path", ["./test_input/NonExistingFile.json"])
    def test_non_existing_input_json(self, input_file_path):    
        # open input file
        with pytest.raises(OpenFileError):
            assert input_file_parser(input_file_path)

class TestClassFirstLevel: 
    def test_not_valid_element(self):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        input_dict['not_valid'] = 'test'
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['not_valid'] = 123
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['not_valid'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['not_valid'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

    @pytest.mark.parametrize("mandatory_elements", mandatory_elements_array)
    def test_mandatory_is_missing(self, mandatory_elements):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        del input_dict[mandatory_elements]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
    
    @pytest.mark.parametrize("mandatory_elements", mandatory_elements_array)
    def test_mandatory_is_missing_count_is_ok(self, mandatory_elements):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        del input_dict[mandatory_elements]
        input_dict['not_valid'] = 'test'
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

class TestClass_test_sequence:
    def test_sequence_empty_array(self):   
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        input_dict['test_sequence'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

    def test_sequence_dict(self):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        input_dict['test_sequence'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

    def test_sequence_calls_array(self):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        # empty array
        input_dict['test_sequence'] = []
        input_dict['test_sequence'].append([])
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

        # something is in array
        input_dict['test_sequence'] = []
        input_dict['test_sequence'].append(["test"])
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

class TestClass_test_endpoint:
    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_endpoint_does_not_exist(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        del input_dict['test_sequence'][idx_sequence]['endpoint']
        assert is_input_json_valid(input_dict)[0] == False

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_endpoint_is_not_dict(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        input_dict['test_sequence'][idx_sequence]['endpoint'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_endpoint_not_valid_element(self, idx_sequence):   
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        input_dict['test_sequence'][idx_sequence]['endpoint']['not_valid'] = ""
        result = is_input_json_valid(input_dict)
        assert result[0] == False, "{}".format(result[1])

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_endpoint_only_mandatory(self, idx_sequence):   
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['test_sequence'][idx_sequence]['endpoint'] = {}
        input_dict['test_sequence'][idx_sequence]['endpoint']['url'] = 'testURL'
        input_dict['test_sequence'][idx_sequence]['endpoint']['local_params'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_missing_endpoint_mandatory(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        input_dict['test_sequence'][idx_sequence]['endpoint']['url'] = 'testurl'
        input_dict['test_sequence'][idx_sequence]['endpoint']['local_params'] = []

        # missing url
        del input_dict['test_sequence'][idx_sequence]['endpoint']['url']
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

        # missing local_params
        input_dict['test_sequence'][idx_sequence]['endpoint']['url'] = "URL"
        del input_dict['test_sequence'][idx_sequence]['endpoint']['local_params']
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_missing_endpoint_optional(self, idx_sequence):   
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        input_dict['test_sequence'][idx_sequence]['endpoint']['t-way'] = 1
        input_dict['test_sequence'][idx_sequence]['endpoint']['allow-duplicities'] = 1

        # t-way is missing
        del input_dict['test_sequence'][idx_sequence]['endpoint']['t-way']
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]

        # allow-duplicities is missing
        input_dict['test_sequence'][idx_sequence]['endpoint']['t-way'] = 1
        del input_dict['test_sequence'][idx_sequence]['endpoint']['allow-duplicities']
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_endpoint_local_params_not_array(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        input_dict['test_sequence'][idx_sequence]['endpoint']['local_params'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]    

        input_dict['test_sequence'][idx_sequence]['endpoint']['local_params'] = 'test'
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1] 

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_endpoint_optional_not_int(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        input_dict['test_sequence'][idx_sequence]['endpoint']['t-way'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]         
        input_dict['test_sequence'][idx_sequence]['endpoint']['t-way'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]   
        input_dict['test_sequence'][idx_sequence]['endpoint']['t-way'] = "test"
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]   
        input_dict['test_sequence'][idx_sequence]['endpoint']['t-way'] = 1
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]   

        input_dict['test_sequence'][idx_sequence]['endpoint']['allow-duplicities'] = 'test'
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]   
        input_dict['test_sequence'][idx_sequence]['endpoint']['allow-duplicities'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1] 
        input_dict['test_sequence'][idx_sequence]['endpoint']['allow-duplicities'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1] 
        input_dict['test_sequence'][idx_sequence]['endpoint']['allow-duplicities'] = 1521615
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1] 

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_endpoint_url_not_string(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        input_dict['test_sequence'][idx_sequence]['endpoint']['url'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]        
        input_dict['test_sequence'][idx_sequence]['endpoint']['url'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]       
        input_dict['test_sequence'][idx_sequence]['endpoint']['url'] = 145
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]  
        input_dict['test_sequence'][idx_sequence]['endpoint']['url'] = "test"
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]          

class TestClass_test_method:
    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_method_does_not_exist(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        del input_dict['test_sequence'][idx_sequence]['method']
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_method_is_not_dict(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['test_sequence'][idx_sequence]['method'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['method'] = 'GET'
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['method'] = 165156
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_method_not_valid_element(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['test_sequence'][idx_sequence]['method']['not_valid'] = "test"
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['method']['not_valid'] = 1234
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['method']['not_valid'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['method']['not_valid'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_method_values_not_array(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['test_sequence'][idx_sequence]['method']['values'] = "test"
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['method']['values'] = 123456
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['method']['values'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['method']['values'] = ["GET"]
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_method_values_content_not_string(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['test_sequence'][idx_sequence]['method']['values'] = ["GET", "POST"]
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]
        input_dict['test_sequence'][idx_sequence]['method']['values'] = ["GET"]
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]
        input_dict['test_sequence'][idx_sequence]['method']['values'] = ["GET", 165]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['method']['values'] = [4534, 4545]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['method']['values'] = [{}, {}]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['method']['values'] = [[]]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['method']['values'] = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE"]
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]
        input_dict['test_sequence'][idx_sequence]['method']['values'] = ["not_valid", "GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE"]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

class TestClass_test_header:
    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_header_does_not_exist(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        del input_dict['test_sequence'][idx_sequence]['header']
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
    
    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_header_is_not_array(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['test_sequence'][idx_sequence]['header'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['header'] = 123456
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['header'] = 'test'
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['header'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]
        input_dict['test_sequence'][idx_sequence]['header'] = ['test']
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_header_content_not_string(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['test_sequence'][idx_sequence]['header'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]
        input_dict['test_sequence'][idx_sequence]['header'] = ['test']
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]
        input_dict['test_sequence'][idx_sequence]['header'] = ['test1', 'test2']
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]
        input_dict['test_sequence'][idx_sequence]['header'] = ['test', 123]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['header'] = [1234, 45678]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['header'] = [{}, {}]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['header'] = [[]]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

class TestClass_test_body:
    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_body_does_not_exist(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        del input_dict['test_sequence'][idx_sequence]['body']
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_body_is_not_array(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['test_sequence'][idx_sequence]['body'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['body'] = 123456
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['body'] = 'test'
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['body'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]
        input_dict['test_sequence'][idx_sequence]['body'] = ['test']
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]
        
    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_body_content_not_string(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['test_sequence'][idx_sequence]['body'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]
        input_dict['test_sequence'][idx_sequence]['body'] = ['test']
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]
        input_dict['test_sequence'][idx_sequence]['body'] = ['test1', 'test2']
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]
        input_dict['test_sequence'][idx_sequence]['body'] = ['test', 123]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['body'] = [1234, 45678]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['body'] = [{}, {}]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['body'] = [[]]
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

class TestClass_test_call_optional_elements:
    @pytest.mark.parametrize("idx_sequence", sequence_indexes())
    def test_call_optional_el_not_integer(self, idx_sequence):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['test_sequence'][idx_sequence]['t-way'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['t-way'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['t-way'] = 'test'
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['t-way'] = 123456
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]

        input_dict['test_sequence'][idx_sequence]['allow_duplicities'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['allow_duplicities'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['allow_duplicities'] = 'test'
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['allow_duplicities'] = 123456
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]

        input_dict['test_sequence'][idx_sequence]['all-in-one-test'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['all-in-one-test'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['all-in-one-test'] = 'test'
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['test_sequence'][idx_sequence]['all-in-one-test'] = 123456
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]

class TestClass_test_global_params:
    def test_global_params_not_list(self):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['global_params'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['global_params'] = 123456
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['global_params'] = 'test'
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]

    def test_global_params_empty_list(self):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['global_params'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]

    def test_global_params_content_not_array(self):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['global_params']['variable1'] = 123456
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['global_params']['variable1'] = 'test'
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['global_params']['variable1'] = {}
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]
        input_dict['global_params']['variable1'] = [1,2,3,45,6]
        input_dict['global_params']['variable2'] = ["X", "Y"]
        result = is_input_json_valid(input_dict)
        assert result[0] == True, result[1]

    def test_global_params_content_empty_array(self):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        input_dict['global_params']['variable1'] = [1,2,3,45,6]
        input_dict['global_params']['variable2'] = []
        result = is_input_json_valid(input_dict)
        assert result[0] == False, result[1]