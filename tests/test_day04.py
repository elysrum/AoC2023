import unittest
import days.day4

class TestDay04(unittest.TestCase):

    data = ["2-4,6-8",
"2-3,4-5",
"5-7,7-9",
"2-8,3-7",
"6-6,4-6",
"2-6,4-8"]

    def test_day04_part1(self):
        self.assertEqual(days.day4.part1(self.data), 2)
    
    def test_day04_part2(self):
        self.assertEqual(days.day4.part2(self.data), 4)
