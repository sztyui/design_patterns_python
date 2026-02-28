import csv
import unittest
from typing import Any


class Singleton(type):
    _instances: dict[Any, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        with open(
            r"C:\Users\I10815\Desktop\design_patterns_course\singleton\capitals.txt",
            "r",
            encoding="utf-8",
        ) as f:
            reader = csv.reader(f, delimiter=",", quotechar='"')
            next(reader, None)
            for row in reader:
                self.population[row[1]] = int(row[4])


class SingletonRecordFinder:
    def total_population(self, cities):
        return sum(Database().population.get(c, 0) for c in cities)


class ConfigurableRecordFinder:
    def __init__(self, db=Database()):
        self.db = db

    def total_population(self, cities):
        return sum(self.db.population.get(c, 0) for c in cities)


class DummyDatabase(metaclass=Singleton):
    population = {
        "alpha": 1,
        "beta": 2,
        "gamma": 3,
    }

    def get_population(self, name):
        return self.population[name]


class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder().total_population(
            ["Seoul", "Ciudad de México (Mexico City)"]
        )
        self.assertEqual(rf, 31544324)

    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        crf = ConfigurableRecordFinder(SingletonTests.ddb)
        self.assertEqual(3, crf.total_population(["alpha", "beta"]))


if __name__ == "__main__":
    unittest.main()
