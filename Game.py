class Game():

    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        score = 0
        frame_index = 0
        for frame in xrange(10):
            if self._isStrike(frame_index):
                score += 10 + self._strikeBonus(frame_index)
                frame_index += 1
            elif self._isSpare(frame_index):
                score += 10 + self._spareBonus(frame_index)
                frame_index += 2
            else:
                score += self._sumOfBallsInFrame(frame_index)
                frame_index += 2
        return score

    def _isStrike(self, frame_index):
        return self._rolls[frame_index] == 10

    def _isSpare(self, frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index+1] == 10

    def _strikeBonus(self, frame_index):
        return self._rolls[frame_index+1] + self._rolls[frame_index+2]

    def _spareBonus(self, frame_index):
        return self._rolls[frame_index+2]

    def _sumOfBallsInFrame(self, frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index+1]
