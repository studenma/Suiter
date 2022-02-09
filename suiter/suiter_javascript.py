"""
"""
from suiter_general import get_header_from_file
from suiter_exceptions import *
from textwrap import indent

import logging 
logger = logging.getLogger(__name__)

tab = "    "
call_identifier = "call_"
test_case_identifier = "test_case_"

TC_VARIABLE_NAME = "test_case"
CALL_VARIABLE_NAME = "request_id"
TEST_CASE_CNT_START = 1
CALL_CNT_START = 1
EXPECTION_ELSE_MESSAGE = "\"Should have never gotten here: [${{{}}},${{{}}}]\"".format(TC_VARIABLE_NAME, CALL_VARIABLE_NAME)

def prefix_format_calculation(case_amount):
    return "{{0:0{}}}".format(len(str(abs(case_amount))))

def prepare_verify_tag(tc):
    """
    Prepare the text which should replace <VERIFY> tag in pre-template
    """
    logger.debug("Calling the prepare_verify_tag method")

    prefix_format = prefix_format_calculation(len(tc))
    result = ""
    test_case_counter = TEST_CASE_CNT_START
    for test_case in tc:
        # change the test counter number to a format calculated by the number of test cases
        stringified_tc_counter = prefix_format.format(test_case_counter)

        # get the number of calls in the test case
        call_amount = len(test_case)

        if test_case_counter == TEST_CASE_CNT_START:
            result += indent("if({} == \"{}{}\") {{\n".format(TC_VARIABLE_NAME, test_case_identifier, stringified_tc_counter), tab)
        else:
            result += indent("else if({} == \"{}{}\") {{\n".format(TC_VARIABLE_NAME, test_case_identifier, stringified_tc_counter), tab)
        block = []
        block.append('assert.strictEqual(response.statusCode,200);\n')
    
        if call_amount > 1:
            prefix_call_format = prefix_format_calculation(call_amount)
            for call_idx in range(CALL_CNT_START, CALL_CNT_START+call_amount):
                # change the call counter number to a format calculated by the number of calls
                stringified_call_counter = prefix_call_format.format(call_idx)
                if call_idx == CALL_CNT_START:
                    new_line = indent("if({} == \"{}{}\") {{\n".format(CALL_VARIABLE_NAME, call_identifier, stringified_call_counter), 2*tab)
                else:
                    new_line = indent("else if({} == \"{}{}\") {{\n".format(CALL_VARIABLE_NAME, call_identifier, stringified_call_counter), 2*tab)
                result += new_line
                # print the information about request
                result += indent("// Test Case Information\n", 3*tab)
                result += indent("// endpoint = {}\n".format(str(test_case[call_idx-1][0])), 3*tab)
                result += indent("// method = {}\n".format(str(test_case[call_idx-1][1])), 3*tab)
                result += indent("// header = {}\n".format(str(test_case[call_idx-1][2])), 3*tab)
                result += indent("// body = {}\n".format(str(test_case[call_idx-1][3])), 3*tab)
                for line in block:
                    line = indent(line, 3*tab)
                    result += line
                result += indent("}\n",2*tab) 
            # else statement - raise error 
            result += indent("else {\n", 2*tab)
            result += indent("throw new Error({})\n".format(EXPECTION_ELSE_MESSAGE), 3*tab)
            result += indent("}\n", 2*tab)
        else:
            # print the information about request
            result += indent("// Test Case Information\n", 2*tab)
            result += indent("// endpoint = {}\n".format(str(test_case[0][0])), 2*tab)
            result += indent("// method = {}\n".format(str(test_case[0][1])), 2*tab)
            result += indent("// header = {}\n".format(str(test_case[0][2])), 2*tab)
            result += indent("// body = {}\n".format(str(test_case[0][3])), 2*tab)
            for line in block:
                line = indent(line, 2*tab)
                result += line
        result += indent("}\n",tab) 
        test_case_counter += 1

    if len(tc) != 1:
        # else statement - raise error 
        new_line = indent("else {\n", tab)
        new_line += indent("throw new Error({})\n".format(EXPECTION_ELSE_MESSAGE), 2*tab)
        result += new_line
        result += indent("}\n",tab) 
    return result

def prepare_test_case_list_tag(tc):
    """
    Prepare the text which should replace <TEST_CASE_LIST> tag in pre-template
    """
    logger.debug("Calling the prepare_test_case_list_tag method")

    result = ""
    test_case_counter = TEST_CASE_CNT_START
    prefix_format = prefix_format_calculation(len(tc))
    for test_case in tc:
        # change the test counter number to following format: '000'
        stringified_tc_counter = prefix_format.format(test_case_counter)

        # get the number of calls in the first test_case
        call_amount = len(test_case)
        
        if test_case_counter == TEST_CASE_CNT_START:
            result += indent("if({} == \"{}{}\") {{\n".format(TC_VARIABLE_NAME, test_case_identifier, stringified_tc_counter), tab)
        else:
            result += indent("else if( {} == \"{}{}\") {{\n".format(TC_VARIABLE_NAME, test_case_identifier, stringified_tc_counter), tab)
        
        if call_amount > 1:
            prefix_call_format = prefix_format_calculation(call_amount)
            for call_idx in range(CALL_CNT_START, CALL_CNT_START+call_amount):
                # change the call counter number to a format calculated by the number of calls
                stringified_call_counter = prefix_call_format.format(call_idx)

                if call_idx == CALL_CNT_START:
                    new_line = indent("if({} == \"{}{}\") {{\n".format(CALL_VARIABLE_NAME, call_identifier, stringified_call_counter), 2*tab)
                else:
                    new_line = indent("else if({} == \"{}{}\") {{\n".format(CALL_VARIABLE_NAME, call_identifier, stringified_call_counter), 2*tab)
                result += new_line
                # URL
                new_line = indent("url = \"" + str(test_case[call_idx-1][0]) + "\"\n", 3*tab)
                result += new_line
                # METHOD
                new_line = indent("method = \"" + str(test_case[call_idx-1][1]) + "\"\n", 3*tab)
                result += new_line
                # HEADER
                header = test_case[call_idx-1][2]
                new_line = indent("header = " + str(header) + "\n", 3*tab)
                result += new_line
                # BODY
                new_line = indent("body = \"" + str(test_case[call_idx-1][3]) + "\"\n", 3*tab)
                result += new_line
                # parameters 
                result += indent("endpoint_params = []\n", 3*tab)
                result += indent("method_params = []\n", 3*tab)
                result += indent("header_params = []\n", 3*tab)
                result += indent("body_params = []\n", 3*tab)
                result += indent("}\n", 2*tab)
            result += indent("else {\n", 2*tab)
            result += indent("throw new Error({})\n".format(EXPECTION_ELSE_MESSAGE), 3*tab)
            result += indent("}\n", 2*tab)
        else:
            # URL
            new_line = indent("url = \"" + str(test_case[0][0]) + "\"\n", 2*tab)
            result += new_line
            # METHOD
            new_line = indent("method = \"" + str(test_case[0][1]) + "\"\n", 2*tab)
            result += new_line
            # HEADER
            # header = get_header_from_file(test_case[0][2])
            header = test_case[0][2]
            new_line = indent("header = " + str(header) + "\n", 2*tab)
            result += new_line
            # BODY
            new_line = indent("body = \"" + str(test_case[0][3]) + "\"\n", 2*tab)
            result += new_line  
            # parameters 
            result += indent("endpoint_params = []\n", 2*tab)
            result += indent("method_params = []\n", 2*tab)
            result += indent("header_params = []\n", 2*tab)
            result += indent("body_params = []\n", 2*tab)

        result += indent("}\n", tab)   
        test_case_counter += 1

    if len(tc) != 1:
        # else statement - raise error 
        new_line = indent("else {\n", 1*tab)
        new_line += indent("throw new Error({})\n".format(EXPECTION_ELSE_MESSAGE), 2*tab)
        result += new_line
        result += indent("}\n", tab)
    return result

def prepare_sequence_tag(tc):
    """
    Prepare the text which should replace <TEST_SEQUENCE> tag in pre-template
    """
    logger.debug("Calling the prepare_sequence_tag method")

    result = ""
    test_case_counter = TEST_CASE_CNT_START
    prefix_format = prefix_format_calculation(len(tc))
    for test_case in tc:
        # change the test counter number to following format: '000'
        stringified_tc_counter = prefix_format.format(test_case_counter)

        # get the number of calls in the first test_case
        call_amount = len(test_case)

        # each element represents a new line
        
        result += indent("it('test_sequence_{}', function() {{\n".format(stringified_tc_counter), tab)

        # SETUP
        block = []
        block.append('// SUT setup')
        block.append('setup();')

        prefix_call_format = prefix_format_calculation(call_amount)
        for call_idx in range(CALL_CNT_START, CALL_CNT_START+call_amount):
            # change the call counter number to a format calculated by the number of calls
            stringified_call_counter = prefix_call_format.format(call_idx)

            call_tag = call_identifier + stringified_call_counter
            # CALLS
            block.append('// {}. request'.format(stringified_call_counter))
            block.append('req = all_test_cases(\"{}{}\", \"{}\");'.format(test_case_identifier, stringified_tc_counter, call_tag))
            block.append('var options = {')
            block.append('\t\'url\': req.endpoint,')
            block.append('\t\'method\': req.method,')
            block.append('\t\'headers\': req.header')
            block.append('}')
            block.append('request(options, function (error, response) {')
            block.append('\tif (error) throw new Error(error);')
            block.append('\tverify(\"{}{}\", \"{}\", response, req);'.format(test_case_identifier, stringified_tc_counter, call_tag))
            block.append('});')
        
        block.append('// SUT Teardown ')
        block.append('teardown();')

        for line in block:
            result += indent(line + "\n", 2*tab)
        result += indent("});\n", tab)
        result += "\n"
        test_case_counter += 1

    return result

def fill_the_pre_template(path, tc):
    """
    Fill the tags in pre-template with a values for the first test case 
    Output: New file created - containing the executable template with the first test cases
    """
    logger.debug("Calling the fill_the_pre_template method")

    tc_amount = len(tc)

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
            verify_code_block = prepare_verify_tag(tc)
            new_file_content += line.replace('<VERIFY>', verify_code_block)
        elif '<TEST_CASE_LIST>' in line:
            test_case_list_code_block = prepare_test_case_list_tag(tc)
            new_file_content += line.replace('<TEST_CASE_LIST>', test_case_list_code_block)
        elif '<TEST_SEQUENCE>' in line:
            test_sequence_code_block = prepare_sequence_tag(tc)
            new_file_content += line.replace('<TEST_SEQUENCE>', test_sequence_code_block)
        else:
            # if all test cases should be generated, the duplicate tag is not needed anymore
            if ('<DUPLICATE>' in line) or ('</DUPLICATE>' in line):
                if len(tc) == 1: # TODO: Nastavit dle nejakeho togglu z argumentu (muze nastat situace, kdy si budu chtit vygenerovat pouze jeden test)
                    new_file_content += line 
            else:
                new_file_content += line
    f.close() 
    
    # open and write into a file the new content
    f = open('./result/javascript_script.js', 'w')
    f.write(new_file_content)
    f.close()

def create_template(content, tc):
    """
    Entry point of this module
    Based on the pre-template creates a executable template for user
    """
    logger.debug('Calling the create_template method for javaScript')

    """
    Fill in the pre-template with a corresponding values
    """
    fill_the_pre_template(content, tc)