from lox.token import Token
from lox.token_type import TokenType
from lox.lox import Lox


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
        elif c == "!":
            self.__add_token__(
                TokenType.BANG_EQUAL if self.__match__("=") else TokenType.BANG
            )
        elif c == "=":
            self.__add_token__(
                TokenType.EQUAL_EQUAL if self.__match__("=") else TokenType.EQUAL
            )
        elif c == "<":
            self.__add_token__(
                TokenType.LESS_EQUAL if self.__match__("=") else TokenType.LESS
            )
        elif c == ">":
            self.__add_token__(
                TokenType.GREATER_EQUAL if self.__match__("=") else TokenType.GREATER
            )
        elif c == "/":
            if self.__match__("/"):
                while self.__peek__() != "\n" and self.is_at_end():
                    _ = self.__advance__()
            else:
                self.__add_token__(TokenType.SLASH)
        elif c == " " or c == "\r" or c == "\t":
            return
        elif c == "\n":
            self.__line__ = self.__line__ + 1
        elif c == '"':
            self.__string__()
        else:
            Lox.error(self.__line__, f"Unexpected character: {c}")

    def __advance__(self) -> str:
        if self.__current__ + 1 <= len(self.__source__):
            return self.__source__[self.__current__ + 1]
        return "End of String"

    def __add_token__(self, _type: TokenType, literal: object | None = None) -> None:
        text: str = self.__source__[self.__start__ : self.__current__]
        self.__tokens__.append(Token(_type, text, literal, self.__line__))

    def __match__(self, expected: str) -> bool:
        if self.is_at_end():
            return False
        if self.__source__[self.__current__] != expected:
            return False

        self.__current__ = self.__current__ + 1
        return True

    def __peek__(self) -> str:
        if self.is_at_end():
            return "\0"
        return self.__source__[self.__current__]

    def __string__(self) -> None:
        while self.__peek__() != '"' and not self.is_at_end():
            if self.__peek__() == "\n":
                self.__line__ = self.__line__ + 1
            _ = self.__advance__()

        if self.is_at_end():
            Lox.error(self.__line__, "Unterminated string")
            return

        _ = self.__advance__()

        value: str = self.__source__[self.__start__ + 1 : self.__current__ - 1]
        self.__add_token__(TokenType.STRING, value)
