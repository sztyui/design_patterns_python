# event broker (observer)
# cqs


from abc import ABC
from enum import Enum


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQUery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name, what_to_query, default_value) -> None:
        self.creature_name = creature_name
        self.what_to_query = what_to_query
        self.value = default_value


class Game:
    def __init__(self) -> None:
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)


class CreatureModifier(ABC):
    def __init__(self, game, creature) -> None:
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if (
            sender.name == self.creature.name
            and query.what_to_query == WhatToQUery.ATTACK
        ):
            query.value *= 2


class Creature:
    def __init__(self, game, name, attack, defense):
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        q = Query(self.name, WhatToQUery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQUery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self) -> str:
        return f"{self.name} ({self.attack}/{self.defense})"


if __name__ == "__main__":
    game = Game()
    goblin = Creature(game, "Strong Goblin", 2, 2)
    print(goblin)

    with DoubleAttackModifier(game, goblin):
        print(goblin)
    print(goblin)
