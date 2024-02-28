import benny


class BismuthInterpreter(benny.Interpreter):
    def __init__(self, inputs: [str], outputs):
        super().__init__(inputs, outputs)

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
        self.increment()
        match self.inputs[0][self.current_char]:
            case "=":
                self.var_set()
            case _:
                if self.inputs[0][self.current_char] == "+":
                    self.increment()
                self.var_get()

    def func_logic(self):
        pass

    def bismuth_logic(self):
        self.increment()
        match self.inputs[0][self.current_char]:
            case "%":
                print("var", end="-")
                self.var_logic()
            case "#":
                print("func", end="-")
                self.func_logic()

    def interpret(self):
        while self.current_char < len(self.inputs[0]):
            match self.inputs[0][self.current_char]:
                case "@":
                    self.bismuth_logic()
                case _:
                    self.outputs[0] += self.inputs[0][self.current_char]
            self.increment()
