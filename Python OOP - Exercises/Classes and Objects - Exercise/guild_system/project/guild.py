from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = list()

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if all(x.name != player_name for x in self.players):
            return f"Player {player_name} is not in the guild."

        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.remove(player)
                return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}"
        for player in self.players:
            result += f"\n{player.player_info()}"
        return result
