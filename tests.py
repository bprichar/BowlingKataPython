import unittest
import Game

class testBolwingGame(unittest.TestCase):

    def setUp(self):
        self._g = Game.Game()

    def testGutterGame(self):
        for i in xrange(20):
            self._g.roll(0)
        assert self._g.score() == 0

    def testAllOnes(self):
        for i in xrange(20):
            self._g.roll(1)
        assert self._g.score() == 20
