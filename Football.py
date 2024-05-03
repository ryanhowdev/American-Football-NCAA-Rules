import random

class Clock:
    def __init__(self, total_minutes=60):
        self.total_seconds = total_minutes * 60
        self.time_left = self.total_seconds
        self.running = False

    def update_status(self):
        if self.time_left <= 120:
            return 'last_two_minutes_first_half'
        elif self.time_left <= 300:
            return 'last_five_minutes_second_half'
        return None

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def update(self, seconds_passed):
        if self.running:
            self.time_left -= seconds_passed
            self.time_left = max(0, self.time_left)

    def handle_event(self, event_type):
        if event_type in ['incomplete_pass', 'end_of_quarter', 'scoring_play']:
            self.stop()

class Scoreboard:
    def __init__(self):
        self.score = {'Home': 0, 'Visitor': 0}

    def update_score(self, team, points):
        self.score[team] += points

class Field:
    def __init__(self):
        self.position = 50

    def move_ball(self, yards):
        self.position += yards
        self.position = max(0, min(100, self.position))

class Player:
    def __init__(self, player_id, name, position):
        self.player_id = player_id
        self.name = name
        self.position = position
        self.stats = {}

class Team:
    def __init__(self, name):
        self.name = name
        self.players = {}
        self.timeouts_remaining = 3

    def add_player(self, player):
        self.players[player.player_id] = player

class Event:
    def __init__(self, game, name):
        self.game = game
        self.name = name

    def trigger(self):
        pass

class Play(Event):
    def __init__(self, game, play_type, details):
        super().__init__(game, 'play')
        self.play_type = play_type
        self.details = details

    def trigger(self):
        if self.play_type == 'touchdown':
            self.game.scoreboard.update_score(self.game.teams[self.game.current_possession_team_index].name, 6)
            self.game.clock.stop()

class Game:
    def __init__(self, teams):
        self.teams = teams
        self.clock = Clock(60)
        self.scoreboard = Scoreboard()
        self.field = Field()
        self.current_possession_team_index = 0

    def start_game(self):
        self.clock.start()

    def execute_play(self, play):
        play.trigger()

    def update_game_state(self):
        critical_timing = self.clock.update_status()
        if critical_timing:
            print(f"Special timing rules applied for {critical_timing}.")

    def possession_change(self):
        self.current_possession_team_index = 1 - self.current_possession_team_index

def main():
    team1 = Team("Home")
    team2 = Team("Visitor")
    game = Game([team1, team2])
    game.start_game()

    # Simulate a touchdown
    touchdown_play = Play(game, 'touchdown', {'yards': 75})
    game.execute_play(touchdown_play)
    game.update_game_state()
    print(f"Score: {game.scoreboard.score}")
    print(f"Game Time Left: {game.clock.time_left/60} minutes")

if __name__ == '__main__':
    main()

