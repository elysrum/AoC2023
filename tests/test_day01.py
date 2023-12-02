import unittest
import days.day1

class TestDay01(unittest.TestCase):

    data = ["1abc2\n",
"pqr3stu8vwx\n",
"a1b2c3d4e5f\n",
"treb7uchet\n"]

    def test_day01_part1(self):
        self.assertEqual(days.day1.part1(self.data), 142)
    
    def test_day01_part2(self):
        self.assertEqual(days.day1.part2(self.data), 45000)
