# SRP SOC


from urllib import request


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as file:
            file.write(str(journal))

    @staticmethod
    def load_from_file(filename) -> Journal:
        j = Journal()
        with open(filename, "r") as file:
            data = file.readlines()
            j.entries = [line.strip() for line in data]
        return j

    @staticmethod
    def load_from_web(uri) -> Journal:
        j = Journal()
        with request.urlopen(uri) as response:
            data = response.read().decode()
            for line in data.splitlines():
                j.add_entry(line.strip())
        return j


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")

PersistenceManager.save_to_file(j, "journal.txt")
loaded_journal = PersistenceManager.load_from_file("journal.txt")
print(loaded_journal)
