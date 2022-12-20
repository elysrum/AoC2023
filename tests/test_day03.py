import unittest
import days.day3

class TestDay03(unittest.TestCase):

    data = ["vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw]"]

    def test_day03_part1(self):
        self.assertEqual(days.day3.part1(self.data), 157)
    
    def test_day03_part2(self):
        self.assertEqual(days.day3.part2(self.data), 70)
