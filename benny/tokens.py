import benny

STRING = benny.TokenDefinition("STRING", "\"")
SEPERATOR = benny.TokenDefinition("SEPERATOR", ",")
SCOPE = benny.TokenDefinition("SCOPE", ["{", "}"])
GROUP = benny.TokenDefinition("GROUP", ["(", ")"])
