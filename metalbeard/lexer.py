import sys

import benny
import metalbeard.tokens
import metalbeard.macros


class Lexer(benny.lexer.Lexer):
    def string(self):
        string = ""
        while self.current_char != "\"":
            string += self.current_char
            self.advance()
        return string

    def operator(self, identifier):
        match self.current_char:
            case "=":
                self.advance()
                self.skip_whitespace()
                if self.current_char == "\"":
                    self.advance()
                    value = self.string()
                    self.memory[identifier.value] = value
                else:
                    print(f"Unexpected char at {self.position}"
                          f"Expected: \"")
                    sys.exit()
            case "(":
                pass
            case "%":
                pass

    def expression(self, style_name, style):
        identifier = self.identifier(style_name, style)
        self.skip_whitespace()
        self.operator(identifier)

    def lex_expression(self):
        match self.current_char:
            case "%":
                self.advance()
                self.expression("SCREAMING_SNAKE_CASE", benny.text.case.screaming_snake_case)
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
    print(lexer.memory)
