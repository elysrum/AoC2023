import unittest
import days.day1

class TestDay01(unittest.TestCase):

    data = ["1000","2000","3000","\n","4000","\n","5000","6000","\n","7000","8000","9000","\n","10000\n", "\n"]

    def test_day01_part1(self):
        self.assertEqual(days.day1.part1(self.data), 24000)
    
    def test_day01_part2(self):
        self.assertEqual(days.day1.part2(self.data), 45000)
