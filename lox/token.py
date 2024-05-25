from .token_type import TokenType
# TODO import `Object` definition from lexer?


class Token:
    _type: TokenType
    lexeme: str
    literal: Object
    line: int

    def __init__(self, _type: TokenType, lexeme: str, literal: Object, line: int):
        self._type = _type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def to_str(self) -> str:
        return f"{self._type} {self.lexeme} {self.literal}"
