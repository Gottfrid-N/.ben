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
GROUP_OPEN = benny.Token("GROUP", "OPEN")
GROUP_CLOSE = benny.Token("GROUP", "CLOSE")
GROUP_SEPERATOR = benny.Token("GROUP", "SEPERATOR")
METALBEARD_OPEN = benny.Token("METALBEARD", "OPEN")
METALBEARD_CLOSE = benny.Token("METALBEARD", "CLOSE")
