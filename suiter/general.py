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
