import unittest
from pybowling.game import Game

__author__ = '<a href="khalasi@gmail.com">Naresh Khalasi</a>'

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def tearDown(self):
        print(self.game)

    def _roll(self, total_rolls, pins_knocked):
        for _ in range(total_rolls):
            self.game.roll(pins_knocked)

    def test_gutter_game(self):
        self._roll(20, 0)
        self.assertEqual(0, self.game.score)

    def test_all_ones(self):
        self._roll(20, 1)
        self.assertEqual(20, self.game.score)

    def _roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)
    def test_one_spare(self):
        self._roll_spare()
        self.game.roll(3)
        self._roll(17, 0)
        self.assertEqual(16, self.game.score)

    def _roll_strike(self):
        self.game.roll(10)
    def test_one_strike(self):
        self._roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        self._roll(16, 0)
        self.assertEqual(24, self.game.score)

    def test_perfect_game(self):
        self._roll(12, 10)
        self.assertEqual(300, self.game.score)

    def test_a_game(self):
        self.game.roll(1)
        self.game.roll(4)

        self.game.roll(4)
        self.game.roll(5)

        self.game.roll(6)
        self.game.roll(4)

        self.game.roll(5)
        self.game.roll(5)

        self.game.roll(10)

        self.game.roll(0)
        self.game.roll(1)

        self.game.roll(7)
        self.game.roll(3)

        self.game.roll(6)
        self.game.roll(4)

        self.game.roll(10)

        self.game.roll(2)
        self.game.roll(8)

        self.game.roll(6)

        self.assertEqual(133, self.game.score)

