import benny
import bismuth

class ShhtmlInterpreter(benny.Interpreter):
    def interpret(self):
        bismuth_interpreter = bismuth.BismuthInterpreter(self.inputs)
        bismuth_interpreter.interpret()