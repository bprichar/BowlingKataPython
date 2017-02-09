class Game():

    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        score = 0
        for roll in xrange(len(self._rolls)):
            score += self._rolls[roll]
            if self._rolls[roll] + self._rolls[roll-1] == 10: #Spare
                score += self._rolls[roll+1]
        return score
