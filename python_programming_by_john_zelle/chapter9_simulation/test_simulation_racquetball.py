import unittest
from python_programming_by_john_zelle.chapter9_simulation.simulation_racquetball import *


class MyTestCase(unittest.TestCase):
    def test_game_over(self):
        self.assertEqual(game_over(15, 14), True)
        self.assertEqual(game_over(14, 14), False)
        self.assertEqual(game_over(16, 20), False)
        self.assertEqual(game_over(5, 15), True)

    def test_simulate_one_game(self):
        print('simulating one game:', simulate_one_game(.6, .65))
        self.assertEqual(15 in simulate_one_game(.3, .5), True)
        self.assertEqual(15 in simulate_one_game(.6, .3), True)
        self.assertEqual(15 in simulate_one_game(.2, .9), True)

if __name__ == '__main__':
    unittest.main()
