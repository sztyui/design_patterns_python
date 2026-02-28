from enum import Enum


class CreatureType(Enum):
    GOBLIN = 1
    GOBLINKING = 2


class Creature:
    pass


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        self.game = game
        self.base_attack = attack
        self.base_defense = defense
        self.type = CreatureType.GOBLIN

    @property
    def defense(self):
        return self.base_defense + len(self.game.creatures) - 1

    @property
    def attack(self):
        gk_persist = any(
            [x.type == CreatureType.GOBLINKING for x in self.game.creatures]
        )
        return self.base_attack + 1 if gk_persist else self.base_attack


class GoblinKing(Goblin):
    def __init__(self, game, attack=3, defense=3):
        super().__init__(game, attack, defense)
        self.type = CreatureType.GOBLINKING


class Game:
    def __init__(self):
        self.creatures = []


def test_game():
    game = Game()
    goblin = Goblin(game)
    goblin2 = GoblinKing(game)
    game.creatures.append(goblin)
    game.creatures.append(goblin2)

    assert 2 == goblin.attack
    assert 2 == goblin.defense
