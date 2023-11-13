########################
# METALBEARD TOKENS    #
# TT = Token Type      #
# TC = Token Character #
########################

TT_METALBEARD = "METALBEARD" 
TC_METALBEARD = "@"

TT_BISMUTH = "BISMUTH"
TC_BISMUTH = "$"

TT_RUTHENIUM = "RUTHENIUM"
TC_RUTHENIUM = "£"

TT_SCOPE = "SCOPE"
TC_SCOPE_OPEN = "{"
TC_SCOPE_CLOSE = "}"

TT_GROUP = "GROUP"
TC_GROUP_OPEN = "("
TC_GROUP_CLOSE = ")"
TC_GROUP_SEPERATOR = ","

TT_VARIABLE = "VARIABLE"
TC_VARIABLE_OPEN = "%"
TC_VARIABLE_CLOSE = "%"

################
# GLOBAL TYPES #
################

def fuckOff(tard):
    return "fuck off " + tard

class Token:
    def __init__(self, type, content):
        self.type = type
        self.content = content
    def __str__(self) -> str:
        return self.type + ":" + self.content

class Position:
    def __init__(self):
        self.line = 1
        self.column = 1
        self.character = 1
    def __str__(self) -> str:
        return "(line: " + self.line + ", column: " + self.column + "), character: " + self.character
    
    def increment(self, counter):
        counter += 1
    def incrementLine(self):
        self.line += 1
        self.column = 1