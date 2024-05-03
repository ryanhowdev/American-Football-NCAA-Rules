class Clock:
    def __init__(self, total_minutes=60):  # NCAA games are divided into four 15-minute quarters
        self.total_seconds = total_minutes * 60
        self.time_left = self.total_seconds
        self.running = False
        self.last_two_minutes_first_half = False
        self.last_five_minutes_second_half = False

    def update_status(self):
        """ Update status flags for special timing rules. """
        if self.time_left <= 120 and self.time_left > 15 * 60:
            self.last_two_minutes_first_half = True
        else:
            self.last_two_minutes_first_half = False

        if self.time_left <= 300 and self.time_left > 0:
            self.last_five_minutes_second_half = True
        else:
            self.last_five_minutes_second_half = False

    def handle_event(self, event_type):
        """ Handle different events that affect the clock. """
        if event_type in ['incomplete_pass', 'end_of_quarter', 'scoring_play']:
            self.stop()

        if event_type == 'out_of_bounds':
            if (self.last_two_minutes_first_half or self.last_five_minutes_second_half):
                self.stop()
            else:
                self.start()

        if event_type == 'first_down':
            self.stop()
            if not (self.last_two_minutes_first_half or self.last_five_minutes_second_half):
                self.start()

        self.update_status()

    def start(self):
        """ Start the clock if not already running. """
        if not self.running:
            self.running = True

    def stop(self):
        """ Stop the clock if it is running. """
        if self.running:
            self.running = False

    def update(self, seconds_passed):
        """ Update the clock time, decreasing the remaining time by the seconds passed. """
        if self.running:
            self.time_left -= seconds_passed
            self.time_left = max(0, self.time_left)
