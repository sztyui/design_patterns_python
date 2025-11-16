from enum import Enum
from math import atan2, cos, sin, sqrt


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y, a=0):
        self.x = x
        self.y = y
        self.a = a

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    def return_from_polar(self):
        rho = sqrt(self.x**2 + self.y**2)
        theta = atan2(self.y, self.x)
        return rho, theta

    class PointFactory:
        def new_cartesian_point(self, x, y):
            return Point(x, y)

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta), rho)

    factory = PointFactory()


if __name__ == "__main__":
    p = Point(2, 3)
    p2 = Point.factory.new_polar_point(1, 2)

    print(p, p2)
    print(p2.return_from_polar())
