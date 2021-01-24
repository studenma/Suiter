"""
Module provides a generator of test suits
"""

import sys
import os
import json
import requests
import logging

COMBINE_LOCAL = "http://127.0.0.1:3000"
COMBINE_URL = "https://combine.testos.org"

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
		print(response.json())
	except ValueError: # includes json.decoder.JSONDecodeError
		logging.error('Response from Combine is not in a valid JSON format')

	# print(response.text)
	# print(response.content)
	# print(response.status_code)


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
	api_call_combine(COMBINE_URL)