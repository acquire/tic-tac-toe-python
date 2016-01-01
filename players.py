from player import Player


class Players:

    def __init__(self):
        self.players = []
        self.current = None

    def create_player(self, mark):
        player = Player(mark)
        self.players.append(player)
        return player

    def switch_players(self):
        for p in self.players:
            if p != self.current:
                self.current = p
                break

