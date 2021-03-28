import pytest
import json

""" import suiter package """ 
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from input_parser import parse_input_file
from exceptions import *

test_cases_files = [
    './test_input/input01.json',
    './test_input/input02.json',
    './test_input/input03.json'
]

@pytest.mark.parametrize("input_file_path", ["./test_input/input01.json"])
def test_valid_input_json(input_file_path):
    # open input file
    try:
        with open(input_file_path) as json_file:
            input_dict = json.load(json_file)
    except OpenFileError:
        raise pytest.fail("Could not open the file: {}".format(input_file_path))
    except:
        raise pytest.fail("The given file is not a json: {}".format(input_file_path))


@pytest.mark.parametrize("input_file_path", ["./test_input/input02.json"])
def test_not_valid_input_json(input_file_path):
    # open input file
    with pytest.raises(InputFileError):
        assert parse_input_file(input_file_path)

@pytest.mark.parametrize("input_file_path", ["./test_input/NonExistingFile.json"])
def test_non_existing_input_json(input_file_path):    
    # open input file
    with pytest.raises(OpenFileError):
        assert parse_input_file(input_file_path)
