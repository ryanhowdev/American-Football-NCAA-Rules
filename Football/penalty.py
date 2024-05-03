class Penalty(Event):
    def __init__(self, game, penalty_type, team_affected):
        super().__init__(game, 'penalty')
        self.penalty_type = penalty_type
        self.team_affected = team_affected

    def trigger(self):
        # Handle the penalty effect on the game state here
        if self.penalty_type == 'delay_of_game':
            self.game.clock.handle_event('stop')
        # Add other penalties and their specific effects
        self.game.update_game_state()

