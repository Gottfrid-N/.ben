import re
import sys
import benny

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


def skip_whitespace():
    global current_char
    while re.match("\s", input[current_char]):
        current_char += 1


def capture_until_match(pattern):
    global current_char
    capture = ""
    while not re.match(pattern, input[current_char]):
        capture += input[current_char]
        current_char += 1
    return capture


def identifier():
    return capture_until_match("[^A-Za-z\._-]")


def var_logic():
    global current_char
    global output
    global variables
    current_char += 1
    match input[current_char]:
        case "=":
            print("declare", end=": ")
            current_char += 1
            var_id = identifier()
            skip_whitespace()
            if input[current_char] != "=":
                raise SyntaxError("Expected \"=\" at character: " + str(current_char))
            current_char += 1
            skip_whitespace()
            if input[current_char] != "\"":
                raise SyntaxError("Expected \"\"\" at character: " + str(current_char))
            current_char += 1
            value = capture_until_match("[\"]")
            print(var_id, end=" = ")
            print(value)
            variables[var_id] = value
            if input[current_char + 1] == "+":
                print("access", end=": ")
                print(var_id)
                output += variables[var_id]
                current_char += 1
        case _:
            if input[current_char] == "+":
                current_char += 1
            print("access", end=": ")
            var_id = identifier()
            print(var_id)
            output += variables[var_id]
            current_char -= 1

def func_logic():
    pass


def bismuth_logic():
    global current_char
    current_char += 1
    match input[current_char]:
        case "%":
            print("var", end="-")
            var_logic()
        case "#":
            print("func", end="-")
            func_logic()


while current_char < len(input):
    match input[current_char]:
        case "@":
            bismuth_logic()
        case _:
            print(input[current_char], end="")
            output += input[current_char]
    current_char += 1

outputFile.write(output)
outputFile.close()
