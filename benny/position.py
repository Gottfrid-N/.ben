class Position:
    def __init__(self):
        self.char = -1
        self.column = 0
        self.line = 1

    def increment(self):
        self.char += 1
        self.column += 1

    def increment_line(self):
        self.line += 1
        self.column = 1

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"<character: {self.char} || line: {self.line}, column: {self.column}>"
