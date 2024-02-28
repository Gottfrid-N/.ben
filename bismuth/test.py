import bismuth

if __name__ == "__main__":
    import sys

    try:
        inputPath = sys.argv[1]
    except IndexError:
        inputPath = "input.bismuth"

    try:
        outputPath = sys.argv[2]
    except IndexError:
        outputPath = "output.txt"

    bismuth_interpreter = bismuth.BismuthInterpreter([open(inputPath, "r", encoding="UTF-8").read()], [""])
    bismuth_interpreter.interpret()

    output = bismuth_interpreter.outputs[0]
    outputFile = open(outputPath, "w", encoding="UTF-8").write(output)
