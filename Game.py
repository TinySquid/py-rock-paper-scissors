import random


class GameManager:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.choices = ["r", "p", "s"]

    def get_npc_choice(self):
        return random.choice(self.choices)

    def get_player_choice(self):
        return input("-> ")

    def get_score(self):
        return f"Score: {self.wins} / {self.losses} / {self.ties}"

    def get_result(self, player_choice, npc_choice):
        # Thanks to David Nagy (DS8) for the win_matrix
        win_matrix = {
            "r": {"r": 0, "p": -1, "s": 1},
            "p": {"r": 1, "p": 0, "s": -1},
            "s": {"r": -1, "p": 1, "s": 0},
        }

        result = win_matrix[player_choice][npc_choice]

        if result == 0:
            # Player tied
            self.ties += 1
            return "You tied!"
        elif result == 1:
            # Player wins
            self.wins += 1
            return "You win!"
        elif result == -1:
            # Player loses
            self.losses += 1
            return "You lost!"

    def play(self, player_choice):
        return self.get_result(player_choice, self.get_npc_choice())

