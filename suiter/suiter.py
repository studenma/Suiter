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

sut_api_url = "http://127.0.0.1:5000/api/calculator"

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
		return response.json()
	except ValueError: # includes json.decoder.JSONDecodeError
		logging.error('Response from Combine is not in a valid JSON format')

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
	Output: file pointer
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
	f = open(file_relative_path_name, "w")
	return f


def test_suite_header(file_pointer):
	logging.debug('Creating a header of a \'' + file_pointer.name +  '\' test script')
	# import
	file_pointer.write("import requests\n\n")
	# url
	file_pointer.write("url = \"" + sut_api_url + "\"\n\n")
	# payload
	payload = "{\"operation\": \"add\",\"num1\": 3,\"num2\": 2}"
	file_pointer.write("payload = " + payload + "\n")
	# header
	headers = {
		'Content-Type': 'application/json'
	}
	file_pointer.write("headers = " + json.dumps(headers) + "\n\n")
	# API call 
	file_pointer.write("response = requests.request(\"GET\", url, headers=headers, data=payload)\n\n")
	# response
	file_pointer.write("print(response.text)\n")
	file_pointer.close()
	exit(1)

def suiter(test_cases):
	"""
	Test suite creator for Python Requests
	"""
	file_pointer = create_test_suite_file()
	test_suite_header(file_pointer)

	






def python_test_file():
	return "TEST"

def generate_test_suite(test_suite):
	"""
	Returns a test suite for a given API endpoint with specified characteristics
	"""
	print("DEBUG: generate_test_suite()", flush=True)
	test_suite = json.loads(test_suite)

	for test_case in test_suite:
		print(test_case, flush=True)

	file = open("../../tests/testSuite.py", "w")
	data = python_test_file()
	file.write(data)
	file.close()


if __name__ == "__main__":
	test_cases = api_call_combine(COMBINE_URL)
	suiter(test_cases)