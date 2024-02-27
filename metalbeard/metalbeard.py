########################
# METALBEARD TOKENS    #
# TT = Token Type      #
# TC = Token Character #
# TV = Token Value     #
########################


TV_OPEN = "OPEN"
TV_CLOSE = "CLOSE"
TV_SINGLE = "SINGLE"

TT_ID = "ID"

TT_METALBEARD = "METALBEARD"
TC_METALBEARD = "@"

TT_BISMUTH = "BISMUTH"
TC_BISMUTH = "$"

TT_RUTHENIUM = "RUTHENIUM"
TC_RUTHENIUM = "£"

TT_VARIABLE = "VARIABLE"
TC_VARIABLE = "%"

TT_MACRO = "MACRO"
TC_MACRO = "#"

TT_STRING = "STRING"
TC_STRING = "\""

TT_SEPERATOR = "SEPERATOR"
TC_SEPERATOR = ","

TT_SCOPE = "SCOPE"
TC_SCOPE_OPEN = "{"
TC_SCOPE_CLOSE = "}"

TT_GROUP = "GROUP"
TC_GROUP_OPEN = "("
TC_GROUP_CLOSE = ")"


################
# GLOBAL TYPES #
################
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


class Token:
    def __init__(self, type_, value):
        self.type = type_
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

    def increment(self):
        self.column += 1
        self.character += 1

    def increment_line(self):
        self.line += 1
        self.column = 0
