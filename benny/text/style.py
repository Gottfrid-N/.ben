import re


def pascal_case(text):
    # PascalCase
    if re.match("^([A-Z0-9][a-z0-9]*)+", text):
        return True


def camel_case(text):
    # camelCase
    if re.match("^([a-z0-9]+)+([A-Z0-9][a-z0-9]*)*", text):
        return True


def snake_case(text):
    # snake_case
    if re.match("[A-Z]", text):
        return True


def screaming_snake_case(text):
    # SCREAMING_SNAKE_CASE
    if not re.match("[a-z]", text):
        return True
