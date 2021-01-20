"""
Module provides a generator of test suits
"""

import sys
import os
import json

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