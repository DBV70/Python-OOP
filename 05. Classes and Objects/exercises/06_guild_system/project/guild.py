from .player import Player

class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: list[Player] = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"


    def kick_player(self, player: str):
        for p in self.players:
            if p.name == player:
                self.players.remove(p)
                p.guild = "Unaffiliated"
                return f"Player {player} has been removed from the guild."
        return f"Player {player} is not in the guild."

    def guild_info(self):
        result = [f"Guild: {self.name}"]
        for p in self.players:
            result.append(f"{p.player_info()}")
        return '\n'.join(result)

# Test code
# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())