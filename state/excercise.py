import unittest


class Status:
    LOCKED = "LOCKED"
    OPEN = "OPEN"
    ERROR = "ERROR"


class CombinationLock:
    def __init__(self, combination: list) -> None:
        self._status: str = Status.LOCKED
        self.entered: list[int] = []
        self.combination: list[int] = combination

    def reset(self):
        self.status = Status.LOCKED
        self.entered = []

    def enter_digit(self, digit):
        if digit == self.combination[len(self.entered)]:
            self.entered.append(digit)
        else:
            self._status = Status.ERROR

        if self.entered == self.combination:
            self.status = Status.OPEN

    @property
    def status(self):
        if self.entered and not (
            self._status == Status.ERROR or self._status == Status.OPEN
        ):
            return "".join(map(str, self.entered))
        else:
            return self._status

    @status.setter
    def status(self, value: str):
        if value == Status.LOCKED or value == Status.OPEN or value == Status.ERROR:
            self._status = value

    def __repr__(self) -> str:
        tmp = "".join([str(x) for x in self.entered])
        if not self.entered:
            tmp = "<empty>"
        return (
            f"Combination({self._status}[" + "*" * len(self.combination) + "]): " + tmp
        )


class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual("LOCKED", cl.status)
        cl.enter_digit(1)
        self.assertEqual("1", cl.status)
        cl.enter_digit(2)
        self.assertEqual("12", cl.status)
        cl.enter_digit(3)
        self.assertEqual("123", cl.status)
        cl.enter_digit(4)
        self.assertEqual("1234", cl.status)
        cl.enter_digit(5)
        self.assertEqual("OPEN", cl.status)

    def test_failure(self):
        cl = CombinationLock([1, 2, 3])
        self.assertEqual("LOCKED", cl.status)
        cl.enter_digit(1)
        self.assertEqual("1", cl.status)
        cl.enter_digit(2)
        self.assertEqual("12", cl.status)
        cl.enter_digit(5)
        self.assertEqual("ERROR", cl.status)


if __name__ == "__main__":
    c1 = CombinationLock([1, 2, 3])
    print(c1.status)
    c1.enter_digit(1)
    c1.enter_digit(2)
    c1.enter_digit(5)
    print(c1.status)
    print(c1)
