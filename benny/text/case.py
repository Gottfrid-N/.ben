import benny.text.regex as regex


def is_style(expected_style, string):
    if expected_style(string):
        return True
    return False


def pascal_case(string):
    # PascalCase
    return regex.exclusive_match("^([A-Z0-9][a-z0-9]*)+", string)


def camel_case(string):
    # camelCase
    return regex.exclusive_match("^([a-z0-9]+)+([A-Z0-9][a-z0-9]*)*", string)


def snake_case(string):
    # snake_case
    return regex.exclusive_match("^([a-z0-9]+)(_[a-z0-9]+)*", string)


def screaming_snake_case(string):
    # SCREAMING_SNAKE_CASE
    return regex.exclusive_match("^([A-Z0-9]+)(_[A-Z0-9]+)*", string)
