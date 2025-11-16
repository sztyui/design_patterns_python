import random

from typing_extensions import Self


class Database:
    _instance = None

    def __init__(self):
        id = random.randint(1, 101)
        print("id =", id)

    def __new__(cls, *args, **kwargs) -> Self:
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
