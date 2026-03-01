"""
Interpreter Coding Exercise
You are asked to write an expression processor for simple numeric expressions with the following constraints:

Expressions use integral values (e.g., '13' ), single-letter variables defined in Variables, as well as + and - operators only

There is no need to support braces or any other operations

If a variable is not found in variables  (or if we encounter a variable with >1 letter, e.g. ab), the evaluator returns 0 (zero)

In case of any parsing failure, evaluator returns 0

Example:

calculate("1+2+3")  should return 6

calculate("1+2+xy")  should return 0

calculate("10-2-x")  when x=3 is in variables  should return 5
"""

from enum import Enum, auto
from typing import Tuple


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        MULTIPLY = auto()
        VARIABLE = auto()

    def __init__(self, value: str, type: Type):
        self.value = value
        self.type = type

    def __str__(self):
        return f"`{self.value}`"

    def __repr__(self):
        return f"`${self.value}`"


class BinaryOperation:
    class Type(Enum):
        ADD = auto()
        SUBTRACT = auto()
        MULTIPLY = auto()

    def __init__(self, type: Type = Type.ADD, left=0, right=0) -> None:
        self.type: BinaryOperation.Type = type
        self.left: int = left
        self.right: int = right

    def __str__(self):
        operation = "ADD" if self.type == BinaryOperation.Type.ADD else "SUB"
        return f"Left: {self.left}, Right: {self.right}, Operation: {operation}"

    @property
    def value(self) -> int:
        if self.type == BinaryOperation.Type.ADD:
            return self.left + self.right
        elif self.type == BinaryOperation.Type.MULTIPLY:
            if self.right == 0:
                self.right = 1
            return self.left * self.right
        else:
            return self.left - self.right


def switch(
    op: BinaryOperation, tok: Token, has_left: bool, variables
) -> Tuple[BinaryOperation, bool]:
    retop = op
    value = (
        variables.get(tok.value, 0)
        if tok.type == Token.Type.VARIABLE
        else int(tok.value)
    )
    if not has_left:
        retop.left = value
        return retop, True
    else:
        retop.right = value
        retop.left, retop.right = op.value, 0
        return retop, True


def parser(tokens, variables):
    DEFAULT = BinaryOperation(BinaryOperation.Type.ADD, 0, 0)
    op = BinaryOperation()
    has_left = False
    for tok in tokens:
        match tok.type:
            case Token.Type.INTEGER:
                op, has_left = switch(op, tok, has_left, variables)
            case Token.Type.PLUS:
                op.type = BinaryOperation.Type.ADD
            case Token.Type.MINUS:
                op.type = BinaryOperation.Type.SUBTRACT
            case Token.Type.MULTIPLY:
                op.type = BinaryOperation.Type.MULTIPLY
            case Token.Type.VARIABLE:
                if len(tok.value) > 1:
                    return DEFAULT
                op, has_left = switch(op, tok, has_left, variables)
    return op


def lexer(expression):
    tokens = []
    index = 0
    while index < len(expression):
        char = expression[index]
        if char == "+":
            tokens.append(Token(char, Token.Type.PLUS))
        elif char == "-":
            tokens.append(Token(char, Token.Type.MINUS))
        elif char.isdigit():
            number = [char]
            for j in range(index + 1, len(expression)):
                if expression[j].isdigit():
                    number.append(expression[j])
                    index += 1
                else:
                    break
            tokens.append(Token("".join(number), Token.Type.INTEGER))
        elif char == "*":
            tokens.append(Token(char, Token.Type.MULTIPLY))
        else:
            variable = [char]
            for j in range(index + 1, len(expression)):
                if expression[j].isalpha():
                    variable.append(expression[j])
                    index += 1
                else:
                    break
            tokens.append(Token("".join(variable), Token.Type.VARIABLE))
        index += 1
    return tokens


class ExpressionProcessor:
    def __init__(self):
        self.variables = {"x": 4}

    def calculate(self, expression):
        tokens = lexer(expression)
        parsed = parser(tokens, self.variables)
        print(f"{expression} = {parsed.value}")


if __name__ == "__main__":
    exp = ExpressionProcessor()
    exp.calculate("1+2+3+15-23*2")
    exp.calculate("1+2*x")
