import metalbeard.metalbeard as metalbeard
import metalbeard.bismuth.bismuth as bismuth


#########
# LEXER #
#########
class Lexer:
    def __init__(self, text_input: str):
        self.buffer = metalbeard.StringBuffer()
        self.input = text_input
        self.position = metalbeard.Position()
        self.current_char = None
        self.current_id_open = None
        self.current_id_close = None
        self.advance()

    def advance(self):
        self.position.increment()
        if self.position.character < len(self.input):
            self.current_char = self.input[self.position.character]
        else:
            self.current_char = None

    def lex(self):
        output = []

        while self.current_char is not None:
            if self.current_char == "\n":
                self.advance()
                self.position.increment_line()
                continue
            if self.current_char in " \t":
                self.advance()
                continue
            match self.current_char:
                case self.current_id_open:
                    self.advance()
                    while self.current_char != self.current_id_close:
                        if self.current_char == "\\":
                            self.advance()
                        self.buffer.add(self.current_char)
                        self.advance()
                    output.append(metalbeard.Token(metalbeard.TT_ID, "\"" + self.buffer.__str__() + "\""))
                    self.buffer.clear()
                    self.current_id_open = self.current_id_close = None

                case metalbeard.TC_VARIABLE:
                    output.append(metalbeard.Token(metalbeard.TT_VARIABLE, metalbeard.TV_SINGLE))
                    self.current_id_open = self.current_id_close = metalbeard.TC_VARIABLE
                    continue

                case metalbeard.TC_MACRO:
                    output.append(metalbeard.Token(metalbeard.TT_MACRO, metalbeard.TV_SINGLE))
                    self.current_id_open = self.current_id_close = metalbeard.TC_MACRO
                    continue

                case metalbeard.TC_STRING:
                    output.append(metalbeard.Token(metalbeard.TT_STRING, metalbeard.TV_SINGLE))
                    self.current_id_open = self.current_id_close = metalbeard.TC_STRING
                    continue

                case metalbeard.TC_SEPERATOR:
                    output.append(metalbeard.Token(metalbeard.TT_SEPERATOR, metalbeard.TV_SINGLE))

                case metalbeard.TC_SCOPE_OPEN:
                    output.append(metalbeard.Token(metalbeard.TT_SCOPE, metalbeard.TV_OPEN))
                case metalbeard.TC_SCOPE_CLOSE:
                    output.append(metalbeard.Token(metalbeard.TT_SCOPE, metalbeard.TV_CLOSE))

                case metalbeard.TC_GROUP_OPEN:
                    output.append(metalbeard.Token(metalbeard.TT_GROUP, metalbeard.TV_OPEN))
                case metalbeard.TC_GROUP_CLOSE:
                    output.append(metalbeard.Token(metalbeard.TT_GROUP, metalbeard.TV_CLOSE))

                case _:
                    print("Unrecognized Character: " + self.current_char + " at " + self.position.__str__())
            self.advance()
        return output
