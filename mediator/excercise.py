import unittest


class Participant:
    _part_counter = 1

    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        self._id = Participant._part_counter
        Participant._part_counter += 1
        self.mediator.join(self)

    def say(self, value):
        self.mediator.broadcast(self, value)

    def __eq__(self, other):
        return self._id == other._id

    def __repr__(self):
        return f"Participant({self._id}): {self.value}"


class Mediator:
    def __init__(self) -> None:
        self.participants: list[Participant] = []

    def join(self, participant):
        if not participant in self.participants:
            self.participants.append(participant)

    def broadcast(self, participant, value):
        for part in self.participants:
            if part != participant:
                part.value = value


class FirstTestSuite(unittest.TestCase):
    def test(self):
        m = Mediator()
        p1 = Participant(m)
        p2 = Participant(m)

        self.assertEqual(0, p1.value)
        self.assertEqual(0, p2.value)

        p1.say(2)

        self.assertEqual(0, p1.value)
        self.assertEqual(2, p2.value)

        p2.say(4)

        self.assertEqual(4, p1.value)
        self.assertEqual(2, p2.value)


if __name__ == "__main__":
    sys = Mediator()
    part1 = Participant(sys)
    part2 = Participant(sys)

    print(part1)
    print(part2)
    print(" ========== \n")

    part1.say(2)
    print(part1)
    print(part2)
    print(" ========== \n")

    part2.say(4)
    print(part1)
    print(part2)
    print(" ========== \n")
