# 1 + (2+3)


from abc import ABC


class Expression(ABC):
    def print(self, buffer):
        pass

    def eval(self, eval):
        pass


class DoubleExpression(Expression):
    def __init__(self, value) -> None:
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ExpressionPrinter:
    @staticmethod
    def print(e, buffer):
        if isinstance(e, DoubleExpression):
            buffer.append(str(e.value))
        elif isinstance(e, AdditionExpression):
            buffer.append("(")
            ExpressionPrinter.print(e.left, buffer)
            buffer.append("+")
            ExpressionPrinter.print(e.right, buffer)
            buffer.append(")")

    Expression.print = lambda self, b: ExpressionPrinter.print(self, b)


class ExpressionEvaluator:
    @staticmethod
    def eval(expression):
        if isinstance(expression, DoubleExpression):
            return expression.value
        elif isinstance(expression, AdditionExpression):
            return ExpressionEvaluator.eval(expression.left) + ExpressionEvaluator.eval(
                expression.right
            )

    Expression.eval = lambda self: ExpressionEvaluator.eval(self)


if __name__ == "__main__":
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(DoubleExpression(2), DoubleExpression(3)),
    )

    buffer = []
    e.print(buffer)
    print("".join(buffer), " = ", e.eval())
