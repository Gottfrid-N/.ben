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

###########
# CLASSES #
###########
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __str__(self) -> str:
        return self.type + ":" + self.value

    def __repr__(self) -> str:
        return self.__str__()
