class Scoreboard:
    def __init__(self):
        self.score = {'Home': 0, 'Visitor': 0}
        self.downs = 1
        self.yards_to_go = 10

    def update_score(self, team, points):
        if team in self.score:
            self.score[team] += points

    def update_downs(self, down):
        self.downs = down

    def update_yards_to_go(self, yards):
        self.yards_to_go = yards
