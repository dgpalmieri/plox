from lox.token import Token
from lox.token_type import TokenType


class Lexer:
    __source__: str
    __tokens__: list[Token] = []
    __start__: int = 0
    __current__: int = 0
    __line__: int = 1

    def __init__(self, source: str):
        self.__source__ = source

    def scan_tokens(self) -> list[Token]:
        while not self.is_at_end():
            self.__start__ = self.__current__
            self.scan_token()

        self.__tokens__.append(Token(TokenType.EOF, "", None, self.__line__))
        return self.__tokens__

    def is_at_end(self) -> bool:
        return self.__current__ >= len(self.__source__)

    def scan_token(self) -> None:
        c: str = self.__advance__()
        if c == "(":
            self.__add_token__(TokenType.LEFT_PAREN)
        elif c == ")":
            self.__add_token__(TokenType.RIGHT_PAREN)
        elif c == "{":
            self.__add_token__(TokenType.LEFT_BRACE)
        elif c == "}":
            self.__add_token__(TokenType.RIGHT_BRACE)
        elif c == ",":
            self.__add_token__(TokenType.COMMA)
        elif c == ".":
            self.__add_token__(TokenType.DOT)
        elif c == "-":
            self.__add_token__(TokenType.MINUS)
        elif c == "+":
            self.__add_token__(TokenType.PLUS)
        elif c == ";":
            self.__add_token__(TokenType.SEMICOLON)
        elif c == "*":
            self.__add_token__(TokenType.STAR)
        else:
            raise SyntaxError(f"Bad Token: {c}")

        # elif c == '': self.__add_token__(TokenType.)

    def __advance__(self) -> str:
        if self.__current__ + 1 <= len(self.__source__):
            return self.__source__[self.__current__ + 1]
        return "End of String"

    def __add_token__(self, _type: TokenType, literal: Object | None = None) -> None:
        text: str = self.__source__[self.__start__ : self.__current__]
        self.__tokens__.append(Token(_type, text, literal, self.__line__))