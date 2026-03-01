from project.player import Player

class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: list[Player] = []

    @property
    def name(self):
        return self.__name

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name: str):
        player_to_remove = next((p for p in self.__players if p.name == player_name), None)
        if player_to_remove:
            self.__players.remove(player_to_remove)
            return player_to_remove
        return f"Player {player_name} not found"