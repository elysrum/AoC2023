import unittest
import days.day8

class TestDay08(unittest.TestCase):

    data = ["RL\n",
"\n",
"AAA = (BBB, CCC)\n",
"BBB = (DDD, EEE)\n",
"CCC = (ZZZ, GGG)\n",
"DDD = (DDD, DDD)\n",
"EEE = (EEE, EEE)\n",
"GGG = (GGG, GGG)\n",
"ZZZ = (ZZZ, ZZZ)\n"
]

    def test_day08_part1(self):
        self.assertEqual(days.day8.part1(self.data), 2)

    def test_day08_part2(self):
        self.assertEqual(days.day8.part2(self.data), 8)

