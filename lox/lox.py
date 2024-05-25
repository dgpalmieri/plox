"""
This file implements the "Lox" interface from Robert Nystrom's
"Crafting Interpreters"
"""

from pathlib import Path

from lox.token import Token
from lox.lexer import Lexer


class Lox:
    hadError: bool = False

    @staticmethod
    def main(args: list[str]) -> None:
        """
        Runs a script if given a single file, or the
        REPL if no args are given
        """

        if len(args) > 1:
            print("Usage: plox [script]")
        elif len(args) == 1:
            Lox.__run_file__(Path(args[0]))
        else:
            Lox.__repl__()

    @staticmethod
    def __run_file__(file_path: Path) -> None:
        with open(file_path) as file:
            Lox.__run__(file.read())

    @staticmethod
    def __repl__() -> None:
        print("-- Empty line to exit --")
        while True:
            line = input("> ")
            if not line:
                break
            Lox.__run__(line)
            Lox.hadError = False

    @staticmethod
    def __run__(source: str) -> None:
        if Lox.hadError:
            exit(65)

        lexer: Lexer = Lexer(source)
        tokens: list[Token] = lexer.scan_tokens()

        for t in tokens:
            print(t)

    @staticmethod
    def error(line: int, message: str) -> None:
        Lox.__report__(line, "", message)

    @staticmethod
    def __report__(line: int, where: str, message: str) -> None:
        print(f"[line {line}] Error {where}: {message}")
        Lox.hadError = True
