from benny.lexer import Lexer
from benny.position import Position
from benny.token import Token


def escape_codify_char(char):
    match char:
        case "\n":
            return "\\n"
        case "\t":
            return "\\t"
        case _:
            return char
