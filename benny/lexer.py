import benny
import abc
import re


def nested_logic(self, token_open, token_close):
    def inner(func):
        self.append_token(token_open)
        self.advance()
        func()
        self.append_token(token_close)
    return inner


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
            print(f"{self.position.__str__()}: <\"{benny.escape_codify_char(self.current_char)}\">", end=" ")
        except IndexError:
            self.current_char = None
            print("end", end="")

    def append_token(self, token):
        self.tokens.append(token)
        print(f"{token}", end="")

    def identifier_logic(self, style):
        buffer = ""
        while re.match("\w", self.current_char):
            buffer += self.current_char
            self.advance()
        match style:
            case "PascalCase":
                if not re.match("^([A-Z0-9][a-z0-9]*)+", buffer):
                    print(f"Invalid style in identifier at: {self.position.__str__()}\nExpected: PascalCase")
            case "camelCase":
                if not re.match("^([a-z0-9]+)+([A-Z0-9][a-z0-9]*)*", buffer):
                    print(f"Invalid style in identifier at: {self.position.__str__()}\nExpected: camelCase")
            case "snake_case":
                if not re.match("[A-Z]", buffer):
                    print(f"Invalid style in identifier at: {self.position.__str__()}\nExpected: snake_case")
            case "SCREAMING_SNAKE_CASE":
                if not re.match("[a-z]", buffer):
                    print(f"Invalid style in identifier at: {self.position.__str__()}\nExpected: snake_case")

    @abc.abstractmethod
    def lex_logic(self):
        pass

    def lex(self):
        while self.current_char is not None:
            self.lex_logic()
            self.advance()
