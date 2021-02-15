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


from exceptions import LimitExceededError
from pprint import pprint



COMBINE_LOCAL = "http://127.0.0.1:3000"
COMBINE_URL = "https://combine.testos.org"
test_script_language = "Python"
file_path = "../test_suite_output/"
file_name_base = "test_suite-"
template_file_path = "../test_suite_templates/"
template_file_name = "pytest.template"
test_case_name = "test_case"

sut_api_url = "http://127.0.0.1:5000/api/v1/calculator"

"""
Logger configuration
"""
log_format = '[%(asctime)s.%(msecs)d]-%(name)s-%(levelname)s: %(module)s.%(funcName)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format, datefmt='%H:%M:%S')
logging.basicConfig(level=logging.ERROR, format=log_format, datefmt='%H:%M:%S')

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
		file_pointer.write("\tdef test_case_" + str(test_case_cnt) + "(self):\n")
		# payload
		payload = "\"{\\\"operation\\\": \\\"add\\\",\\\"num1\\\": " + str(test[0]) + ",\\\"num2\\\": " + str(test[1]) + "}\""
		file_pointer.write("\t\tpayload = " + payload + "\n")
		# API call 
		file_pointer.write("\t\tresponse = requests.request(\"GET\", url, headers=headers, data=payload)\n")
		# print response
		# file_pointer.write("\t\tprint(response.text)\n\n")
		# assert
		file_pointer.write("\t\tassert response.status_code == 200\n")
		file_pointer.write("\t\tassert response.json()['Result'] == <TODO:>\n\n")
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
	"""
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
	with open(swag, 'r') as stream:
		try:
			content = yaml.safe_load(stream)
		except yaml.YAMLError as exc:
			print(exc)

	"""
	Get API informations - [endpoint=[method=[]]]
	API_desc = [
		{
			tag: "class_name"
			endpoint: "/calculator", 
			method: "GET", 
			params: []
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

	# co = json.dumps(content['test_case'][0])
	# print("--------------")
	# print(json.dumps(content['test_case']))
	# exit(444)
	co = content['test_case'][0]
	# TODO: with open('combine_input2.json', 'r') as content_file:
	
	# parsed = json.dump(co)
	# print("-------------")
	# print(type(parsed))
	# print("-------------")
	# print(parsed)
	
	f = open('combine_input5.json', 'w')
	# f.write(simplejson.dumps(co, sort_keys=True))
	temp_string = json.dumps(co)
	# temp_string = temp_string.replace('\'', '\"')
	f.write(temp_string)
	# json.dump(co, f)
	f.close()
	# exit(5)



if __name__ == "__main__":
	API_desc = parse_swagger('./web_interface/static/swagger.yaml')
	# TODO: Use API_desc to generate test suite
	prepare_combine_calls(API_desc)
	test_cases = api_call_combine(COMBINE_URL) # tuple is returned (combine_result, par_names)
	suiter(test_cases)