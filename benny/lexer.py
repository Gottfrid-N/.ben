import benny
import abc


class Lexer(abc.ABC):
    def __init__(self, input_: str):
        self.tokens = []
        self.memory = []

        self.input = input_
        self.position = benny.Position()
        self.current_char = ""
        self.advance()

    def advance(self):
        self.position.increment()
        if self.current_char == "\n":
            self.position.increment_line()
        try:
            self.current_char = self.input[self.position.char]
            if self.current_char == "\n":
                print(f"{self.position.__str__()}: <\"\\n\">", end=" ")
            else:
                print(f"{self.position.__str__()}: <\"{self.current_char}\">", end=" ")
        except IndexError:
            self.current_char = None
            print("end", end="")

    def append_token(self, token):
        self.tokens.append(token)
        print(f"{token}", end="")

    @abc.abstractmethod
    def lex_logic(self):
        pass

    def lex(self):
        while self.current_char is not None:
            self.lex_logic()
            print("")
            self.advance()
