from abc import ABC, abstractmethod
from ast import And
from enum import Enum
from typing import Any, Generator, List


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name: str, color: Color, size: Size):
        self.name: str = name
        self.color: Color = color
        self.size: Size = size

    def __str__(self) -> str:
        return f"Product(name={self.name}, color={self.color}, size={self.size})"


class ProductColorFilter:
    @staticmethod
    def filter(products: list[Product], color: Color) -> Generator[Product, Any, None]:
        for p in products:
            if p.color == color:
                yield p


class ProductSizeFilter:
    @staticmethod
    def filter(products: list[Product], size: Size) -> Generator[Product, Any, None]:
        for p in products:
            if p.size == size:
                yield p


# Specification
class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, item: Product) -> bool:
        ...

    def __and__(self, other):
        return AndSpecifictication(self, other)


class Filter(ABC):
    @abstractmethod
    def filter(self, items: list, spec: Specification) -> Generator[Any, Any, None]:
        ...


class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Product):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item: Product):
        return item.size == self.size


class AndSpecifictication(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item: Product) -> bool:
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(
        self, items: list, spec: Specification
    ) -> Generator[Any, Any, None]:  # -> Generator[Any, Any, None]:
        for item in items:
            if spec.is_satisfied(item):
                yield item


class ProductFilter:
    def filter_by_color(
        self, products: List[Product], color: Color
    ) -> Generator[Product, Any, None]:
        for p in products:
            if p.color == color:
                yield p


if __name__ == "__main__":
    # create random products
    p1 = Product("Apple", Color.RED, Size.SMALL)
    p2 = Product("Tree", Color.GREEN, Size.LARGE)
    p3 = Product("House", Color.BLUE, Size.MEDIUM)
    p4 = Product("Car", Color.RED, Size.MEDIUM)
    p5 = Product("Ball", Color.GREEN, Size.SMALL)
    p6 = Product("Sky", Color.BLUE, Size.LARGE)

    products = [p1, p2, p3, p4, p5, p6]
    pf = ProductFilter()
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f" - {p.name} is green")

    bf = BetterFilter()

    print("Green products (new):")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f" - {p.name} is green")

    print("Large products (new):")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name} is large")

    print("Large and blue products (new):")
    large_blue = large & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is large and blue")
