"""
This module provides a functions to parse a given input json file. 
Also, some other functions related with parsing of an user's input are defined here.
"""

import json
import configparser
import logging
logger = logging.getLogger(__name__)
from suiter_classes_and_globals import ConfigDataClass
from suiter_exceptions import *

def create_default_config(file_path):
    """ change the configuration values - used for testing purposes """
    config = configparser.ConfigParser()
    config['ENDPOINT'] = {
        'url_enum_start': '<',
        'url_enum_end': '>',
        'url_enum_separator': ',',
        'url_variable_start': '<:',
        'url_varaible_end': ':>'
    }
    config['METHOD'] = {
        'method_enum_start': '<',
        'method_enum_end': '>',
        'method_enum_separator': ',',
        'method_variable_start': '<:',
        'method_variable_end': ':>'
    }
    config['HEADER'] = {
        'header_enum_start': '<',
        'header_enum_end': '>',
        'header_enum_separator': ',',
        'header_variable_start': '<:',
        'header_variable_end': ':>'
    }
    config['BODY'] = {
        'body_enum_start': '<',
        'body_enum_end': '>',
        'body_enum_separator': ',',
        'inside_body_separator': ';',
        'body_variable_start': '<:',
        'body_variable_end': ':>'
    }
    config['GENERAL'] = {
        'default_framework': "Pytest",
        'default_input_file': "../input/input_file.json",
        'default_output_folder': "./result/"
    }
    config['COMBINATION_LIMIT'] = {
        'final_tc_limit': "150"
    }
    with open(file_path, 'w') as configfile:
        config.write(configfile)

def read_config_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return ConfigDataClass(config)

def open_input_json_file(file_path):
    """
    Open an input json file located in a given path.
    The content of this file is returned
    """
    logging.debug('Trying to open a input json file. Given file path is: {}'.format(file_path))
    try:
        with open(file_path) as json_file:
            file_content = json.load(json_file)
    except ValueError:
        message = "The given file is not a json."
        raise InputFileError(__name__, "input_file_parser", message)
    except:
        message = "Could not open an input json file"
        raise OpenFileError(__name__, "input_file_parser", message)
    return file_content

def input_json_structure_validator(json_content):
    """ 
    Check if the given content of an input json file is valid
    Output: 
    * for valid:    (True, "")
    * for invalid:  (False, ErrorMessage)
    """
    logger.debug("Validating the content of given json file")

    """ FIRST LEVEL
    Should contain only with following keys:
    * 'test_sequence' - API calls description
    * 'global_params' - global parameters description
    * 't-way' - the stregth of a T-way on test sequence level 
            (after combining all API calls, also the combination of them has to be done)
    """
    logger.debug("Validating of a first level")
    mandatory_first_level_keys = ['test_sequence', 'global_params']
    optional_first_level_keys = ['t-way']
    first_level_input_keys = json_content.keys()
    for element in mandatory_first_level_keys:
        if element not in first_level_input_keys:
            message = "The '{}' element was not found in input json file".format(element) 
            return False,message
    for element in first_level_input_keys:
        if (element not in mandatory_first_level_keys) and (element not in optional_first_level_keys):
            message = "The '{}' element is not allowed to be in the first level of input json file".format(element) 
            return False,message

    """ TEST SEQUENCE
    """
    logger.debug("Validating of a test sequence element")
    # test_sequence have to be an array
    if type(json_content['test_sequence']) is not list:
        message = "The 'test_sequence' key in the input json file was expected to be a list, but the {} is given".format(type(json_content['test_sequence']))
        return False,message
    # test_sequence cannot be empty
    test_case_array_length = len(json_content['test_sequence'])
    if test_case_array_length == 0:
        message = "The test_sequence array is empty"
        return False,message
    # following keys have to exist in every sequence call
    call_keys_mandatory = ['endpoint', 'method', 'header', 'body', 't-way']
    call_keys_optional = ['allow_duplicities', 'all-in-one-test']
    allowed_methods = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE"]
    """ iterate over all calls in test_sequence """
    for idx in range(test_case_array_length):
        # is dict?
        if type(json_content['test_sequence'][idx]) is not dict:
            message = "The test_sequence[{}] is not a dict".format(idx)
            return False,message
        # check mandatory call keys
        for element in call_keys_mandatory:
            if element not in json_content['test_sequence'][idx].keys():
                message = "The '{}' element was not found in call keys in input file".format(element) 
                return False,message
        # check any other call keys
        for element in json_content['test_sequence'][idx].keys():
            if (element not in call_keys_mandatory) and (element not in call_keys_optional):
                message = "The '{}' element is not supported".format(element) 
                return False,message
            if element in call_keys_optional:
                el_type = type(json_content['test_sequence'][idx][element])
                if el_type is not int:
                    message = "The '{}' element is expected to be a integer, {} is given".format(element,el_type) 
                    return False,message
        # check if t-way is integer
        tway_type = type(json_content['test_sequence'][idx]['t-way'])
        if tway_type is not int:
            message = "The 't-way' element is expected to be a integer, {} is given".format(tway_type) 
            return False,message
        """
        ENDPOINT
        """
        # check if endpoint is a dict
        if type(json_content['test_sequence'][idx]['endpoint']) is not dict:
            message = "The endpoint element is not a json_content"
            return False,message
        # check mandatory endpoint keys
        endpoint_keys_mandatory = ['values', 'local_params']
        endpoint_keys_optional = ['t-way', 'allow-duplicities']
        for element in endpoint_keys_mandatory:
            if element not in json_content['test_sequence'][idx]['endpoint'].keys():
                message = "The '{}' element was not found in endpoint json_content".format(element) 
                return False,message
        # check all endpoint keys
        for element in json_content['test_sequence'][idx]['endpoint'].keys():
            if (element not in endpoint_keys_mandatory) and (element not in endpoint_keys_optional):
                message = "The '{}' element is not supported".format(element) 
                return False,message
            # all optional keys should be integers
            if element in endpoint_keys_optional:
                el_type = type(json_content['test_sequence'][idx]['endpoint'][element])
                if el_type is not int:
                    message = "The '{}' element does not have a valid type: expected: integer, {} is given".format(element, el_type) 
                    return False,message         
        # check local_param is array
        local_params_type = type(json_content['test_sequence'][idx]['endpoint']['local_params'])
        if local_params_type is not list:
            message = "The local_params element is not a json_content, but {}".format(local_params_type) 
            return False,message
        # check if value is string
        url_type = type(json_content['test_sequence'][idx]['endpoint']['values'])
        if url_type is not str:
            message = "The values element in endpoint is not a string, but {}".format(url_type) 
            return False,message
        """
        METHOD
        """
        # check if method is a dict
        method_type = type(json_content['test_sequence'][idx]['method'])
        if method_type is not dict:
            message = "The method element is not a json_content, but {}".format(method_type)
            return False,message
        # check mandatory method keys
        method_keys_mandatory = ['values', 'local_params']
        method_keys_optional = [] # there are no optional keys in method
        for element in method_keys_mandatory:
            if element not in json_content['test_sequence'][idx]['method'].keys():
                message = "The '{}' element was not found in method json_content".format(element) 
                return False,message
        # check all method keys
        for element in json_content['test_sequence'][idx]['method'].keys():
            if (element not in method_keys_mandatory) and (element not in method_keys_optional):
                message = "The '{}' element is not supported".format(element) 
                return False,message
            # all optional keys should be integers
            if element in method_keys_optional:
                el_type = type(json_content['test_sequence'][idx]['method'][element])
                if el_type is not int:
                    message = "The '{}' element does not have a valid type: expected: integer, {} is given".format(element, el_type) 
                    return False,message 
        # method value type check
        method_val_type = type(json_content['test_sequence'][idx]['method']['values'])
        if method_val_type is not str:
            message = "The value element in method is not a string, but {}".format(method_val_type) 
            return False,message  
        """
        HEADER
        """
        # header
        header_type = type(json_content['test_sequence'][idx]['header'])
        if header_type is not dict:
            message = "The header is not a dict, but {}".format(header_type)
            return False,message
        # check mandatory header keys
        header_keys_mandatory = ['values', 'local_params']
        header_keys_optional = ['t-way']
        for element in header_keys_mandatory:
            if element not in json_content['test_sequence'][idx]['header'].keys():
                message = "The '{}' element was not found in header json_content".format(element) 
                return False,message
        # check all header keys
        for element in json_content['test_sequence'][idx]['header'].keys():
            if (element not in header_keys_mandatory) and (element not in header_keys_optional):
                message = "The '{}' element is not supported".format(element) 
                return False,message
            # all optional keys should be integers
            if element in header_keys_optional:
                el_type = type(json_content['test_sequence'][idx]['header'][element])
                if el_type is not int:
                    message = "The '{}' element does not have a valid type: expected: integer, {} is given".format(element, el_type) 
                    return False,message 
        # check local_param is array
        local_params_type = type(json_content['test_sequence'][idx]['header']['local_params'])
        if local_params_type is not list:
            message = "The local_params element is not a json_content, but {}".format(local_params_type) 
            return False,message
        # header value should be dictionary or string
        header_value_type = type(json_content['test_sequence'][idx]['header']['values'])
        if (header_value_type is not dict) and (header_value_type is not str):
            message = "The header value is not a dict or string, but {}".format(type(element))
            return False,message
        """
        BODY
        """
        body_type = type(json_content['test_sequence'][idx]['body'])
        if body_type is not dict:
            message = "The body is not a dict, but {}".format(body_type)
            return False,message
        # check mandatory body keys
        body_keys_mandatory = ['values', 'local_params']
        body_keys_optional = ['t-way']
        body_keys_optional_boolean = ['value_is_string']
        for element in body_keys_mandatory:
            if element not in json_content['test_sequence'][idx]['body'].keys():
                message = "The '{}' element was not found in body json_content".format(element) 
                return False,message
        # check all body keys
        for element in json_content['test_sequence'][idx]['body'].keys():
            if (element not in body_keys_mandatory) and (element not in body_keys_optional) and (element not in body_keys_optional_boolean):
                message = "The '{}' element is not supported".format(element) 
                return False,message
            # all optional keys should be integers
            if element in body_keys_optional:
                el_type = type(json_content['test_sequence'][idx]['body'][element])
                if el_type is not int:
                    message = "The '{}' element does not have a valid type: expected: integer, {} is given".format(element, el_type) 
                    return False,message 
            # check boolean types
            if element in body_keys_optional_boolean:
                el_type = type(json_content['test_sequence'][idx]['body'][element])
                if el_type is not bool:
                    message = "The '{}' element does not have a valid type: expected: boolean, {} is given".format(element, el_type) 
                    return False,message 
        # check local_param is array
        local_params_type = type(json_content['test_sequence'][idx]['body']['local_params'])
        if local_params_type is not list:
            message = "The local_params element is not a json_content, but {}".format(local_params_type) 
            return False,message
        # body value should be dictionary or string
        body_value_type = type(json_content['test_sequence'][idx]['body']['values'])
        if body_value_type is not str:
            message = "The body value is not a string, but {}".format(body_value_type)
            return False,message
    
    """ GLOBAL PARAMS
    """
    logger.debug("Validating of a global_params element")
    global_params_type = type(json_content['global_params'])
    if global_params_type is not dict:
        message = "The global_params is not a json_content, but {}".format(global_params_type)
        return False,message
    for element in json_content['global_params']:
        el_type = type(json_content['global_params'][element])
        if el_type is not list:
            message = "The global_params's element {} is not a array, but {}".format(element, el_type)
            return False,message
    for element in json_content['global_params']:
        # empty array is not allowed
        variable_array_len = len(json_content['global_params'][element])
        if variable_array_len < 2:
            message = "The global_params's element {} is empty or there is only one element".format(element)
            return False,message

    """ T-WAY
    """
    logger.debug("Validating of a t-way element")
    
    return True,None