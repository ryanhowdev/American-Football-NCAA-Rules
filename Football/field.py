class Field:
    def __init__(self):
        self.position = 50  # Start at midfield for example
        self.end_zones = {0: 'Home Endzone', 100: 'Visitor Endzone'}

    def move_ball(self, yards):
        self.position += yards
        self.position = max(0, min(100, self.position))  # Ensure the ball stays within the field bounds

    def check_position(self):
        if self.position in self.end_zones:
            return f"Ball in {self.end_zones[self.position]}"
        return "Ball in play"

