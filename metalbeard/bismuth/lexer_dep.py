import metalbeard
import benny


#########
# LEXER #
#########
class Lexer:
    def __init__(self, text_input: str):
        self.buffer = benny.StringBuffer()
        self.input = text_input
        self.position = benny.Position()
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
                    output.append(benny.Token(metalbeard.tokens.TT_ID, "\"" + self.buffer.__str__() + "\""))
                    self.buffer.clear()
                    self.current_id_open = self.current_id_close = None

                case metalbeard.tokens.TC_VARIABLE:
                    output.append(benny.Token(metalbeard.tokens.TT_VARIABLE, metalbeard.tokens.TV_SINGLE))
                    self.current_id_open = self.current_id_close = metalbeard.tokens.TC_VARIABLE
                    continue

                case metalbeard.tokens.TC_MACRO:
                    output.append(benny.Token(metalbeard.tokens.TT_MACRO, metalbeard.tokens.TV_SINGLE))
                    self.current_id_open = self.current_id_close = metalbeard.tokens.TC_MACRO
                    continue

                case metalbeard.tokens.TC_STRING:
                    output.append(benny.Token(metalbeard.tokens.TT_STRING, metalbeard.tokens.TV_SINGLE))
                    self.current_id_open = self.current_id_close = metalbeard.tokens.TC_STRING
                    continue

                case metalbeard.tokens.TC_SEPERATOR:
                    output.append(benny.Token(metalbeard.tokens.TT_SEPERATOR, metalbeard.tokens.TV_SINGLE))

                case metalbeard.tokens.TC_SCOPE_OPEN:
                    output.append(benny.Token(metalbeard.tokens.TT_SCOPE, metalbeard.tokens.TV_OPEN))
                case metalbeard.tokens.TC_SCOPE_CLOSE:
                    output.append(benny.Token(metalbeard.tokens.TT_SCOPE, metalbeard.tokens.TV_CLOSE))

                case metalbeard.tokens.TC_GROUP_OPEN:
                    output.append(benny.Token(metalbeard.tokens.TT_GROUP, metalbeard.tokens.TV_OPEN))
                case metalbeard.tokens.TC_GROUP_CLOSE:
                    output.append(benny.Token(metalbeard.tokens.TT_GROUP, metalbeard.tokens.TV_CLOSE))

                case _:
                    print("Unrecognized Character: " + self.current_char + " at " + self.position.__str__())
            self.advance()
        return output
