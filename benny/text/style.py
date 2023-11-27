import re


def exclusive_match(pattern, text):
    try:
        regex_text = re.search(pattern, text)[0]
        if regex_text is text:
            return True
    except TypeError:
        return False
    return False


def pascal_case(text):
    # PascalCase
    return exclusive_match("^([A-Z0-9][a-z0-9]*)+", text)


def camel_case(text):
    # camelCase
    return exclusive_match("^([a-z0-9]+)+([A-Z0-9][a-z0-9]*)*", text)


def snake_case(text):
    # snake_case
    return exclusive_match("^([a-z0-9]+)(_[a-z0-9]+)*", text)


def screaming_snake_case(text):
    # SCREAMING_SNAKE_CASE
    return exclusive_match("^([A-Z0-9]+)(_[A-Z0-9]+)*", text)
