from abc import ABC


class Summarizer(ABC):
    @property
    def sum(self):
        if hasattr(self, "value"):
            return self.value

        return sum(list(x if isinstance(x, int) else x.sum for x in self.values))


class SingleValue(Summarizer):
    def __init__(self, value):
        self.value = value


class ManyValues(list, Summarizer):
    def __init__(self):
        super().__init__()
        self.values = []

    def append(self, value):
        self.values.append(value)
