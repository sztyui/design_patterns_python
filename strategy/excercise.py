import cmath
import math
from abc import ABC
from typing import Any
from unittest import TestCase


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c) -> Any:
        return math.pow(b, 2) - (4 * a * c)


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c) -> Any:
        res = math.pow(b, 2) - (4 * a * c)
        if res < 0:
            return float("nan")
        return res


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """Returns a pair of complex (!) values"""
        d = complex(
            self.strategy.calculate_discriminant(
                a,
                b,
                c,
            ),
            0,
        )
        root = cmath.sqrt(d)
        return ((-b + root) / (2 * a), (-b - root) / (2 * a))


class Evaluate(TestCase):
    def test_positive_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_positive_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_negative_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertEqual(complex(-2, 1), results[0])
        self.assertEqual(complex(-2, -1), results[1])

    def test_negative_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertTrue(math.isnan(results[0].real))
        self.assertTrue(math.isnan(results[1].real))
        self.assertTrue(math.isnan(results[0].imag))
        self.assertTrue(math.isnan(results[1].imag))
