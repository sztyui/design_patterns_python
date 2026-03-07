from copy import deepcopy
from unittest import TestCase


class Token:
    def __init__(self, value=0):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Memento(list):
    def __init__(self, value) -> None:
        super().__init__(value)


class TokenMachine:
    def __init__(self) -> None:
        self.tokens: list[Token] = []

    def add_token_value(self, value) -> Memento:
        return self.add_token(Token(value))

    def add_token(self, token) -> Memento:
        self.tokens.append(token)
        return Memento(deepcopy(self.tokens))

    def revert(self, memento) -> None:
        self.tokens = memento

    def __str__(self) -> str:
        r = "TokenMachine: \n"
        for token in self.tokens:
            r += f"\t{token}\n"
        return r


if __name__ == "__main__":
    tm = TokenMachine()
    m = tm.add_token_value(123)
    m2 = tm.add_token_value(456)
    print(tm)
