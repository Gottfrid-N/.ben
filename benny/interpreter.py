from abc import ABC, abstractmethod
import re


class Interpreter(ABC):
    def __init__(self, inputs: [str]):
        self.current_char = 0
        self.input = 0
        self.inputs = inputs
        self.outputs = []
        self.variables = {}

    @abstractmethod
    def interpret(self):
        pass

    def increment(self):
        self.current_char += 1

    def decrement(self):
        self.current_char -= 1

    def skip_whitespace(self):
        while re.match("\s", self.inputs[self.input][self.current_char]):
            self.current_char += 1

    def capture_until_match(self, pattern):
        capture = ""
        try:
            while not re.match(pattern, self.inputs[self.input][self.current_char]):
                capture += self.inputs[self.input][self.current_char]
                self.increment()
        except IndexError:
            return capture
        return capture

    def identifier(self):
        return self.capture_until_match("[^A-Za-z0-9\._-]")
