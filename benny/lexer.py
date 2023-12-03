import benny.position
import benny.text
import abc
import re


class Lexer(abc.ABC):
    def __init__(self, input_: str):
        self.tokens = []
        self.memory = {}

        self.input = input_
        self.position = benny.position.Position()
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
            print(f"{self.position.__str__()}: <\"{repr(self.current_char)}\">", end=" ")
        except IndexError:
            self.current_char = None
            print("end", end="")

    def skip_whitespace(self):
        while self.current_char in benny.text.whitespace:
            self.advance()

    def append_token(self, token):
        if token is not None:
            self.tokens.append(token)
            print(f"{token}", end="")

    def append_memory(self, key, value):
        self.memory[key] = value
        print(f"<{key}: {self.memory[key]}")

    def identifier(self, style_name, style, **kwargs):
        identifier = ""
        while re.match("\w", self.current_char):
            identifier += self.current_char
            self.advance()
        if not style(identifier, **kwargs):
            print(f"Invalid Identifier style in \"{identifier}\" at {self.position.__str__()}\n\n"
                  f"Expected {style_name}")
        if identifier != "":
            return benny.Token("IDENTIFIER", identifier)
        return None

    @abc.abstractmethod
    def lex_logic(self):
        pass

    def lex(self):
        while self.current_char is not None:
            self.lex_logic()
            self.advance()
