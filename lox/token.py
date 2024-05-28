from lox.token_type import TokenType


class Object:  # TODO: real Object implementation
    pass


class Token:
    _type: TokenType
    lexeme: str
    literal: Object | None
    line: int

    def __init__(
        self, _type: TokenType, lexeme: str, literal: Object | None, line: int
    ):
        self._type = _type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def to_str(self) -> str:
        l = self.literal if self.literal is not None else "NoneType"
        return f"{self._type} {self.lexeme} {l}"
