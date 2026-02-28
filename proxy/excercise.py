"""
Proxy Coding Exercise
You are given the Person  class and asked to write a ResponsiblePerson  proxy that does the following:

Allows person to drink unless they are younger than 18 (in that case, return "too young")

Allows person to drive unless they are younger than 16 (otherwise, "too young")

In case of driving while drink, returns "dead", regardless of age
"""


class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return "drinking"

    def drive(self):
        return "driving"

    def drink_and_drive(self):
        return "driving while drunk"


class ResponsiblePerson:
    def __init__(self, person):
        self.person = person

    # todo: rest of this class
    def drink(self):
        if self.person.age < 18:
            return "too young"
        else:
            return self.person.drink()

    def drive(self):
        return self.person.drive() if self.person.age >= 16 else "too young"

    def drink_and_drive(self):
        return "dead"
