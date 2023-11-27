import benny.text.style


def escape_codify_char(char):
    match char:
        case "\n":
            return "\\n"
        case "\t":
            return "\\t"
        case _:
            return char
