import string

import benny
import metalbeard
import re

if __name__ == "__main__":
    file = open("A:\\Projects\\.shhtml\\metalbeard\\input.metalbeard", "r", encoding="UTF-8")

    lexer = metalbeard.Lexer(file.read())

    print("\n")
    print(f"{file}")
    print(f"{lexer.input}")
    lexer.lex()


class Lexer(benny.Lexer):
    def lex_logic(self):
        match self.current_char:
            case "@":
                self.advance()
                self.lex_metalbeard_logic()
            case _:
                self.append_token(benny.Token("CHARACTER", repr(self.current_char)))

    def lex_metalbeard_logic(self):
        match self.current_char:
            case "{":
                self.advance()
                pass
            case "#":
                self.advance()
                self.identifier(benny.text.Style.camel_case)
            case "%":
                self.advance()
                self.identifier(benny.text.Style.screaming_snake_case)