import sys
import metalbeard.bismuth as bismuth

input_path = None
output_path = None


########
# MAIN #
########
def main():
    global input_path
    global output_path

    args = sys.argv

    input_path = "A:\\Projects\\.shhtml\\metalbeard\\bismuth\\put\\input.txt"
    output_path = "A:\\Projects\\.shhtml\\metalbeard\\bismuth\\put\\output.txt"

    print(input_path, output_path)

    input_file = open(input_path, "r")
    lexer = bismuth.lexer.BismuthLexer(input_file.read())

    output = lexer.lex()
    output_file = open(output_path, "w")

    output_file.write(output.__str__())
    output_file.close()
    input_file.close()
    print(output.__str__())


if __name__ == "__main__":
    main()
