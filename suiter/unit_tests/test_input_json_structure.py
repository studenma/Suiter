import pytest
import json
# from unittest import TestCase

""" import suiter package """ 
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from input_parser import input_file_parser
from input_parser import is_input_json_valid
from exceptions import *

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

    @pytest.mark.parametrize("input_file_path", ["./test_input/input02.json"])
    def test_not_valid_input_json(self, input_file_path):
        # open input file
        with pytest.raises(InputFileError):
            assert input_file_parser(input_file_path)

    @pytest.mark.parametrize("input_file_path", ["./test_input/NonExistingFile.json"])
    def test_non_existing_input_json(self, input_file_path):    
        # open input file
        with pytest.raises(OpenFileError):
            assert input_file_parser(input_file_path)

class TestClassContentCheck: 
    first_level_cases = [
        './test_input/first_level_tests/input03.json',
        './test_input/first_level_tests/input04.json',
        './test_input/first_level_tests/input05.json',
    ]

    test_sequence_element_cases = [
        './test_input/seq_elem_tests/input01.json',
        './test_input/seq_elem_tests/input02.json',
        './test_input/seq_elem_tests/input03.json',
    ]

    @pytest.mark.parametrize("input_file_path", first_level_cases)
    def test_first_level(self, input_file_path):    
        # open input file
        with pytest.raises(InputFileError):
            assert input_file_parser(input_file_path)

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
        assert is_input_json_valid(input_dict)[0] == False

    def test_sequence_dict(self):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        input_dict['test_sequence'] = {}
        assert is_input_json_valid(input_dict)[0] == False

    def test_endpoint_does_not_exist(self):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        del input_dict['test_sequence'][0]['endpoint']
        assert is_input_json_valid(input_dict)[0] == False

    def test_endpoint_is_array(self):
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        input_dict['test_sequence'][0]['endpoint'] = []
        assert is_input_json_valid(input_dict)[0] == False

    def test_missing_endpoint_url(self):   
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        del input_dict['test_sequence'][0]['endpoint']['url']
        assert is_input_json_valid(input_dict)[0] == False

    def test_endpoint_not_valid_element(self):   
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))
        
        input_dict['test_sequence'][0]['endpoint']['not_valid'] = ""
        assert is_input_json_valid(input_dict)[0] == False

    def test_endpoint_only_url(self):   
        input_file_path = './test_input/valid.json'
        # open input file and check if it is a json
        try:
            with open(input_file_path) as json_file:
                input_dict = json.load(json_file)        
        except:
            raise pytest.fail("The given file is not a json or it could not be read: {}".format(input_file_path))

        del input_dict['test_sequence'][0]['endpoint']['T-way']
        del input_dict['test_sequence'][0]['endpoint']['allow-duplicities']
        del input_dict['test_sequence'][0]['endpoint']['local_params']
        assert is_input_json_valid(input_dict)[0] == True



