class Game():

    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        score = 0
        for roll in self._rolls:
            score += roll
        return score
