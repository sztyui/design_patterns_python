class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.chat_log: list[str] = []
        self.room: ChatRoom | None = None

    def receive(self, sender, message):
        s = f"{sender}: {message}"
        print(f"[{self.name}'s chat session] {s}")
        self.chat_log.append(s)

    def private_message(self, who, message):
        if self.room:
            self.room.message(self.name, who, message)

    def say(self, message):
        if self.room:
            self.room.broadcast(self.name, message)


class ChatRoom:
    def __init__(self) -> None:
        self.people: list[Person] = []

    def join(self, person):
        join_msg = f"{person.name} joins the chat"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def message(self, source, destination, message):
        # aim = next(filter(lambda p: p.name == destination, self.people))
        # if aim:
        #     aim.receive(source, self.message)
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)


if __name__ == "__main__":
    room = ChatRoom()

    john = Person("John")
    jane = Person("Jane")

    room.join(john)
    room.join(jane)

    john.say("hi room!")
    jane.say("ho, hey john")

    simon = Person("Simon")
    room.join(simon)
    simon.say("Hi everyone!")

    jane.private_message("Simon", "glad you could join us!")
