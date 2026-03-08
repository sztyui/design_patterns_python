from abc import ABC


class Game(ABC):
    def __init__(self, number_of_players) -> None:
        self.number_of_players = number_of_players
        self.current_player = 0

    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f"Player {self.winning_player} wins!")

    def start(self):
        pass

    @property
    def have_winner(self) -> bool:
        pass

    def take_turn(self):
        pass

    @property
    def winning_player(self) -> int:
        pass


class Chess(Game):
    def __init__(self):
        super().__init__(2)
        self.max_turns = 10
        self.turn = 1

    def start(self):
        print(f"Starting a game of chess with {self.number_of_players} players")

    @property
    def have_winner(self) -> bool:
        return self.turn == self.max_turns

    def take_turn(self):
        print(f"Turn {self.turn} taken by player {self.current_player}")
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self) -> int:
        return self.current_player


if __name__ == "__main__":
    chess = Chess()
    chess.run()
