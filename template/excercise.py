from abc import ABC


class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack

    def alive(self):
        return self.health > 0


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        f = self.creatures[c1_index]
        s = self.creatures[c2_index]
        self.hit(f, s)
        self.hit(s, f)
        if f.alive == s.alive:
            return -1
        if f.alive:
            return c1_index
        if s.alive:
            return c2_index

    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature):
        if (defender.health - attacker.attack) > 0:
            pass
        else:
            defender.health -= attacker.attack


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature):
        defender.health -= attacker.attack
