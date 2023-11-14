__version__ = "0.1a|0.0b|>2023-11-14"

import metalbeard.tokens


class Position:
    def __init__(self):
        self.line = 0
        self.column = -1
        self.character = -1

    def __str__(self) -> str:
        return ("(line: " + (self.line + 1).__str__() + ", column: " + (self.column + 1).__str__() +
                "), character: " + (self.character + 1).__str__())

    def __repr__(self) -> str:
        return self.__str__()

    def increment(self):
        self.column += 1
        self.character += 1

    def increment_line(self):
        self.line += 1
        self.column = 0


class StringBuffer:
    def __init__(self):
        self.buffer = ""

    def __str__(self) -> str:
        return self.buffer

    def __repr__(self) -> str:
        return self.__str__()

    def add(self, addition):
        self.buffer += str(addition)

    def clear(self):
        self.buffer = ""
