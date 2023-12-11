import re

import benny
import metalbeard.macros


class Lexer(benny.lexer.Lexer):
    def is_case(self, case_pattern, string):
        if re.fullmatch(case_pattern, string) is None:
            print(f"Invalid case in \"{string}\" at {self.position}")

    def identifier(self, case_pattern):
        identifier = ""
        self.skip_whitespace()
        while self.current_char in benny.text.regex.word:
            identifier += self.current_char
        self.is_case(case_pattern, identifier)
        return identifier

    def token(self, type_, value):
        self.is_case(benny.text.case.screaming_snake_case_pattern, type_)
        self.append_token(benny.Token(type_, value))

    def lex_metalbeard_logic(self):
        match self.current_char:


    def lex_logic(self):
        match self.current_char:
            case "@":
                self.lex_metalbeard_logic()
            case _:
                self.token("CHARACTER", self.current_char)


if __name__ == "__main__":
    input_ = open("A:\\Projects\\.shhtml\\metalbeard\\input.metalbeard", "r")

    lexer = Lexer(input_.read())
    Lexer.lex(lexer)
    print(lexer.tokens)
