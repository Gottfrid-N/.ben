import benny
import metalbeard


class Lexer(benny.Lexer):
    def lex_metalbeard_scope_logic(self):
        while self.current_char != "}":
            if self.current_char == ";":
                self.append_token(metalbeard.tokens.SCOPE_SEPERATOR)
            self.lex_metalbeard_logic()
            self.advance()

    def lex_metalbeard_group_logic(self):
        while self.current_char != ")":
            self.lex_metalbeard_logic()
            self.advance()

    def lex_metalbeard_logic(self):
        match self.current_char:
            case "{":
                self.append_token(metalbeard.tokens.SCOPE_OPEN)
                self.advance()
                self.lex_metalbeard_scope_logic()
                self.append_token(metalbeard.tokens.SCOPE_CLOSE)
            case "(":
                self.append_token(metalbeard.tokens.GROUP_OPEN)
                self.advance()
                self.lex_metalbeard_group_logic()
                self.append_token(metalbeard.tokens.GROUP_CLOSE)
            case "%":
                self.append_token(self.identifier("SCREAMING_SNAKE_CASE", benny.text.style.screaming_snake_case))
            case "#":
                self.advance()
                while self.current_char != "=":
                    self.append_token(self.identifier("SCREAMING_SNAKE_CASE", benny.text.style.screaming_snake_case))
                    self.advance()

    def lex_logic(self):
        match self.current_char:
            case "@":
                self.append_token(metalbeard.tokens.METALBEARD_OPEN)
                self.advance()
                self.lex_metalbeard_logic()
                self.append_token(metalbeard.tokens.METALBEARD_CLOSE)
            case _:
                self.append_token(metalbeard.tokens.character(self.current_char))
