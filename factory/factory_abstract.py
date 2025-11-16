from abc import ABC, abstractmethod
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This tea is  delicious.")


class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious.")


class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount) -> HotDrink:
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount) -> Tea:
        print(f"Put in tea bag, boil water, pour {amount}ml, enjoy! ")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount) -> Coffee:
        print(f"Grind some beans, boil water, pour {amount}ml, enjoy!")
        return Coffee()


def make_drink(type):
    if type == "tea":
        return TeaFactory().prepare(200)
    elif type == "coffee":
        return CoffeeFactory().prepare(50)
    else:
        raise AttributeError("unknown type: {type}")


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories: list[tuple[str, HotDrinkFactory]] = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name.capitalize()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((factory_name, factory_instance))

    def make_drink(self):
        print("Available drinks:")
        for idx, f in enumerate(self.factories):
            print(f"{idx+1}: {f[0]}")

        s = input(f"Please pick drink (1-{len(self.factories)}): ")
        idx = int(s) - 1
        s = input(f"Specify amount: ")
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == "__main__":
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
