from abc import ABC, abstractmethod
import benny


class Lexer(ABC):
    def __init__(self,  str_input: str):
        self.buffer = benny.StringBuffer()
        self.position = benny.Position()
        self.input = str_input
        self.current_char = None
        self.advance()

    def advance(self):
        self.position.increment()
        try:
            self.current_char = self.input[self.position.character]
            print("[" + self.position.__str__() + "]: " + self.current_char)
        except IndexError:
            self.current_char = None

    @abstractmethod
    def lex(self):
        pass