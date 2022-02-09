"""
This module is used to decide which language of resulted script should have been used
Redirect the test cases data to a module corresponding with this language
"""

from ast import literal_eval
import logging
logger = logging.getLogger(__name__)

from suiter_exceptions import *
import suiter_classes_and_globals as globe
from suiter_general import get_file_content

def create_template(path, module, tc):
    """
    Import a module which should be used (based on a desired framework)
    Call the create_template function in this module (all these modules has to contain this function)
    """
    logger.debug("Calling the create_template function")

    if module == "Python":
        from suiter_python import create_template as create
    elif module == "Pytest":
        from suiter_pytest import create_template as create
    elif module == "JavaScript":
        from suiter_javascript import create_template as create
    else:
        message = "The following module does not exist: "
        raise TemplateError(__name__, "create_template", message)
    create(path, tc)

def get_pre_template_path(framework):
    """
    Returns the path to pre-template of a desired language
    """
    logger.debug('Calling the get_pre_template_path method with a following parameter: ' + framework)

    """ Dictionary of all supported frameworks and its paths to its pretemplates """
    paths = {
        "Pytest": 		"./pre-templates/pytest.py",
        "Python": 		"./pre-templates/python.py",
        "JavaScript": 	"./pre-templates/javascript.js",
    }
    
    # get the path of a framework pre-template
    try:
        return paths[framework]
    except:
        message = "The following framewrok does not have specified file path of pre-template: " + framework
        raise TemplateError(__name__, "template_picker", message)

def get_test_cases(path):
    """
    Get list of test cases of a given file (output of suiter_preparator module)
    Return an array of test cases values
    """
    logger.debug("Calling the get_test_cases with a following parameter: " + path)  

    content = get_file_content(path)
    # change format of test_cases from string to array
    content_array = literal_eval(content)
    return content_array

def get_executable_template(framework, preparator_output_file):
    """
    The entry method for this module
    """
    logger.debug("Calling the get_template method")

    # get the test cases from a output of preparator module
    test_cases = get_test_cases(preparator_output_file)
    # test_cases = get_test_cases("../test_cases/calls_4/tests_100")

    # get the path of a pre-template which should have been used
    path = get_pre_template_path(framework)
    # call the module corresponding with a pre-template which is going to be used
    create_template(path, framework, test_cases)
