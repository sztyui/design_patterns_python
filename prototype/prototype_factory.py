import copy
from dataclasses import dataclass


@dataclass
class Address:
    city: str
    suite: int
    street_address: str

    def __str__(self) -> str:
        return f"{self.street_address}, Suite: #{self.suite}, {self.city}"


@dataclass
class Employee:
    name: str
    address: Address

    def __str__(self):
        return f"{self.name} lives at {self.address}"


class EmployeeFactory:
    main_office_employee = Employee("", Address("123 East Drive", 0, "London"))
    aux_office_employee = Employee("", Address("123B East Drive", 0, "London"))

    @staticmethod
    def __new_employee(proto: Employee, name: str, suite: int):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name: str, suite: int):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name, suite
        )

    @staticmethod
    def new_aux_office_employee(name: str, suite: int):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee, name, suite
        )


if __name__ == "__main__":
    john = EmployeeFactory.new_main_office_employee("John", 101)
    jane = EmployeeFactory.new_aux_office_employee("Jane", 500)

    print(john)
    print(jane)
