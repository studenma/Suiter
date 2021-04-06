"""
This module provides creates an pre-template for a language of a user's choice
"""

import logging 
logger = logging.getLogger(__name__)

from exceptions import TemplateError
from exceptions import OpenFileError

"""
List of all supported frameworks and its paths to its pretemplates
"""
paths = {
	"Pytest": 		"./pre-templates/pytest.py",
	"Python": 		"./pre-templates/python.py",
	"JavaScript": 	"./pre-templates/javascript.js",
}

def get_pre_template_path(framework):
	"""
	Returns the path to pre-template
	"""
	logger.debug('Calling the get_pre_template_path method with a following parameter: ' + framework)
	try:
		return paths[framework]
	except:
		message = "The following framewrok does not have specified file path: " + framework
		raise TemplateError(__name__, "template_picker", message)

def create_template(path, module, tc):
	"""
	Import a module which should be used (based on a desired framework)
	Call the create_template method in this module
	"""
	logger.debug("Calling the create_template method")

	if module == "Python":
		from suiter_python import create_template as create
	elif module == "Pytest":
		from suiter_pytest import create_template as create
	elif module == "JavaScript":
		from suiter_javascript import create_template as create
	else:
		# TODO: ErrorHandling with variables
		message = "The following module does not exist: "
		raise TemplateError(__name__, "create_template", message)
	create(path, tc)

def template_picker(framework, first_tc):
	"""
	What pre-template should be used (based on a user's choice)
	"""
	logger.debug('Calling the template_picker method with a following parameter: ' + framework)
	
	# get the pre-template path
	path = get_pre_template_path(framework)
	return path

def get_executable_template(framework, tc):
	"""
	The entry method for this module
	"""
	logger.debug("Calling the get_template method")
	
	path = template_picker(framework, tc)

	# send the path of a pre-template to the corresponding module
	create_template(path, framework, tc)
	
