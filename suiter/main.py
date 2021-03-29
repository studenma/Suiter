"""
Module provides a generator of test suits
"""

import sys
import os
import stat
import json
import simplejson
import yaml
import requests
import logging
import subprocess
import copy
import argparse
import importlib
import inspect
from ast import literal_eval

from exceptions import LimitExceededError
from pprint import pprint


"""
Global variables
"""
COMBINE_LOCAL = "http://127.0.0.1:3000" 
COMBINE_URL = "https://combine.testos.org"
test_script_language = "Python"
file_path = "../test_suite_output/"
file_name_base = "test_suite-"
template_file_path = "../test_suite_templates/"
# template_file_name = "pytest.template"
template_file_name = "test_pytest.py"
test_case_name = "test_case"
sut_api_url = "http://127.0.0.1:5000/api/v1/calculator"
test_case_identificator = "__test_case_id__"
test_case_identificator_replacement = "tc"
test_case_name_id = "def test_case(self):"
tab = "    "


from template_picker import get_executable_template
from input_parser import get_test_cases
from input_parser import get_first_test_case
from input_parser import input_file_parser

import input_configuration as conf

full_template = True

def log_config():
	"""
	Logger configuration
	"""
	# log format with method name
	log_format_modules = '[%(asctime)s.%(msecs)d]-%(name)s-%(levelname)s: %(module)s.%(funcName)s: %(message)s'
	# log format without method name
	log_format = '[%(asctime)s.%(msecs)d]-%(name)s-%(levelname)s: %(message)s'
	# log configuration
	logging.basicConfig(level=logging.DEBUG, format=log_format, datefmt='%H:%M:%S')
	logging.basicConfig(level=logging.ERROR, format=log_format, datefmt='%H:%M:%S')

def argument_parser():
	""" The Suiter is an application to generate a test suite for a testing of API with usage of combinatory testing\n 
	How to use:
	1. The suiter creates a test suite for all inputs in a single application pass
		./suiter input.json
	2. The Suiter creates only the test suite for the first input (-f argument). A user can modify what he needs and the other inputs are generated in the second pass of a Suiter (with a -d argument)
		a) ./suiter input.json -f
		b) ./suiter input.json -d 
	"""
	logging.debug('Parsing the arguments')
	parser = argparse.ArgumentParser()
	# input file path
	parser.add_argument('filename', help='the input json file path', nargs='?', default=conf.default_input_file)
	# Framework
	framework_choices = ['Pytest', 'Nodejs', 'C#']
	parser.add_argument('--framework', help='the framework of a resulted test suite ({} is default)'.format(conf.default_framework), choices=framework_choices,
	default=conf.default_framework)
	# output folder
	parser.add_argument('--output', help='the output folder location ({} is default)'.format(conf.default_output_folder), 
	default=conf.default_output_folder, metavar='output_folder')	
	# configuration file

	""" Two application pass mode """
	group = parser.add_argument_group('two pass mode')
	group.add_argument('-f', '--first', help='create a test suite with only the first test case', action='store_true')
	group.add_argument('-d', '--duplicate', help='complete the test suite generated with --first argument', action='store_true')
	args = parser.parse_args()

	if args.first and args.duplicate:
		parser.error('--first and --duplicate cannot be given together')
	return args
	

if __name__ == "__main__":
	""" The entry point of Suiter application """
	
	# logging configuration
	log_config() 

	# argument parser
	args = argument_parser()
	input_file_path = args.filename
	framework = args.framework
	output_path = args.output

	# parse the input file
	input_file_parser(input_file_path)

	# get all test cases
	test_cases = get_test_cases("../test_cases/calls_4/tests_100")

	"""
	First test case only / All test cases
	"""
	if full_template == False:
		# get first test case
		first_test_case = get_first_test_case(test_cases)
		# create a executable template based on a first test case
		template = get_executable_template(framework, first_test_case)
	else:
		# create a executable template based on all test cases
		template = get_executable_template(framework, test_cases)





	# API_description = parse_swagger('./web_interface/static/swagger.yaml')
	# prepare_combine_calls(API_description)
	# test_cases = api_call_combine(COMBINE_URL) # tuple is returned (combine_result, par_names)
	
	# suiter2("../test_cases/tc1_array")

	# suiter(test_cases)
	