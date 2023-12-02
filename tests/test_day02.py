import unittest
import days.day2

class TestDay02(unittest.TestCase):

    data1 = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

    data2 = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n",
"Game 91: 1 blue; 1 blue, 3 green; 1 green, 2 red\n",
"Game 100: 10 blue, 2 red; 7 green, 20 blue, 9 red; 8 red, 6 green, 2 blue"]
    

    def test_day02_part1(self):
        self.assertEqual(days.day2.part1(self.data1), 8)
        self.assertEqual(days.day2.part1(self.data2), 99)

    
    def test_day02_part2(self):
        self.assertEqual(days.day2.part2(self.data1), 2286)
