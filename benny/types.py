class TokenDefinition:
    def __init__(self, type_, character):
        self.type = type_
        self.character = character


class Token:
    def __init__(self, definition: TokenDefinition, value: str):
        self.type = definition.type
        self.value = value

    def __str__(self) -> str:
        return self.type + ":" + self.value

    def __repr__(self) -> str:
        return self.__str__()


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

    def __add__(self, other):
        return self.__str__() + other

    def increment(self):
        self.column += 1
        self.character += 1

    def increment_line(self):
        self.line += 1
        self.column = -1


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
