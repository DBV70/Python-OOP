class SteamUser:
    def __init__(self, username: str, games: list):
        self.username = username
        self.games = games

    played_hours = 0

    def play(self, game:str, hours:int):
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self, game:str):
        if game not in self.games:
            self.games.append(game)
            return F"{self.username} bought {game}"
        else:
            return f"{game} is already in your library"

    def status(self):
        return F"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"

# Test code
user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())