import re
import sys

try:
    inputPath = sys.argv[1]
except IndexError:
    inputPath = "input.bismuth"

try:
    outputPath = sys.argv[2]
except IndexError:
    outputPath = "output.txt"

input = open(inputPath, "r", encoding="UTF-8").read()
outputFile = open(outputPath, "w", encoding="UTF-8")
output = ""

current_char = 0

variables = {}

def skipWhitespace():
    global current_char
    while re.match("\s", input[current_char]):
        current_char += 1

def captureUntilMatch(pattern):
    global current_char
    capture = ""
    while not re.match(pattern, input[current_char]):
        capture += input[current_char]
        current_char += 1
    return capture

def identifier():
    return captureUntilMatch("[^A-Za-z\._-]")

def varLogic():
    global current_char
    global output
    global variables
    current_char += 1
    match input[current_char]:
        case "=":
            print("declare", end=": ")
            current_char += 1
            varId = identifier()
            skipWhitespace()
            if (input[current_char] != "="):
                raise SyntaxError("Expected \"=\" at character: " + str(current_char))
            current_char += 1
            skipWhitespace()
            if (input[current_char] != "\""):
                raise SyntaxError("Expected \"\"\" at character: " + str(current_char))
            current_char += 1
            value = captureUntilMatch("[\"]")
            print(varId, end=" = ")
            print(value)
            variables[varId] = value
            if (input[current_char + 1] == "+"):
                print("acces", end=": ")
                print(varId)
                output += variables[varId]
                current_char += 1
        case _:
            print("acces", end=": ")
            varId = identifier()
            print(varId)
            output += variables[varId]
            current_char -= 1


def funcLogic():
    pass

def bismuthLogic():
    global current_char
    current_char += 1
    match input[current_char]:
        case "%":
            print("var", end="-")
            varLogic()
        case "#":
            print("func", end="-")
            funcLogic()

while current_char < len(input):
    match input[current_char]:
        case "@":
            bismuthLogic()
        case _:
            print(input[current_char], end="")
            output += input[current_char]
    current_char += 1

outputFile.write(output)
outputFile.close()