class Sentence:
    class WordFormatter:
        def __init__(self, word, capitalize=False):
            self.word = word
            self.capitalize = capitalize

        def __str__(self) -> str:
            return self.word.upper() if self.capitalize else self.word

    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.words = [self.WordFormatter(w) for w in plain_text.split(" ")]

    def __getitem__(self, index):
        if index > len(self.words):
            raise IndexError("index unreachable for words")

        return self.words[index]

    def __str__(self):
        return " ".join([str(w) for w in self.words])


if __name__ == "__main__":
    sentence = Sentence("hello world")
    sentence[1].capitalize = True
    print(sentence)  # writes "hello WORLD"
