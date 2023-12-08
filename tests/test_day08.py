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
    
    data2 = ["LR\n",
"\n",
"11A = (11B, XXX)\n",
"11B = (XXX, 11Z)\n",
"11Z = (11B, XXX)\n",
"22A = (22B, XXX)\n",
"22B = (22C, 22C)\n",
"22C = (22Z, 22Z)\n",
"22Z = (22B, 22B)\n",
"XXX = (XXX, XXX)\n"
    ]
    def test_day08_part1(self):
        self.assertEqual(days.day8.part1(self.data), 2)

    def test_day08_part2(self):
        self.assertEqual(days.day8.part2(self.data2), 6)

