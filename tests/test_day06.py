import unittest
import days.day6

class TestDay06(unittest.TestCase):

    data = ["Time:      7  15   30\n",
            "Distance:  9  40  200\n"]

    def test_day06_part1(self):
        self.assertEqual(days.day6.part1(self.data), 288)
    def test_day06_part2(self):
        self.assertEqual(days.day6.part2(self.data), 71503)
