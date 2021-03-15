"""
This module creates an resulted test suite for python

*** Input ***
Input has a following strucure (the result of input_parser module):
[  
    [ 
        ["http://127.0.0.1:5000/api/v1/calculator1","GET","header1.yaml","body1.json"],
        ["http://127.0.0.1:5000/api/v1/calculator2","GET","header1.yaml","body2.json"],
        ["http://127.0.0.1:5000/api/v1/calculator3","GET","header1.yaml","body3.json"]
    ],
    [
        ["http://127.0.0.1:5000/api/v1/calculator","GET","header1.yaml","body1.json"],
        ["http://127.0.0.1:5000/api/v1/calculator","GET","header1.yaml","body2.json"],
        ["http://127.0.0.1:5000/api/v1/calculator","GET","header1.yaml","body3.json"]
    ],
    [
        ["http://127.0.0.1:5000/api/v1/calculator","GET","header1.yaml","body1.json"],
        ["http://127.0.0.1:5000/api/v1/calculator","GET","header1.yaml","body2.json"],
        ["http://127.0.0.1:5000/api/v1/calculator","GET","header1.yaml","body3.json"]
    ]
]

*** Output ***
The test suite for python
"""

from input_parser import get_test_cases
from input_parser import get_header_from_file
from exceptions import OpenFileError
from textwrap import indent

import logging 
logger = logging.getLogger(__name__)

tab = "    "
call_identifier = "call_"
test_case_identifier = "test_case_"

def prepare_verify_tag(tc):
    """
    Prepare the text which should replace <VERIFY> tag in pre-template
    """
    logger.debug("Calling the prepare_verify_tag method")

    result = ""
    test_case_counter = 1
    for test_case in tc:
        # get the number of calls in the test case
        call_cnt = len(test_case)

        if test_case_counter == 1:
            result += indent("if test_case == \"{}\":\n".format(test_case_identifier + str(test_case_counter)), tab)
        else:
            result += indent("elif test_case == \"{}\":\n".format(test_case_identifier + str(test_case_counter)), tab)
        block = []
        block.append('#####################################\n')
        block.append('# TODO: HERE IS YOUR CODE TO PREDEFINE ALL TEST CASE VERIFICATION\n')
        block.append('# example:\n')
        block.append('## statusCode = None\n')
        block.append('## json = {\'Result\': None}\n')
    
        if call_cnt > 1:
            for call_idx in range(1, call_cnt):
                if call_idx == 1:
                    new_line = indent("if request_id == \"{}\":\n".format(call_identifier + str(call_idx)), 2*tab)
                else:
                    new_line = indent("elif request_id == \"{}\":\n".format(call_identifier + str(call_idx)), 2*tab)
                result += new_line
                for line in block:
                    line = indent(line, 3*tab)
                    result += line
        else:
            for line in block:
                line = indent(line, 2*tab)
                result += line
        test_case_counter += 1
    
    return result

def prepare_test_case_list_tag(tc):
    """
    Prepare the text which should replace <TEST_CASE_LIST> tag in pre-template
    """
    logger.debug("Calling the prepare_test_case_list_tag method")

    result = ""
    test_case_counter = 1
    for test_case in tc:
        # get the number of calls in the first test_case
        call_cnt = len(test_case)
        
        if test_case_counter == 1:
            result += indent("if test_case == \"{}\":\n".format(test_case_identifier + str(test_case_counter)), tab)
        else:
            result += indent("elif test_case == \"{}\":\n".format(test_case_identifier + str(test_case_counter)), tab)
        
        if call_cnt > 1:
            for call_idx in range(call_cnt):
                if call_idx == 0:
                    new_line = indent("if request_id == \"req" + str(call_idx+1) + "\":\n", 2*tab)
                else:
                    new_line = indent("elif request_id == \"req" + str(call_idx+1) + "\":\n", 2*tab)
                result += new_line
                # URL
                new_line = indent("url = \"" + str(test_case[call_idx][0]) + "\"\n", 3*tab)
                result += new_line
                # METHOD
                new_line = indent("method = \"" + str(test_case[call_idx][1]) + "\"\n", 3*tab)
                result += new_line
                # HEADER
                header = get_header_from_file(test_case[call_idx][2])
                new_line = indent("header = " + str(header) + "\n", 3*tab)
                result += new_line
                # BODY
                new_line = indent("body = \"" + str(test_case[call_idx][3]) + "\"\n", 3*tab)
                result += new_line
        else:
            # URL
            new_line = indent("url = \"" + str(test_case[0][0]) + "\"\n", 2*tab)
            result += new_line
            # METHOD
            new_line = indent("method = \"" + str(test_case[0][1]) + "\"\n", 2*tab)
            result += new_line
            # HEADER
            header = get_header_from_file(test_case[0][2])
            new_line = indent("header = " + str(header) + "\n", 2*tab)
            result += new_line
            # BODY
            new_line = indent("body = \"" + str(test_case[0][3]) + "\"\n", 2*tab)
            result += new_line     
        test_case_counter += 1
    return result

def prepare_requests_tag(test_case):
    """
    Prepare the text which should replace <REQUESTS> tag in pre-template
    """
    logger.debug("Calling the prepare_requests_tag method")

    # get the number of calls in the first test_case
    call_cnt = len(test_case)
    
    result = ""

    for call_idx in range(1, call_cnt+1):
        call_tag = 'call' + str(call_idx)
        
        # each element represents a new line
        block = []
        block.append('\"\"\"')
        block.append('{}. Request'.format(call_idx))
        block.append('\"\"\"')
        block.append('# execution')
        block.append('call = list_of_all_cases(test_case_id, \"{}\")'.format(call_tag))
        block.append('response = requests.request(call[1], call[0], headers=call[2], data=dumps(call[3]))')
        block.append('# request verification')
        block.append('expected_response = verify(test_case_id, \"{}\")'.format(call_tag))
        block.append('#####################################')
        block.append('# TODO: HERE MAY BE YOUR ASSERTIONS')
        block.append('# delete this part otherwise')
        block.append('# the assertions have to be based on \'expected_response\' variable')
        block.append('# example:')
        block.append('# assert response.status_code == expected_response.status_code')
        block.append('# assert response.json() == expected_response.json')
        
        for line in block:
            result += indent(line + "\n", 2*tab)
        result += "\n"
    return result

def prepare_verification_tag(test_case):
    result = ""

    block = []
    block.append('\"\"\"')
    block.append('SUT Verification')
    block.append('\"\"\"')
    block.append('result = verify(test_case_id, "sut")')
    block.append('#####################################')
    block.append('# TODO: HERE MAY BE YOUR ASSERTIONS')
    block.append('# delete this part otherwise')
    block.append('# the assertions have to be based on \'result\' variable')
        
    for line in block:
        result += indent(line + "\n", 2*tab)

    return result

def fill_the_pre_template(path, tc):
    """
    Fill the tags in pre-template with a values for the first test case 
    Output: New file created - containing the executable template with the first test cases
    """
    logger_message = "Calling the fill_the_pre_template method with following parameters: [{}, {}]".format(path,tc)
    logger.debug(logger_message)

    # Open file for reading only
    try:
        f = open(path, 'r')
    except:
        message = "Could not read a pre-template file: " + path
        raise OpenFileError(__name__, "fill_the_pre_template", message)

    # replace the tags with values and store it in the 'new_file_content' variable
    new_file_content = ""
    for line in f:
        if '<VERIFY>' in line:
            new_line = prepare_verify_tag(tc)
            new_file_content += line.replace('<VERIFY>', new_line)
        elif '<TEST_CASE_LIST>' in line:
            print(tc)
            new_line = prepare_test_case_list_tag(tc)
            new_file_content += line.replace('<TEST_CASE_LIST>', new_line)
        elif '<REQUESTS>' in line:
            new_line = prepare_requests_tag(tc)
            new_file_content += line.replace('<REQUESTS>', new_line)
        elif '<VERIFICATION>' in line:
            new_line = prepare_verification_tag(tc)
            new_file_content += line.replace('<VERIFICATION>', new_line)
        else:
            # if all test cases should be generated, the duplicate tag is not needed anymore
            if ('<DUPLICATE>' in line) or ('</DUPLICATE>' in line):
                if len(tc) == 1:
                    new_file_content += line
            else:
                new_file_content += line
    
    # close file
    f.close() 
    
    # open and write into a file the new content
    f = open('./result/template.py', 'w')
    f.write(new_file_content)
    f.close()


def create_template(content, tc):
    """
    Based on a content of pre-template creates a executable template for user
    """
    logger.debug('Calling the create_template method')

    fill_the_pre_template(content, tc)