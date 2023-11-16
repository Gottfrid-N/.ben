import benny
import re
import metalbeard
import metalbeard.bismuth as bismuth


class BismuthLexer(benny.Lexer):
    def parameter_lex(self):
        output = []

        while self.current_char is not benny.tokens.characters.GROUP_CLOSE:
            while self.current_char is not benny.tokens.characters.SEPERATOR:
                output.append(benny.tokens.STRING_OPEN)
                output.append(self.string_lex())
                output.append(benny.tokens.STRING_CLOSE)

    def string_lex(self):
        output = []

        self.advance()
        while self.current_char is not benny.tokens.characters.STRING:
            output.append(benny.tokens.char(self.current_char))
        self.advance()

    def bismuth_lex(self):
        output = []

        while self.current_char is not None:
            match self.current_char:
                case benny.tokens.characters.SCOPE_OPEN:
                    output.append(benny.tokens.SCOPE_OPEN)
                case benny.tokens.characters.SCOPE_CLOSE:
                    output.append(benny.tokens.SCOPE_CLOSE)
                    output.append(metalbeard.tokens.BISMUTH_CLOSE)
                    break
                case benny.tokens.characters.STRING:
                    output.append(benny.tokens.STRING_OPEN)
                    output.append(self.string_lex())
                    output.append(benny.tokens.STRING_CLOSE)

                case metalbeard.tokens.characters.MACRO:
                    output.append(metalbeard.tokens.MACRO_OPEN)
                    output.append(benny.tokens.STRING_OPEN)
                    output.append(self.string_lex())
                    output.append(benny.tokens.STRING_CLOSE)

            self.advance()
        output.append(metalbeard.tokens.BISMUTH_CLOSE)
        return output

    def lex(self):
        output = []

        while self.current_char is not None:
            match self.current_char:
                case benny.tokens.characters.NEWLINE:
                    self.advance()
                    self.position.increment_line()
                    continue
                case benny.tokens.characters.TAB | benny.tokens.characters.SPACE:
                    self.advance()
                    continue
                case metalbeard.tokens.characters.BISMUTH:
                    output.append(metalbeard.tokens.BISMUTH_OPEN)
                    self.advance()
                    output.append(self.bismuth_lex())

            self.advance()
        return output