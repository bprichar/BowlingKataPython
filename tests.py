import unittest
import Game

class testBolwingGame(unittest.TestCase):

    def testGutterGame(self):
        g = Game.Game()
        for i in xrange(20):
            g.roll(0)
        assert g.score() == 0

    def testAllOnes(self):
        g = Game.Game()
        for i in xrange(20):
            g.roll(1)
        assert g.score() == 20
