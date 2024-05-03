class Event:
    def __init__(self, game, name):
        self.game = game
        self.name = name

    def trigger(self):
        # This method will be overridden to provide specific event handling
        pass
