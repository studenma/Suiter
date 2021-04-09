import requests
import logging
logger = logging.getLogger(__name__)

from exceptions import *
import suiter_classes_and_globals as globe
from general import replace_the_tag_with_value

def evaluate_combine_response(response, taged_string, tag):
    """
    Evaluate the response from combine -> replace the values in taged string for each test_case and 
    create an araray oyt of all of these
    """
    endpoint_cases = []

    for test_case in response:
        tmp_taged_string = taged_string
        # print(test_case)
        value_idx = 0
        while len(test_case) > 0:
            value = test_case.pop(0)
            tmp_taged_string = replace_the_tag_with_value(tmp_taged_string, tag, str(value), 0)
            value_idx+=1
        endpoint_cases.append(tmp_taged_string)

    return endpoint_cases


def api_call_combine():
    """
    REST API call to combine
    """
    logging.debug('Calling call_combine function')

    # get the information of request
    url = globe.combine_request.url
    header = globe.combine_request.header
    body = globe.combine_request.body

    try:
        response = requests.request("GET", url, headers=header, json=body)
        # if proxy error
        if response.status_code == 502:
            # try to call it 5 more times
            for _ in range(5):
                response = requests.request("GET", combine_url, headers=headers, json=combine_body)
                # if some of the request is not Proxy error, break this loop and do not call combine anymore
                if response.status_code != 502:
                    break
        if response.status_code == 200:
            """
            Some of the suiter variables have to be reseted
            """
            globe.combine_request = None
            globe.param_id_counter = 0
            globe.all_parameters = []
            # return the response
            return response.json()
        else:
            message = 'Combine status code is not 200'
            raise CombineCallError(__name__, "", message)
    except ValueError: # includes json.decoder.JSONDecodeError
        message = 'Response from Combine is not in a valid JSON format'
        raise CombineCallError(__name__, "", message)

def add_parameter_to_combine_call(parameter):
    """
    Add a given parameter to the prepared global combine class
    """
    logging.debug('Calling add_parameter_to_combine_call function')

    combine_block_array = []
    # prepare identificator
    identificator = 'id_' + str(parameter['id'])
    
    # prepare value_array (different for enum, integer,..)
    # TODO: what if there are different types of values in one array -> so far, only the first element of an array is evaluated
    parameter_values_type = type(parameter['content'][0])
    if parameter_values_type is str:
        parameter_values_type = 'enum'
        combine_block_array = parameter['content']
    elif parameter_values_type is int:
        parameter_values_type = 'integer'
        for element in parameter['content']:
            element = identificator + "=" + str(element)
            combine_block_array.append(element)
    else:
        print("Another data types are not supported yet")
        exit(2)

    new_param = {
        "identificator": identificator,
        "type": parameter_values_type,
        "blocks": combine_block_array
    }
    globe.combine_request.body['parameters'].append(new_param)
    

def create_combine_call(param_array):
    """
    Prepare the combine call with a default header and url values
    Body has to be retrieved from a given parameter array
    """
    logging.debug('Calling prepare_combine_call function')

    # create the combine class with a defined header and url values
    globe.combine_request = globe.CombineCallClass()