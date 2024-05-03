class Team:
    def __init__(self, name):
        self.name = name
        self.roster = {}

    def add_player(self, player):
        self.roster[player.player_id] = player

    def get_player_stats(self, player_id):
        return self.roster[player_id].stats if player_id in self.roster else None
