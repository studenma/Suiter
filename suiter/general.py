"""
This module provides general functions used in all other modules 
"""
from exceptions import *
import re

# https://stackoverflow.com/questions/35091557/replace-nth-occurrence-of-substring-in-string
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
        message = 'The file could not be opened'
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



    