import benny
import metalbeard
import metalbeard.bismuth as bismuth


class BismuthLexer(benny.Lexer):
    def lex(self):
        output = []

        while self.current_char is not None:
            match self.current_char:
                case "\n":
                    self.advance()
                    self.position.increment_line()
                    continue
                case "\t" | "\x20":
                    self.advance()
                    continue
            self.advance()
