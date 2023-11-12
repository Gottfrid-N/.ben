from enum import Enum

#inputPath = input("Enter file path")
path = "A:\\Projects\\.shhtml\\metalbeard\\bismuth\\src\\put\\"
inputFile = open(path + "input.shhtml", "r")

class Modes(Enum):
    EMPTY = 0
    METALBEARD = 1
    VARIABLE = 2
    FUNCTION = 3
    ARGUMENTS = 4

class Lexer:
    def __init__(self, input, output):
        self.buffer = ""
        self.tokens = {
            "var": "%",
            "metalbeard": "@",
            "scope": {
                "open": "{",
                "close": "}"
            },
            "group": {
                "open": "(",
                "close": ")"
            }
        }
        self.mode = Modes.EMPTY
        
        self.input = input
        self.output = output
        
        self.char_var = "%"
        self.token_var = "var"

        self.char_scope_open = "{"
        self.char_scope_close = "}"
        self.token_scope = "scope"
        
        self.char_group_open = "("
        self.char_group_close = ")"
        self.token_group = "group"
        self.token_arguments = "args"
        self.char_argument_seperator = ","
        self.token_argument = "arg"
        
        self.char_function = "#"
        self.token_function = "func"

    
    def __str__(self):
        return self.output.read()
    
    def token(self, tokenType, content):
        return "["+tokenType+": "+"\""+content+"\""+"]" 
    
    def bufferAdd(self, addition):
        self.buffer += addition
    
    def bufferEmpty(self):
        self.buffer = ""
    
    def outputToken(self, token):
        self.output.write(token + "\n")
    
    def lex(self):
        input_string = self.input.read()
        for char in input_string:
            print(self.buffer)
            if char == " " or char == "\n":
                continue
            match self.mode:
                case Modes.EMPTY:
                    match char:
                        case self.char_var:
                            self.mode = Modes.VARIABLE
                        case self.char_function:
                            self.mode = Modes.FUNCTION
                        
                        case self.char_scope_open:
                            self.outputToken(self.token(self.token_scope, "open"))
                        case self.char_scope_close:
                            self.outputToken(self.token(self.token_scope, "close"))
                case Modes.METALBEARD:
                    print("metal")
                case Modes.VARIABLE:
                    if char == self.char_var:
                        self.outputToken(self.token(self.token_var, self.buffer))
                        self.bufferEmpty()
                        self.mode = Modes.EMPTY
                        continue
                    self.bufferAdd(char)
                case Modes.FUNCTION:
                    if char == self.char_group_open:
                        self.outputToken(self.token(self.token_function, self.buffer))
                        self.bufferEmpty()
                        self.outputToken(self.token(self.token_arguments, "open"))
                        self.mode = Modes.ARGUMENTS
                        continue
                    self.bufferAdd(char)
                case Modes.ARGUMENTS:
                    if char == self.char_group_close:
                        self.outputToken(self.token(self.token_argument, self.buffer))
                        self.bufferEmpty()
                        self.outputToken(self.token(self.token_arguments, "close"))
                        self.mode = Modes.EMPTY
                        continue
                    if char == self.char_argument_seperator:
                        self.outputToken(self.token(self.token_argument, self.buffer))
                        self.bufferEmpty()
                        continue
                    self.bufferAdd(char)

lexer = Lexer(open(path + "input.shhtml", "r"), open(path + "output.txt", "w"))
lexer.lex()