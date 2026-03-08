from unittest import TestCase


class EventList(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.rat_enters = EventList()
        self.rat_dies = EventList()
        self.notify_rat = EventList()


class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1

        self.game.rat_enters.append(self.rat_enters)
        self.game.notify_rat.append(self.notify_rat)
        self.game.rat_dies.append(self.rat_dies)

        self.game.rat_enters(self)

    def rat_enters(self, which_rat):
        if which_rat != self:
            self.attack += 1
            self.game.notify_rat(which_rat)

    def notify_rat(self, which_rat):
        if which_rat == self:
            self.attack += 1

    def rat_dies(self, which_rat):
        self.attack -= 1

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.game.rat_dies(self)

    def __repr__(self):
        return f"Rat: {self.attack}"


class Evaluate(TestCase):
    def test_single_rat(self):
        game = Game()
        rat = Rat(game)
        self.assertEqual(1, rat.attack)

    def test_two_rats(self):
        game = Game()
        rat = Rat(game)
        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

    def test_three_rats_one_dies(self):
        game = Game()

        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)


if __name__ == "__main__":
    game = Game()

    rat = Rat(game)
    print(rat)
    rat2 = Rat(game)

    print(rat)
    print(rat2)

    with Rat(game) as rat3:
        print(rat3)

    print(rat)
    print(rat2)
