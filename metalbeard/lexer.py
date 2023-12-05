import re

import benny
import metalbeard.tokens
import metalbeard.macros


class Lexer(benny.lexer.Lexer):
    def value(self):
        string = ""
        while self.current_char != "\"":
            string += self.current_char
            self.advance()
        return string

    def operator(self):
        match self.current_char:
            case "=":
                self.advance()
                self.skip_whitespace()

    def identifier(self, style_name, style, **kwargs):
        identifier = ""
        while re.match("\w", self.current_char):
            identifier += self.current_char
            self.advance()
        if not style(identifier, **kwargs):
            print(f"Invalid Identifier style in \"{identifier}\" at {self.position.__str__()}\n\n"
                  f"Expected {style_name}")
        return identifier

    def assign_expression(self):


    def call_expression(self):


    def lex_expression(self):
        match self.current_char:
            case "%":
                self.advance()
                self.assign_expression("SCREAMING_SNAKE_CASE", benny.text.case.screaming_snake_case)
            case "#":
                self.advance()
                self.expression("camelCase", benny.text.case.camel_case)
            case "{":
                pass

    def lex_logic(self):
        match self.current_char:
            case "@":
                self.advance()
                self.lex_expression()
            case _:
                self.append_token(metalbeard.tokens.character(self.current_char))


if __name__ == "__main__":
    input_ = open("A:\\Projects\\.shhtml\\metalbeard\\input.metalbeard", "r")

    lexer = Lexer(input_.read())
    Lexer.lex(lexer)
    print(lexer.tokens)
