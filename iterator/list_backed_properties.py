class Creature:
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self) -> None:
        self.stats = [10, 10, 10]

    @property
    def strength(self):
        return self.stats[Creature._strength]

    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength] = value

    @property
    def intelligence(self):
        return self.stats[Creature._intelligence]

    @intelligence.setter
    def intelligence(self, value):
        self.stats[Creature._intelligence] = value

    @property
    def agility(self):
        return self.stats[Creature._agility]

    @agility.setter
    def agility(self, value):
        self.stats[Creature._agility] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def average_stat(self):
        return float(sum(self.stats) / len(self.stats))

    def __iter__(self):
        return self

    def __next__(self):
        yield self.strength
        yield self.agility
        yield self.intelligence
        raise StopIteration


if __name__ == "__main__":
    creature = iter(Creature())
    strength = next(creature)
    agility = next(creature)
    intelligence = next(creature)

    print(f"{strength}, {agility}, {intelligence}")
