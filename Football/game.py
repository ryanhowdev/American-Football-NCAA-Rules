class Game:
    def __init__(self, teams):
        self.teams = teams
        self.clock = Clock(60)  # Game duration in minutes
        self.scoreboard = Scoreboard()
        self.field = Field()
        self.current_possession_team_index = 0  # Index of the team currently having the ball

    def start_game(self):
        self.clock.start()
        # Start the game loop here, e.g., kickoff

    def execute_play(self, play):
        self.current_play = play
        play.trigger()

    def possession_change(self):
        # Change possession between the two teams
        self.current_possession_team_index = 1 - self.current_possession_team_index
        self.field.position = 100 - self.field.position  # Reset field position based on new possession

    def update_game_state(self):
        # General updates after each play
        self.clock.update(5)  # Assume each play takes approximately 5 seconds
        print(f"Time remaining: {self.clock.time_left} seconds, Possession: {self.teams[self.current_possession_team_index].name}")

    def handle_event(self, event_type, details):
        # Event handling logic based on the type of event
        if event_type == 'score_update':
            self.scoreboard.update_score(details['team'], details['points'])
        elif event_type == 'field_position_change':
            self.field.move_ball(details['yards'])
        elif event_type == 'possession_change':
            self.possession_change()
        # Add other event types as needed

    def end_half(self):
        if self.current_half == 1:
            print("End of First Half.")
            self.current_half += 1
            self.clock.time_left = 60 * 15  # Reset for the second half
        else:
            print("End of Game.")
            self.clock.stop()
    
    def call_timeout(self, team):
        if self.teams[self.current_possession_team_index] == team and team.timeouts_remaining > 0:
            team.timeouts_remaining -= 1
            self.clock.stop()
            print(f"Timeout called by {team.name}. Timeouts remaining: {team.timeouts_remaining}")
            self.handle_event('timeout', {})
