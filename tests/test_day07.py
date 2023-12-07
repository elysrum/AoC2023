import unittest
import days.day7

class TestDay07(unittest.TestCase):

    data = ["32T3K 765\n",
"T55J5 684\n",
"KK677 28\n",
"KTJJT 220\n",
"QQQJA 48\n"
]

    def test_day07_part1(self):
        self.assertEqual(days.day7.part1(self.data), 6440)

    def test_day07_part2(self):
        self.assertEqual(days.day7.part2(self.data), 6440)

