import re


def exclusive_match(pattern, text):
    try:
        regex_text = re.search(pattern, text)[0]
        if regex_text is text:
            return True
    except TypeError:
        return False
    return False
