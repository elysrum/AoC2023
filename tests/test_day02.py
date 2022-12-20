import unittest
import days.day2

class TestDay02(unittest.TestCase):

    data = ["A Y", "B X", "C Z"]

    def test_day02_part1(self):
        self.assertEqual(days.day2.part1(self.data), 15)
    
    def test_day02_part2(self):
        self.assertEqual(days.day2.part2(self.data), 12)
