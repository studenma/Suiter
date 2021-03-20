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

def api_call_combine(api_end_point_base_url):
	"""
	REST API call to combine
	"""
	headers = {
		'Content-Type': 'application/json'
	}

	combine_output = []
	#payload="{\r\n    \"name\": \"SUT name\", \r\n    \"t_strength\": \"2\", \r\n    \"dont_care_values\": \"no\", \r\n    \"values\": \"values\", \r\n    \"parameters\": [\r\n        {\"identificator\": \"num1\", \"type\": \"integer\", \"blocks\": [\"num1<0\", \"num1>0\", \"num1=0\"]}, \r\n        {\"identificator\": \"num2\", \"type\": \"integer\", \"blocks\": [\"num2<0\", \"num2>0\", \"num2=0\"]}\r\n    ], \r\n    \"constraints\": []\r\n}"
	with open('combine_input5.json', 'r') as content_file:
		payload = content_file.read()
	logging.debug('Calling: ' + api_end_point_base_url + '/generate:\n' + str(payload))

	# getting the names of parameters
	payload_json = json.loads(payload)
	for var in payload_json['parameters']:
		combine_output.append(var['identificator'])

	# Send REST API request
	try:
		response = requests.request("GET", api_end_point_base_url + "/generate", headers=headers, data=payload)
		logging.debug('Combine response: ' + str(response.json()))
		logging.debug('Tuple is returned: ' + str((response.json(), combine_output)))
		return response.json(), combine_output
	except ValueError: # includes json.decoder.JSONDecodeError
		logging.error('Response from Combine is not in a valid JSON format')
		exit(9)
	# except ConnectionError:
	# 	logging.error('Unable to connect to the Combine server')

def parse_file_name(file_name):
	"""
	Ipnut: 	file_name-XXX.py
	Output: XXX
	"""
	return file_name[-6:][:3]

def create_test_suite_file():
	"""
	Creates a test file
	Max. supported number of test files is 999
	Output: File name
	"""
	logging.debug('Creating a test suite file')
	# Find the first available file number
	logging.debug('Looking for a available file number')
	for cnt in range (1,999):
		file_relative_path_name = file_path + file_name_base + f"{cnt:03}" + ".py"
		if not os.path.isfile(file_relative_path_name):
			break
	else: # for loop finished without break
		logging.error('Maximum file count of 999 has been exceeded')
		raise LimitExceededError('Maximum file count of 999 has been exceeded')	

	# Create a file 
	logging.debug('Creating a file: ' + file_relative_path_name)
	global file_pointer
	file_pointer = open(file_relative_path_name, "w")
	return file_pointer.name

def test_suite_header():
	logging.debug('Creating a header of a \'' + file_pointer.name +  '\' test script')
	# import
	file_pointer.write("from unittest import TestCase\n")
	file_pointer.write("import requests\n\n")
	# url
	file_pointer.write("url = \"" + sut_api_url + "\"\n\n")
	# header
	headers = {
		'Content-Type': 'application/json'
	}
	file_pointer.write("headers = " + json.dumps(headers) + "\n\n")
	
def test_suite_class(test_cases):
	logging.debug('Creating a test class of a \'' + file_pointer.name +  '\' test script')
	# class
	file_pointer.write("class TryTesting(TestCase):\n")
	
	# Test case loop
	test_case_cnt = 1
	for test in test_cases:
		file_pointer.write(tab + "def test_case_" + str(test_case_cnt) + "(self):\n")
		# payload
		payload = "\"{\\\"operation\\\": \\\"add\\\",\\\"num1\\\": " + str(test[0]) + ",\\\"num2\\\": " + str(test[1]) + "}\""
		file_pointer.write(2*tab + "payload = " + payload + "\n")
		# API call 
		file_pointer.write(2*tab + "response = requests.request(\"GET\", url, headers=headers, data=payload)\n")
		# assert
		file_pointer.write(2*tab + "assert response.status_code == 200\n")
		file_pointer.write(2*tab + "assert response.json()['Result'] == <TODO:>\n\n")
		test_case_cnt+=1

def edit_ASSERT_tags(file_name):
	logging.debug('Edditing TODO tags in ' + file_name)
	# open file for reading only
	f = open(file_name, "r")
	
	new_file_content = ""

	# loop around all TODO tags and ask user for input
	print("Enter a expected result of following asserts:")
	for line in f:
		print(line, end=" ")
		if '<ASSERT_RESULT>' in line:
			assert_result = input()
			new_file_content += line.replace('<ASSERT_RESULT>', assert_result)
		else:
			new_file_content += line
	f.close()

	# write a new content into test suite file
	f = open(file_name, 'w')
	f.write(new_file_content)
	f.close()

def edit_template_tags(file_name, test_cases):
	logging.debug('Edditing template tags')
	print(test_cases)
	f = open(template_file_path + template_file_name, 'r')
	new_file_content = ""

	# TODO: prekopirovat obsah sablony do noveho souboru + rozsirit o <FOR>
	duplicity_switch = 0
	for_content = ""
	for line in f:
		if '<FOR>' in line:
			duplicity_switch = 1
		elif '<END_FOR>' in line:
			duplicity_switch = 0
			for _ in range(len(test_cases[0])): # for number of test cases
				file_pointer.write(for_content + "\n")
			for_content = ""
		else:
			if duplicity_switch == 1:
				for_content += line
			else:
				file_pointer.write(line)

	from_imports = [['math', 'fabs'], ['math', 'factorial']]
	imports = ['sys', 'os']
	import_headers = {'Content-Type': 'application/json'}
	
	y = {'Test':'TestValu'}
	import_headers.update(y)

	class_name = "TryTesting"

	status_code = '200'
	method = "GET"

	file_pointer.close()
	file_p = open(file_pointer.name, 'r')
	
	for line in file_p:
		if '<FROM_IMPORT>' in line:
			for custom_from_import in from_imports:
				new_file_content += 'from ' + custom_from_import[0] + ' import ' + custom_from_import[1] + '\n'
		elif '<IMPORT>' in line:
			for custom_import in imports:
				new_file_content += 'import ' + custom_import + '\n'
		elif '<URL>' in line:
			new_file_content += line.replace('<URL>', sut_api_url)
		elif '<HEADERS>' in line:
			new_file_content += line.replace('<HEADERS>', str(import_headers))
		elif '<CLASS_NAME>' in line:
			new_file_content += line.replace('<CLASS_NAME>', class_name)
		# elif '<TEST_NAME>' in line:
		# 	new_file_content += line.replace('<TEST_NAME>', test_name)
		# elif '<PAYLOAD>' in line:
		# 	new_file_content += line.replace('<PAYLOAD>', payload)
		# elif '<METHOD>' in line:
		# 	new_file_content += line.replace('<METHOD>', method)
		# elif '<STATUS_CODE>' in line:
		# 	new_file_content += line.replace('<STATUS_CODE>', status_code)
		else:
			new_file_content += line
	file_p.close()

	file_p = open(file_pointer.name, 'w')
	file_p.write(new_file_content)
	file_p.close()


	payload = []
	for i in range(len(test_cases[0])):
		p = {}
		for j in range(len(test_cases[0][i])):
			p[test_cases[1][j]] = test_cases[0][i][j]
		payload.append(p)

	fp = open(file_pointer.name, 'r')
	new_file_content = ""
	idx_case = 0
	for line in fp:
		if '<TEST_NAME>' in line:
			idx_case += 1
			new_file_content += line.replace('<TEST_NAME>', test_case_name + "_" + str(idx_case))
		elif '<PAYLOAD>' in line:
			new_file_content += line.replace('<PAYLOAD>', json.dumps(payload.pop(0)))
		elif '<METHOD>' in line:
			new_file_content += line.replace('<METHOD>', "\"GET\"")
		elif '<STATUS_CODE>' in line:
			new_file_content += line.replace('<STATUS_CODE>', "200")
		else:
			new_file_content += line
	fp.close()

	file_p = open(file_pointer.name, 'w')
	file_p.write(new_file_content)
	file_p.close()

def suiter(test_cases):
	"""Documentation dor a function
	Test suite creator for Python Requests
	"""
	file_name = create_test_suite_file()
	#test_suite_header()
	#test_suite_class(test_cases)
	
	edit_template_tags(file_name, test_cases)
	edit_ASSERT_tags(file_name)

	file_p = open('./run_test.sh', 'w')
	file_p.write("#!/bin/bash\n")
	strin = "pytest " + file_name
	file_p.write(strin)
	file_p.close()
	st = os.stat('./run_test.sh')
	os.chmod('./run_test.sh', st.st_mode | stat.S_IEXEC)
	return_code = subprocess.call('./run_test.sh')

def parse_swagger(swag):
	"""
	Retrieves a desired information from a swagger file
	Input: .yaml
	Output: Array of following dictionaries:
			{
				tag: "class_name"
				endpoint: "/calculator", 
				method: "GET", 
				params: []
			}
	"""
	with open(swag, 'r') as stream:
		try:
			content = yaml.safe_load(stream)
		except yaml.YAMLError as exc:
			print(exc)

	"""
	Get API informations - [endpoint=[method=[]]]
	API_desc = [
		{
			
		}
	]
	"""
	API_desc = []
	# for all functions
	for func in content['paths']:
		# for all methods
		for meth in content['paths'][func]:
			test_class = {}
			test_class['tag'] = content['paths'][func][meth]['tags'][0]
			test_class['endpoint'] = func
			test_class['method'] = meth
			test_class['params'] = content['paths'][func][meth]['parameters']
			API_desc.append(test_class)	

	pprint(API_desc)
	# exit(1)			
	return API_desc

def get_characteristics(parameter):
	print(parameter)
	value = {}
	n = parameter['name']
	if parameter['type'] == 'string':
		value['identificator'] = n
		value['type'] = "string"
		value['blocks'] = []
		value['blocks'].append(n + "='add'")
		value['blocks'].append(n + "='substract'")
		value['blocks'].append(n + "='multiply'")
	elif parameter['type'] == 'integer':
		value['identificator'] = n
		value['type'] = "integer"
		value['blocks'] = []
		value['blocks'].append(n + ">0")
		value['blocks'].append(n + "<0")
		value['blocks'].append(n + "=0")
	else:
		print("Je to neco jineho")
		exit(33)
	return value

def prepare_combine_calls(description):
	"""
	Test class attributes: endpoint, method, params, tag
	test_suite = [
		{
			class_name
			url 

		}
	]
	"""
	# get combine_input_template
	f = open('./combine_input.template', 'r')
	content = f.read()
	f.close()


	# make a json out of it 
	content = json.loads(content)
	
	# duplicate numer of test_cases
	for test_idx in range(1, len(description)):
		temp = copy.copy(content['test_case'][0])
		content['test_case'].append(temp)
	
	# fill up the template
	idx = 0
	for test_class in description:
		name = test_class['tag'] + "_" + test_class['method'] 
		content['test_case'][idx]['values'] = 'values'
		content['test_case'][idx]['dont_care_values'] = 'no'
		content['test_case'][idx]['name'] = name
		content['test_case'][idx]['t_strength'] = "2"

		content['test_case'][idx]['parameters'].pop()

		# for all params
		for par in test_class['params']:
			val = get_characteristics(par)
			content['test_case'][idx]['parameters'].append(val)
		idx += 1
		break

	co = content['test_case'][0]
	# TODO: with open('combine_input2.json', 'r') as content_file:

	
	f = open('combine_input5.json', 'w')
	temp_string = json.dumps(co)
	f.write(temp_string)
	f.close()

def test_case_check_in(tc):
	logging.debug('Test cases template preparation:' + str(tc))
	for message in tc:
		for part in message:
			print(part)

	exit(1)

def fullify_pre_template_one_call():
	type(465)

def preapre_verify_tag(length):
	verify_string = ""
	verify_string += (tab + "if test_case == test_case_id:\n")

	for calls_expect in range(length):
		if(calls_expect == 0):
			new_line = 2*tab + "if request_id == \"req" + str(calls_expect+1) + "\":"
		else:
			new_line = 2*tab + "elif request_id == \"req" + str(calls_expect+1) + "\":"
		verify_string += new_line
		new_block = """ 	
			#####################################
			# TODO: HERE IS YOUR CODE TO PREDEFINE ALL TEST CASE VERIFICATION
			# example:
			## statusCode = None
			## json = {'Result': None}\n """
		verify_string += new_block
	return verify_string

def get_header_content_from_yaml(file_name):
	with open('./templates/python/' + file_name, 'r') as input_file:
		head = input_file.read()
		
	
	input_file.close()
	return yaml.load(head)

def prepare_test_case_list_tag(tc):
	tc_list_string = ""
	tc_list_string += (tab + "if test_case == test_case_id:\n")
	
	for call_cnt in range(0, len(tc)):
		if(call_cnt == 0):
			new_line = 2*tab + "if request_id == \"req" + str(call_cnt+1) + "\":\n"
		else:
			new_line = 2*tab + "elif request_id == \"req" + str(call_cnt+1) + "\":\n"
		tc_list_string += new_line
		
		# [URL, METHOD, HEADER, BODY]
		# URL
		new_line = 3*tab + "url = \"" + str(tc[call_cnt][0]) + "\"\n"
		tc_list_string += new_line
		# METHOD
		new_line = 3*tab + "method = \"" + str(tc[call_cnt][1]) + "\"\n"
		tc_list_string += new_line
		# HEADER
		h = get_header_content_from_yaml(tc[call_cnt][2])
		new_line = 3*tab + "header = " + str(h) + "\n"
		tc_list_string += new_line
		# BODY
		new_line = 3*tab + "body = \"" + str(tc[call_cnt][3]) + "\"\n"
		tc_list_string += new_line
	return tc_list_string

# https://stackoverflow.com/questions/10112614/how-do-i-create-a-multiline-python-string-with-inline-variables
def prepare_requests_tag(tc, length):
	request_string = ""

	for idx in range(1, length+1):
		req_tag = 'req' + str(idx)
		new_block = """
		\"\"\"
        {TestCnt}. Request
        \"\"\"
		# execution
        call = list_of_all_cases(test_case_id, \"{RequestTag}\")
        response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))
        # request verification
        expected_response = verify(test_case_id, \"{RequestTag}\")
        #####################################
        # TODO: HERE MAY BE YOUR ASSERTIONS
        # delete this part otherwise
        # the assertions have to be based on 'expected_response' variable
        # example:
        # assert response.status_code == expected_response.status_code
        # assert response.json() == expected_response.json
			""".format(TestCnt=idx, RequestTag=req_tag)
		request_string += new_block

	return request_string

def prepare_verification_tag(tc, length):
	verification_string = ""

	new_block = 2*tab + """\"\"\"
		SUT Verification
		\"\"\"
		result = verify(test_case_id, "sut")
		#####################################
		# TODO: HERE MAY BE YOUR ASSERTIONS
		# delete this part otherwise
		# the assertions have to be based on 'result' variable
	"""
	verification_string += new_block

	return verification_string

def fullify_pre_template_multiple_calls(tc):
	f = open('templates/python/pre-template', 'r')
	
	new_file_content = ""

	for line in f:
		if '<VERIFY>' in line:
			new_line = preapre_verify_tag(len(tc))
			new_file_content += line.replace('<VERIFY>', new_line)
		elif '<TEST_CASE_LIST>' in line:
			new_line = prepare_test_case_list_tag(tc)
			new_file_content += line.replace('<TEST_CASE_LIST>', new_line)
		elif '<REQUESTS>' in line:
			new_line = prepare_requests_tag(tc, len(tc))
			new_file_content += line.replace('<REQUESTS>', new_line)
		elif '<VERIFICATION>' in line:
			new_line = prepare_verification_tag(tc, len(tc))
			new_file_content += line.replace('<VERIFICATION>', new_line)
		else:
			new_file_content += line
	f.close()
	
	f = open('templates/python/template', 'w')
	f.write(new_file_content)
	f.close()

def if_first_word_if_replace_elif(string):
	for idx in range(0, len(string)):
		if(string[idx].isspace()):
			continue
		else:
			if (string[idx] == 'i') and (string[idx+1] == "f") and (string[idx+2] == " "):
				string = string.replace('if', 'elif', 1)
			break
	return string

def duplicate(buffer, counter):
	# the original code
	# replace test_case_identificator with a value for the first test case
	new_buffer = buffer
	if test_case_identificator in buffer:
		replacement = "\"" + test_case_identificator_replacement + str(1) + "\""
		new_buffer = new_buffer.replace(test_case_identificator, replacement)
	if test_case_name_id in new_buffer:
		temp = test_case_name_id[4:][:-7]
		replacement = "def " +temp + str(1) + "(self):"
		new_buffer = new_buffer.replace(test_case_name_id, replacement)

	# duplicate with counter == 2 (the first duplicate)
	duplicate = if_first_word_if_replace_elif(buffer)
	
	# duplicate for counter > 1
	for idx in range(2,counter+1):
		temp_duplicate = duplicate
		# replace test_case_identificator with a value for all test case idxs
		if test_case_identificator in duplicate:
			replacement = "\"" + test_case_identificator_replacement + str(idx) + "\""
			temp_duplicate = duplicate.replace(test_case_identificator, replacement)
		if test_case_name_id in temp_duplicate:
			temp = test_case_name_id[4:][:-7]
			replacement = "def " +temp + str(idx) + "(self):"
			temp_duplicate = temp_duplicate.replace(test_case_name_id, replacement)		
		new_buffer += temp_duplicate
	return new_buffer

def duplicate_tc(tc_cnt, req_cnt, test_cases):
	new_block = ""

	for idx in range(2,tc_cnt+1):
		replacement = test_case_identificator_replacement + str(idx)
		new_block += tab + "elif test_case == \"" + replacement + "\":\n"

		for req_idx in range(1,req_cnt+1):
			if req_idx == 1:
				new_block += 2*tab + "if request_id == \"req" + str(req_idx) + "\":\n"
			else:
				new_block += 2*tab + "elif request_id == \"req" + str(req_idx) + "\":\n"
			new_block += 3*tab + "url = \"" + str(test_cases[idx-1][req_idx-1][0]) + "\"\n"
			
			new_block += 3*tab + "method = \"" + str(test_cases[idx-1][req_idx-1][1]) + "\"\n"
			h = get_header_content_from_yaml(test_cases[idx-1][req_idx-1][2])
			new_block += 3*tab + "header = " + str(h) + "\n"
			new_block += 3*tab + "body = \"" + str(test_cases[idx-1][req_idx-1][3]) + "\"\n"
	
	return new_block

def duplicate_template_tags(file_path, test_cases):
	length = len(test_cases)
	f_read = open(file_path, 'r')
	f_write = open('templates/python/test_suite.py', 'w')

	new_file_content = ""
	duplicate_buffer = ""
	in_tag = 0
	in_tag_tc = 0

	for line in f_read:
		if '<duplicate>' in line:
			if (in_tag == 1) or (in_tag_tc == 1):
				# raise Error('trying to do nested duplicate tags')	
				print(in_tag_tc)
				exit(33)
			else:
				in_tag = 1
		elif '</duplicate>' in line:
			if (in_tag == 0) or (in_tag_tc == 1):
				# raise Error('trying to do nested duplicate tags')	
				exit(44)
			else:
				in_tag = 0
				new_file_content += duplicate(duplicate_buffer, length)
				duplicate_buffer = ""
		elif '<tc_extend>' in line:
			if (in_tag == 1) or (in_tag_tc == 1):
				# raise Error('trying to do nested duplicate tags')	
				exit(55)
			else:
				in_tag_tc = 1
		elif '</tc_extend>' in line:
			if (in_tag == 1) or (in_tag_tc == 0):
				# raise Error('trying to do nested duplicate tags')	
				exit(66)
			else:
				in_tag_tc = 0
				if test_case_identificator in duplicate_buffer:
					replacement = "\"" + test_case_identificator_replacement + str(1) + "\""
					new_file_content += duplicate_buffer.replace(test_case_identificator, replacement)
				new_file_content += duplicate_tc(length, 3, test_cases)
				duplicate_buffer = ""
		else:
			if (in_tag == 1) or (in_tag_tc == 1):
				duplicate_buffer += line
			else:
				new_file_content += line

	f_write.write(new_file_content)
	f_read.close()
	f_write.close()

def suiter2(test_cases):
	# read file with an input for suiter module
	with open(test_cases, 'r') as input_file:
		test_cases = input_file.read()
	input_file.close()

	# change format of test_cases from string to array
	test_cases = literal_eval(test_cases)

	"""
	Fullify the pre-template
	* get the first test case which is used as a reference
	* check how many calls are in this test case
	* fullify the pre-template with a first test case and it's calls
	"""
	tc_calls_count = len(test_cases[0])
	if tc_calls_count == 1:
		print("Vyplnuji sablonu s jednim callem")
		fullify_pre_template_one_call()
	else:
		print("Vyplnuji sablonu s vice cally")
		fullify_pre_template_multiple_calls(test_cases[0])


	"""
	Opetovne spusteni suiteru s vyplnenou sablonou
	"""
	duplicate_template_tags('templates/python/filled_template.py', test_cases)



from template_picker import get_executable_template
from input_parser import get_framework
from input_parser import get_test_cases
from input_parser import get_first_test_case

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


if __name__ == "__main__":
	"""
	Main function
	"""
	# logging configuration
	log_config() 

	# framework selection
	framework = get_framework("Pytest") 

	# get all test cases
	test_cases = get_test_cases("../test_cases/calls_4/tests_1")

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
	