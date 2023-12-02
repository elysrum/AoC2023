import unittest
import days.day2

class TestDay02(unittest.TestCase):

    data = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

    def test_day02_part1(self):
        self.assertEqual(days.day2.part1(self.data), 15)
    
    def test_day02_part2(self):
        self.assertEqual(days.day2.part2(self.data), 12)
