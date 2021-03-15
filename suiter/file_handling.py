"""
""" 

import logging
logger = logging.getLogger(__name__)

from exceptions import OpenFileError

def get_file_content(path):
	"""
	Get the content of file
	"""
	logger.debug('Calling the get_file_content method with a following parameter: ' + path)
	
	try:
		with open(path, 'r') as pre_template_file:
			content = pre_template_file.read()
			return content
	except:
		message = "The opening of a following file failed: " + path
		raise OpenFileError(__name__, "get_file_content", message)