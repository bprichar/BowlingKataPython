import unittest
import Game

class testBolwingGame(unittest.TestCase):

    def setUp(self):
        self._g = Game.Game()

    def testGutterGame(self):
        self.rollMany(20, 0)
        assert self._g.score() == 0

    def testAllOnes(self):
        self.rollMany(20, 1)
        assert self._g.score() == 20

    def rollMany(self, n, pins):
        for i in xrange(n):
            self._g.roll(pins)

    def testRollSpare(self):
        self._g.roll(5)
        self._g.roll(5) # Spare
        self._g.roll(3)
        self.rollMany(17, 0)
        assert self._g.score() == 16

    def testRollStrike(self):
        self._g.roll(10) #Strike
        self._g.roll(3)
        self._g.roll(4)
        self.rollMany(17, 0)
        assert self._g.score() == 24

    def testPerfectGame(self):
        self.rollMany(12, 10)
        assert self._g.score() == 300
