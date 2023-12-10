import benny


def logic(input_: str):
    pass


def lex(input_: str):
    output = []
    position = benny.Position()
    while position.character <= len(input_):
        current_character = input_[position.character]
        match current_character:
            case _ if current_character in benny.text.whitespace:
                if current_character == "\n":
                    position.increment_line()



if __name__ == "__main__":
    lex("12")
