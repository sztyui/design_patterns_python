import copy
from dataclasses import dataclass


@dataclass
class Address:
    city: str
    street_address: str
    country: str

    def __str__(self) -> str:
        return f"{self.street_address}, {self.city}, {self.country}"


@dataclass
class Person:
    name: str
    address: Address

    def __str__(self):
        return f"{self.name} lives at {self.address}"


john = Person("John", Address("London", "123 London Road", "UK"))
jane = copy.deepcopy(john)
jane.address.street_address = "123B London Road"

print("---")
print(john)
print(jane)
