import benny


def char(character):
    return benny.Token("CHARACTER", character)


SEPERATOR = benny.Token("SEPERATOR", benny.tokens.values.EMPTY)

STRING_OPEN = benny.Token("STRING", benny.tokens.values.OPEN)
STRING_CLOSE = benny.Token("STRING", benny.tokens.values.CLOSE)

PATH_OPEN = benny.Token("PATH", benny.tokens.values.OPEN)
PATH_CLOSE = benny.Token("PATH", benny.tokens.values.CLOSE)

SCOPE_OPEN = benny.Token("SCOPE", benny.tokens.values.OPEN)
SCOPE_CLOSE = benny.Token("SCOPE", benny.tokens.values.CLOSE)

GROUP_OPEN = benny.Token("GROUP", benny.tokens.values.OPEN)
GROUP_CLOSE = benny.Token("GROUP", benny.tokens.values.CLOSE)
