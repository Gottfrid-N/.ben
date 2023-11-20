import metalbeard

file = open("A:\\Projects\\.shhtml\\metalbeard\\input.metalbeard", "r", encoding="UTF-8")

lexer = metalbeard.Lexer(file.read())

print("\n")
print(f"{file}")
print(f"{lexer.input}")
lexer.lex()
