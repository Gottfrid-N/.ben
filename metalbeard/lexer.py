import benny
import metalbeard


class Lexer(benny.Lexer):
    def lex_metalbeard_logic(self):
        match self.current_char:
            case "{":
                pass
            case "€":
                pass
            case "#":
                pass

    def lex_logic(self):
        match self.current_char:
            case "@":
                self.append_token(benny.Token("METALBEARD", "OPEN"))
                self.lex_metalbeard_logic()
                self.append_token(benny.Token("METALBEARD", "CLOSE"))
            case _:
                self.append_token(benny.Token("CHARACTER", self.current_char))
