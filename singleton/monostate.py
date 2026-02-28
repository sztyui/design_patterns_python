from typing import Any, Dict

from typing_extensions import Self


class CEO:
    __shared_state = {"name": "Steve", "age": 55}

    def __init__(self) -> None:
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f"{self.name} is {self.age} years old"  # type: ignore


class Monostate:
    _shared_state: Dict[str, Any] = {}

    def __new__(cls, *args, **kwargs) -> Self:
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ""
        self.money_managed = 0

    def __str__(self):
        return f"{self.name} manages ${self.money_managed}bn"


if __name__ == "__main__":
    cfo1 = CFO()
    cfo1.name = "Sheryl"
    cfo1.money_managed = 1
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = "Ruth"
    cfo2.money_managed = 10

    print(cfo1)
    print(cfo2)
