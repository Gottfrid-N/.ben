class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __str__(self) -> str:
        if self.value == "\n":
            return f"<[{self.type}: \"\\n\"]>"
        return f"<[{self.type}: \"{self.value}\"]>"

    def __repr__(self):
        return self.__str__()
