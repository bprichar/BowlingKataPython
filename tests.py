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
