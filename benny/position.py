class Position:
    def __init__(self):
        self.character = 0
        self.column = 0
        self.line = 0

    def increment(self):
        self.character += 1
        self.column += 1

    def increment_line(self):
        self.increment()
        self.line += 1
        self.column = 0
