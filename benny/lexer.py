import abc
import re

import benny


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
            print(f"{self.position.__str__()}: <\"{repr(self.current_char)}\">", end=" ")
        except IndexError:
            self.current_char = None
            print("end", end="")

    def append_token(self, token):
        if token is not None:
            self.tokens.append(token)
            print(f"{token}", end="")

    def identifier(self, expected_style: benny.Style):
        buffer = ""

        while re.match("\w", self.current_char):
            buffer += self.current_char
            self.advance()

        if not expected_style.value()(buffer):
            print(f"""Style Warning: Invalid case in {buffer} at {self.position}
                      Expected: {expected_style}""")

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
