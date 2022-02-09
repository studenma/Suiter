"""
This module contains the functions devoted to provide functionality of combine request and evaluating it's response.
"""

import requests
import logging
logger = logging.getLogger(__name__)

from suiter_exceptions import *
import suiter_classes_and_globals as globe
from suiter_general import replace_the_tag_with_value

def api_call_combine(combine_info):
    """
    Combine API request to get the combinations of parameters
    """
    logging.debug('Calling call_combine function')

    """
    Get the data describing the combine request
    """
    url = combine_info.url
    header = combine_info.header
    body = combine_info.body

    """ 
    Check if there are at least 2 parameters to be combined 
    """
    if len(body['parameters']) < 2:
        message = "Cannot combine single parameter"
        raise CombineCallError(__name__, "api_call_combine", message)
    """
    Check if each parameter has at least two values
    """
    for parameter in body['parameters']:
        if len(parameter['blocks']) < 2:
            message = "Cannot combine a parameter with single value"
            raise CombineCallError(__name__, "api_call_combine", message)
    try:
        # make a request
        response = requests.request("POST", url, headers=header, json=body)
        if response.status_code == 502:
            """
            Proxy error 502 
            Sometimes, this response is returned for some reason
            Workaround: if 502 is returned -> try to call it 5 more times
            """
            for _ in range(5):
                response = requests.request("POST", url, headers=header, json=body)
                if response.status_code != 502:
                    # if some of the response is not 502, break this loop and do not call combine again
                    break
        if response.status_code == 200:
            """
            The combine request is OK (200)
            """
            # Some of the suiter variables have to be reseted
            globe.combine_request = None
            globe.param_id_counter = 0
            globe.all_parameters = []
            return response.json()
        else:
            message = 'Combine status code is not 200'
            raise CombineCallError(__name__, "", message)
    except ValueError: # includes json.decoder.JSONDecodeError
        message = 'Response from Combine is not in a valid JSON format'
        raise CombineCallError(__name__, "api_call_combine", message)

def evaluate_combine_response(response, str_and_array, tag, location):
    """
    Evaluate the response from combine
    * replace the values in tagged string for each test_case 
    * create an array out of all of these
    """
    tagged_string = str_and_array[0]
    list_of_parameters_in_string = str_and_array[1]
    endpoint_cases = []
    """
    Iterate over all test cases in combine response
    """
    for test_case in response:
        # create a shallow copy of tagged string and shallow copy of array with all parameters
        temp_tagged_string = tagged_string
        tmp_list_of_parameters_in_string = list_of_parameters_in_string.copy()
        # every testcase has it's own 'local' variables
        local_variables = {}
        while len(tmp_list_of_parameters_in_string) > 0:
            """
            While there are some values in array of all parameters
            The elements are poped ou of this array one by one
            """
            parameter = tmp_list_of_parameters_in_string.pop(0)

            # if the combine is called with endpoint and url locations, the param array would't be empty at the end
            """
            Evaluate only the parameters with the same context it is called
            It is called in endpoint, method, header or body evaluation
            """
            if parameter['location'] == location:
                if parameter['type'] == 'global_variable':
                    """
                    If the parameter is global variable, check if the value is already evaluated
                    """
                    if parameter['name'] in local_variables.keys():
                         # Variable name already does exist in local_variables -> the value should be taken from here
                        value = local_variables[parameter['name']]
                    else:
                        # Variable name was not evaluated yet -> it has to be poped out of the combine response array 
                        value = test_case.pop(0)
                        # Store this variable and its value into test case's local_variables
                        local_variables[parameter['name']] = value
                    # TODO: Should it be transfered into string?
                    # replace the tag in tagged string with its value
                    temp_tagged_string = replace_the_tag_with_value(temp_tagged_string, tag, str(value), 0)
                else:
                    """
                    Local variable or Enumerate
                    The value should have been poped out of the combine response
                    """
                    value = test_case.pop(0)
                    # replace the tag in tagged string with its value
                    temp_tagged_string = replace_the_tag_with_value(temp_tagged_string, tag, str(value), 0)
        endpoint_cases.append((temp_tagged_string, local_variables))
    return endpoint_cases

def add_array_to_a_combine_call(array_of_values, combineClass, identificator):
    """ 
    Append a new parameter block into combine request
    The values are stored in array
    """    
    new_param = {
        "identificator": identificator,
        "type": "enum",
        "blocks": array_of_values
    }
    combineClass.body['parameters'].append(new_param)

def add_parameter_to_combine_call(parameter, combineClass):
    """
    Append a new parameter block into combine request
    Parameter is passed to this function in following format:
        * {"location": "header", 'type': 'enumerate', 'content': [header1.yaml,header2.yaml], 'id': 3}
    Only the integers are passed to a combine as a int -> all other data types are passed as a 'enum'
    """
    combine_block_array = []
    identificator = 'id_' + str(parameter['id'])

    """
    Check if the variable name is already reserved - should not be added to combine request, but it is neccessary to replace it afterwards
    It should have not gotten here, so error is raised
    """
    if (parameter['type'] == 'global_variable') and ('reserved' in parameter.keys()) and (parameter['reserved'] == True):
        raise ShouldHaveNotGottenHereError(__name__, "add_parameter_to_combine_call")
    
    """
    Prepare the parameter's block
    * get the type of a block
    * prepare the array of values to have it in a correct format (different for intereger and enum)
    """
    parameter_content_type = type(parameter['content'][0])
    if parameter_content_type is str:
        """ STRING """
        parameter_content_type = 'enum'
        combine_block_array = parameter['content']
    elif parameter_content_type is int:
        """ INTEGER """
        parameter_content_type = 'integer'
        for element in parameter['content']:
            element = identificator + "=" + str(element)
            combine_block_array.append(element)
    else:
        print("Another data types are not supported yet")
        raise ShouldHaveNotGottenHereError(__name__, "add_parameter_to_combine_call")

    new_param = {
        "identificator": identificator,
        "type": parameter_content_type,
        "blocks": combine_block_array
    }
    
    combineClass.body['parameters'].append(new_param)

def create_combine_call():
    """
    Prepare the combine call with a default header and url values
    """
    logging.debug('Calling prepare_combine_call function')
    globe.combine_request = globe.CombineCallClass()