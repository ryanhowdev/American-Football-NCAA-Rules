class Play(Event):
    def __init__(self, game, play_type, details):
        super().__init__(game, 'play')
        self.play_type = play_type
        self.details = details  # Details such as yards gained, player involved, etc.

    def trigger(self):
        if self.play_type == 'pass':
            self.handle_pass()
        elif self.play_type == 'rush':
            self.handle_rush()
        elif self.play_type == 'field_goal_attempt':
            self.handle_field_goal()
        elif self.play_type == 'kickoff':
            self.handle_kickoff()
        elif self.play_type == 'punt':
            self.handle_punt()
        elif self.play_type == 'safety':
            self.handle_safety()
        elif self.play_type == 'extra_point':
            self.handle_extra_point()
        elif self.play_type == 'two_point_conversion':
            self.handle_two_point_conversion()
        # Add other special play handlers
        self.game.update_game_state()

    def handle_pass(self):
        if self.details['completed']:
            self.game.field.move_ball(self.details['yards'])
            if self.details['out_of_bounds']:
                self.game.clock.handle_event('out_of_bounds')
            else:
                self.game.clock.handle_event('snap_after_incomplete')  # Clock resumes at snap
        else:
            self.game.clock.handle_event('incomplete_pass')  # Clock stops

    def handle_rush(self):
        self.game.field.move_ball(self.details['yards'])
        if self.details['out_of_bounds']:
            self.game.clock.handle_event('out_of_bounds')
        elif self.details['first_down']:
            self.game.clock.handle_event('first_down')

    def handle_field_goal(self):
        if self.details['successful']:
            self.game.scoreboard.update_score(self.game.possessing_team, 3)
            self.game.clock.handle_event('scoring_play')
        else:
            # Handling depends on where the ball is next played
            self.game.clock.handle_event('resume_play')

    def handle_kickoff(self):
        # Assume kickoff distance and return yards are calculated
        self.game.field.move_ball(self.details['kick_distance'] - self.details['return_yards'])
        self.game.clock.handle_event('kickoff_play')
        self.game.possession_change()  # Typically results in possession for the receiving team

    def handle_punt(self):
        # Assume punt distance and outcomes are calculated
        self.game.field.move_ball(self.details['yards'])
        self.game.clock.handle_event('play_ends')  # Stop clock until next snap
        self.game.possession_change()  # Typically results in a change of possession

    def handle_safety(self):
        self.game.scoreboard.update_score(self.game.defending_team, 2)
        self.game.clock.handle_event('scoring_play')
        self.game.possession_change()  # Ball to be kicked back to scoring team

    def handle_extra_point(self):
        if self.details['successful']:
            self.game.scoreboard.update_score(self.game.possessing_team, 1)

    def handle_two_point_conversion(self):
        if self.details['successful']:
            self.game.scoreboard.update_score(self.game.possessing_team, 2)
    
    def handle_kickoff(self):
        # Assume kickoff distance and return yards are calculated
        self.game.field.move_ball(self.details['kick_distance'] - self.details['return_yards'])
        self.game.clock.handle_event('kickoff_play')
        self.game.possession_change()  # Typically results in possession for the receiving team

    def handle_fumble(self):
        if self.details['recovered_by_own_team']:
            self.game.field.move_ball(self.details['yards_lost_or_gained'])
            self.game.clock.handle_event('play_continues')
        else:
            self.game.field.move_ball(self.details['yards_lost_or_gained'])
            self.game.possession_change()  # Change possession if recovered by the opposing team
            self.game.clock.handle_event('change_of_possession')

    def handle_interception(self):
        self.game.field.move_ball(self.details['return_yards'])  # Move the ball based on return yards
        self.game.possession_change()
        self.game.clock.handle_event('change_of_possession')

    def handle_blocked_kick(self):
        if self.details['recovered_by_kicking_team']:
            self.game.field.move_ball(self.details['yards_lost'])  # Loss of yards due to block recovery
            self.game.clock.handle_event('play_continues')
        else:
            self.game.field.move_ball(self.details['yards_returned'])
            self.game.possession_change()
            self.game.clock.handle_event('change_of_possession')
