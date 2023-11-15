import benny
import re
import metalbeard
import metalbeard.bismuth as bismuth


class BismuthLexer(benny.Lexer):
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
                case metalbeard.tokens.BISMUTH.character:
                    output.append(benny.Token(metalbeard.tokens.BISMUTH.type, benny.))
                    match self.current_char:
                        case benny.tokens.GROUP.character


            self.advance()
