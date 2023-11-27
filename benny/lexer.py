import benny
import abc
import re


class Lexer(abc.ABC):
    def __init__(self, input_: str):
        self.tokens = []
        self.memory = []

        self.input = input_
        self.position = benny.Position()
        self.current_char = ""
        self.advance()

    def increment_position(self):
        self.position.increment()
        if self.current_char == "\n":
            self.position.increment_line()

    def advance(self):
        print("\n", end="")
        self.increment_position()
        try:
            self.current_char = self.input[self.position.char]
            print(f"{self.position.__str__()}: <\"{benny.text.escape_codify_char(self.current_char)}\">", end=" ")
        except IndexError:
            self.current_char = None
            print("end", end="")

    def append_token(self, token):
        if token is not None:
            self.tokens.append(token)
            print(f"{token}", end="")

    def identifier(self, style_name, style, **kwargs):
        buffer = ""
        while re.match("\w", self.current_char):
            buffer += self.current_char
            self.advance()
        if not style(buffer, **kwargs):
            print(f"Invalid Identifier style in \"{buffer}\" at {self.position.__str__()}\n\n"
                  f"Expected {style_name}")
        if buffer != "":
            return benny.Token("IDENTIFIER", buffer)
        return None

    @abc.abstractmethod
    def lex_logic(self):
        pass

    def lex(self):
        while self.current_char is not None:
            self.lex_logic()
            self.advance()
