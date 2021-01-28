"""
Module provides a generator of test suits
"""

import sys
import os
import json
import requests
import logging

from exceptions import LimitExceededError

COMBINE_LOCAL = "http://127.0.0.1:3000"
COMBINE_URL = "https://combine.testos.org"
test_script_language = "Python"
file_path = "../test_suite_output/"
file_name_base = "test_suite-"
template_file_path = "../test_suite_templates/"
template_file_name = "pytest.template"

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
	payload="{\r\n    \"name\": \"SUT name\", \r\n    \"t_strength\": \"2\", \r\n    \"dont_care_values\": \"no\", \r\n    \"values\": \"values\", \r\n    \"parameters\": [\r\n        {\"identificator\": \"P1\", \"type\": \"integer\", \"blocks\": [\"P1<0\", \"P1>0\", \"P1=0\"]}, \r\n        {\"identificator\": \"P2\", \"type\": \"integer\", \"blocks\": [\"P2<0\", \"P2>0\", \"P2=0\"]}\r\n    ], \r\n    \"constraints\": []\r\n}"
		  
	logging.debug('Calling: ' + api_end_point_base_url + '/generate:\n' + payload)
	# Send REST API request
	try:
		response = requests.request("GET", api_end_point_base_url + "/generate", headers=headers, data=payload)
		logging.debug('Combine response: ' + str(response.json()))
		return response.json()
	except ValueError: # includes json.decoder.JSONDecodeError
		logging.error('Response from Combine is not in a valid JSON format')
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

def edit_TODO_tags(file_name):
	logging.debug('Edditing TODO tags in ' + file_name)
	# open file for reading only
	f = open(file_name, "r")
	
	new_file_content = ""

	# loop around all TODO tags and ask user for input
	print("Enter a expected result of following asserts:")
	for line in f:
		print(line, end=" ")
		if '<TODO:>' in line:
			assert_result = input()
			new_file_content += line.replace('<TODO:>', assert_result)
		else:
			new_file_content += line
	f.close()

	# write a new content into test suite file
	f = open(file_name, 'w')
	f.write(new_file_content)
	f.close()


def edit_template_tags(file_name, test_cases):
	logging.debug('Edditing template tags')
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
			for _ in range(len(test_cases)): # for number of test cases
				file_pointer.write(for_content + "\n")
			for_content = ""
		else:
			if duplicity_switch is 1:
				for_content += line
			else:
				file_pointer.write(line)
	exit(1)

	from_imports = [['math', 'fabs'], ['math', 'factorial']]
	imports = ['sys', 'os']
	import_headers = {'Content-Type': 'application/json'}
	y = {'Test':'TestValu'}
	import_headers.update(y)

	class_name = "TryTesting"
	test_name = 'test_case_'
	payload = []
	for test in test_cases:
		p = "\"{\\\"operation\\\": \\\"add\\\",\\\"num1\\\": " + str(test[0]) + ",\\\"num2\\\": " + str(test[1]) + "}\""
		payload.append(p)
	status_code = '200'
	method = "GET"
	
	for line in f:
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
		elif '<TEST_NAME>' in line:
			new_file_content += line.replace('<TEST_NAME>', test_name)
		elif '<PAYLOAD>' in line:
			new_file_content += line.replace('<PAYLOAD>', payload)
		elif '<METHOD>' in line:
			new_file_content += line.replace('<METHOD>', method)
		elif '<STATUS_CODE>' in line:
			new_file_content += line.replace('<STATUS_CODE>', status_code)
		else:
			new_file_content += line
	f.close()

	print("\n" + new_file_content)
	exit(10)
	

	
		

def suiter(test_cases):
	"""
	Test suite creator for Python Requests
	"""
	file_name = create_test_suite_file()
	#test_suite_header()
	#test_suite_class(test_cases)
	

	# edit TODO tags
	#edit_TODO_tags(file_name)


	edit_template_tags(file_name, test_cases)

	



if __name__ == "__main__":
	test_cases = api_call_combine(COMBINE_URL)
	suiter(test_cases)