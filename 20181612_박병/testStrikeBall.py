import unittest

from strikeball import StrikeBall

class TestGame(unittest.TestCase):

    def setUp(self):
        self.g = StrikeBall()

    def tearDown(self):
        pass

    def testNewGame(self):
        self.g.newGame(3)
        self.assertEqual(self.g.digits, 3)
        self.assertEqual(self.g.trials, 0)
        self.g.newGame(5)
        self.assertEqual(self.g.digits, 5)
        self.assertEqual(self.g.trials, 0)

    def testGuess(self):
        self.g.newGame(3)
        # We use "638" as test fixture
        self.g.secret = [6, 3, 8]
        s, b = self.g.guess('621')
        self.assertEqual(s, 1)
        self.assertEqual(b, 0)
        s, b = self.g.guess('261')
        self.assertEqual(s, 0)
        self.assertEqual(b, 1)
        s, b = self.g.guess('676')
        self.assertEqual(s, 1)
        self.assertEqual(b, 0)
        s, b = self.g.guess('686')
        self.assertEqual(s, 1)
        self.assertEqual(b, 1)
        s, b = self.g.guess('666')
        self.assertEqual(s, 1)
        self.assertEqual(b, 0)
        s, b = self.g.guess('386')
        self.assertEqual(s, 0)
        self.assertEqual(b, 3)
        s, b = self.g.guess('638')
        self.assertEqual(s, 3)
        self.assertEqual(b, 0)

        t = self.g.getGuessCount()
        self.assertEqual(t, 7)


if __name__ == '__main__':
    unittest.main()

