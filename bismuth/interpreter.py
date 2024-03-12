import benny
import re

import bismuth


class BismuthInterpreter(benny.Interpreter):
    def __init__(self, inputs: [str]):
        super().__init__(inputs)
        self.variables = {"this": self.inputs[0]}
        self.functions = {
            "regex.match": lambda pattern, string, flags: re.match(pattern, string, flags)
        }
        self.outputs.append("")

    def import_logic(self):
        print("import", end=": ")
        self.increment()
        if self.inputs[0][self.current_char] != "\"":
            raise SyntaxError("Expected \"\"\" at character: " + str(self.current_char))
        self.increment()
        import_path = self.capture_until_match("[\"]")
        print(import_path)
        import_interpreter = bismuth.BismuthInterpreter([open(import_path, "r", encoding="UTF-8").read()])
        import_interpreter.interpret()
        imported_variables = import_interpreter.variables
        imported_variables.pop("this")
        self.variables.update(imported_variables)

    def var_set(self):
        print("set", end=": ")
        self.increment()
        var_id = self.identifier()
        print(var_id, end=" = ")
        self.skip_whitespace()
        if self.inputs[0][self.current_char] != "=":
            raise SyntaxError("Expected \"=\" at character: " + str(self.current_char))
        self.increment()
        self.skip_whitespace()
        if self.inputs[0][self.current_char] != "\"":
            raise SyntaxError("Expected \"\"\" at character: " + str(self.current_char))
        self.increment()
        var_value = self.capture_until_match("[\"]")
        print(var_value)
        self.variables[var_id] = var_value
        if self.inputs[0][self.current_char + 1] == "+":
            print("get", end=": ")
            print(var_id)
            self.outputs[0] += self.variables[var_id]
            self.increment()

    def var_get(self):
        print("get", end=": ")
        var_id = self.identifier()
        print(var_id)
        self.outputs[0] += self.variables[var_id]
        self.decrement()

    def var_logic(self):
        print("var", end="-")
        self.increment()
        match self.inputs[0][self.current_char]:
            case "=":
                self.var_set()
            case "+":
                self.increment()
                self.var_get()
            case _:
                self.var_get()

    def func_set(self):
        print("set", end=": ")

    def func_get(self):
        print("get", end=": ")
        func_id = self.identifier()
        print(func_id)
        self.decrement()

    def func_logic(self):
        print("func", end="-")
        self.increment()
        match self.inputs[0][self.current_char]:
            case "=":
                self.func_set()
            case "+":
                self.increment()
                self.func_get()
            case _:
                self.func_get()

    def bismuth_logic(self):
        self.increment()
        match self.inputs[0][self.current_char]:
            case "%":
                self.var_logic()
            case "#":
                self.func_logic()
            case "I":
                self.import_logic()

    def interpret(self):
        while self.current_char < len(self.inputs[0]):
            match self.inputs[0][self.current_char]:
                case "$":
                    self.bismuth_logic()
                case "\\":
                    self.increment()
                    self.outputs[0] += self.inputs[0][self.current_char]
                case _:
                    self.outputs[0] += self.inputs[0][self.current_char]
            self.increment()
