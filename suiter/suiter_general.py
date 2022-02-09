"""
This module provides general functions used in all other modules 
"""
import re
import logging
logger = logging.getLogger(__name__)

from suiter_exceptions import *

def replace_the_tag_with_value(taged_string, tag, content, nth):
    """ 
    TODO:
    Pozor, content muze byt jak string, tak array with one value 
    check if the key in string even exist -> always replace the first occurence
    """
    if type(content) is list:
        # transfer it to string
        if len(content) == 1:
            content = str(content[0])
        else:
            raise ShouldHaveNotGottenHereError(__name__, "replace_the_tag_with_value")
    elif type(content) is str:
        content = content
    else:
        raise ShouldHaveNotGottenHereError(__name__, "replace_the_tag_with_value")

    # replace the nth occurence in taged string
    if nth < 0: 
        raise ShouldHaveNotGottenHereError(__name__, "replace_the_tag_with_value")
    try:
        where = [m.start() for m in re.finditer(tag, taged_string)][nth]
        before = taged_string[:where]
        after = taged_string[where:]
        after = after.replace(tag, content, 1)
        new_string = before + after
        return new_string
    except:
        raise LimitExceededError(__name__, "replace_the_tag_with_value", "This string does not contain nth ({}) occurence".format(nth))

def get_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except:
        message = 'The file could not be opened: {}'.format(file_path)
        raise OpenFileError(__name__, "get_file_content", message)

def verify_tway_value(tway_value, number_of_parameteres):
    """ 
    Verify if the value of t_way does make sense in comparison with number of parameters
    """
    if tway_value < 1 or tway_value > 6:
        message = "T-way value has to be in following range: <1,6>"
        raise InputFileError(__name__, "verify_tway_value", message)
    # tway value has to be less or equal to nubmer of parameters
    if tway_value > number_of_parameteres:
        if number_of_parameteres != 0 and tway_value != 1:
            message = "T-way value has to be less or equal to number of parameters"
            raise InputFileError(__name__, "verify_tway_value", message)

def tag_substring_evaluation(tag1, tag2):
    """
    Return a more important tag:
        if the first variable is the substring of the second one: return tuple (tag2,tag1)
        if the second variable is the substring of the first one: return tuple (tag1,tag2)
    Return None if none of them are substrings
    """
    if tag1 == tag2:
        message = "The start tag '{}' and it's end '{}' can not be the same".format(tag1,tag2)
        raise ConfigurationFileError(__name__, "conf_variabletag_substring_evaluation_substring_evaluation", message)
    elif tag1 in tag2:
        return (tag2,tag1)
    elif tag2 in tag1:
        return (tag1,tag2)
    else:
        None

def get_header_from_file(header_path):
    """ 
    Get the headers from a input file
    """
    logger.debug("calling the get_header_from_file method with following parameter: " + header_path)
    
    try:
        f = open(header_path, 'r')
    except:
        message = "Could not open a header file: " + header_path
        raise OpenFileError(__name__, "get_header_from_file", message)

    header_dict = {}
    for line in f:
        header = line.split(":", 1)
        head = header[0].rstrip(' ')
        value = header[1].rstrip('\n').lstrip()
        header_dict[head] = value
    f.close()
    return header_dict

def yes_or_no(message):
    """ Ask user if he really wants to continue """
    while "the answer is invalid":
        reply = str(input(message+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False