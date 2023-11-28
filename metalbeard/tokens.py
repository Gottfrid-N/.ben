import benny
import enum


operators = [
    # Assigning Operators
    "=",  "=+", "=-", "=*", "=/", "=^"
    # Arithmetic Operators
          "+",  "-",  "*",  "/",  "^"
    # Unary Operators
    "!"
    # Binary Operators
    "==", "||", "&&"
]


def character(char):
    return benny.Token("CHARACTER", char)


def assigning_operator(operator_):
    return benny.Token("OPERATOR_ASSIGN", operator_)


def arithmetic_operator(operator_):
    return benny.Token("OPERATOR_ARITHMETIC", operator_)


def boolean_operator(operator_):
    return benny.Token("OPERATOR_BOOLEAN", operator_)


SCOPE_OPEN = benny.Token("SCOPE", "OPEN")
SCOPE_CLOSE = benny.Token("SCOPE", "CLOSE")
SCOPE_SEPERATOR = benny.Token("SCOPE", "SEPERATOR")