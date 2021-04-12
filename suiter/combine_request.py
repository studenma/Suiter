import requests
import logging
logger = logging.getLogger(__name__)

from exceptions import *
import suiter_classes_and_globals as globe
from general import replace_the_tag_with_value

def evaluate_combine_response(response, str_and_array, tag, location, global_variables):
    """
    Evaluate the response from combine -> replace the values in taged string for each test_case and 
    create an araray oyt of all of these
    """
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(response)
    print(str_and_array)
    print(tag)
    print(location)
    print(global_variables)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    taged_string = str_and_array[0]
    list_of_parameters_in_string = str_and_array[1]

    endpoint_cases = []
    tc_idx = 0
    for test_case in response:
        tmp_taged_string = taged_string
        tmp_list_of_parameters_in_string = list_of_parameters_in_string.copy()
        local_globes = {}
        # while there are some values in list of all params
        while len(tmp_list_of_parameters_in_string) > 0:
            parameter = tmp_list_of_parameters_in_string.pop(0)
            # if the combine is called with endpoint and url locations, the param array would't be empty at the end
            if parameter['location'] == location:
                # if the next param is global variable
                if parameter['type'] == 'global_variable':
                    ############################# this part was added from main
                    if len(global_variables) != 0:
                        if parameter['name'] in global_variables[tc_idx].keys():
                            value = global_variables[tc_idx][parameter['name']]
                    #############################
                    # check if the value is already set
                    elif parameter['name'] in local_globes.keys():
                        # value should be taken from globe
                        value = local_globes[parameter['name']]
                    else:
                        # if not, the value should be poped from a combine response and saved as a global varaible with this name
                        value = test_case.pop(0)
                        local_globes[parameter['name']] = value
                    tmp_taged_string = replace_the_tag_with_value(tmp_taged_string, tag, str(value), 0)
                else:
                    # otherwise, the value should be poped from a combine response a replaced in string
                    value = test_case.pop(0)
                    tmp_taged_string = replace_the_tag_with_value(tmp_taged_string, tag, str(value), 0)
        # check if the test_case array is empty and the param array is empty as well
        # TODO: this was removed to support global call as well -> in local call it worked well -> all arrays was empty, but if there are more parts in response, there will be some parameteres of course
        # if len(test_case) != 0 and len(parameter) != 0:
        #     raise ShouldHaveNotGottenHereError(__name__, "evaluate_combine_response")
        endpoint_cases.append((tmp_taged_string, local_globes))
        tc_idx+=1

    return endpoint_cases


def api_call_combine(combine_info):
    """
    REST API call to combine
    """
    logging.debug('Calling call_combine function')

    # get the information of request
    url = combine_info.url
    header = combine_info.header
    body = combine_info.body

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
            if combine_info == globe.combine_request:
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
        raise CombineCallError(__name__, "api_call_combine", message)

def add_array_to_a_combine_call(array_of_values, combineClass, identificator):
    """ add a array of values to the global combine call """    
    new_param = {
        "identificator": identificator,
        "type": "enum",
        "blocks": array_of_values
    }
    combineClass.body['parameters'].append(new_param)

def add_indexes_of_parameter_to_combine_call(parameter, combineClass):
    """
    Add an index of parameter to the combine call
    """
    None
    # combine_block_array = []
    # # prepare identificator
    # identificator = 'id_' + str(parameter['id'])

    # # check if there is a reserved global variable - should not be added to combine request, but it is neccessary to replace it afterwards
    # if 'reserved' in parameter.keys() and parameter['reserved'] == True and parameter['type'] == 'global_variable':
    #     return
    
    # new_param = {
    #     "identificator": identificator,
    #     "type": parameter_values_type,
    #     "blocks": combine_block_array
    # }
    
    # combineClass.body['parameters'].append(new_param) 

def add_parameter_to_combine_call(parameter, combineClass):
    """
    Add a given parameter to the prepared global combine class
    """

    combine_block_array = []
    # prepare identificator
    identificator = 'id_' + str(parameter['id'])

    # check if there is a reserved global variable - should not be added to combine request, but it is neccessary to replace it afterwards
    if 'reserved' in parameter.keys() and parameter['reserved'] == True and parameter['type'] == 'global_variable':
        return
    
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
    
    combineClass.body['parameters'].append(new_param)
    

def create_combine_call():
    """
    Prepare the combine call with a default header and url values
    Body has to be retrieved from a given parameter array
    """
    logging.debug('Calling prepare_combine_call function')

    # create the combine class with a defined header and url values
    globe.combine_request = globe.CombineCallClass()