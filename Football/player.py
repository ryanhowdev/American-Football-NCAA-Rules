class Player:
    def __init__(self, player_id, name, position):
        self.player_id = player_id
        self.name = name
        self.position = position
        self.stats = {'yards': 0, 'touchdowns': 0, 'interceptions': 0, 'tackles': 0}

    def update_stats(self, stat_type, value):
        if stat_type in self.stats:
            self.stats[stat_type] += value
