import unittest
import days.day13

class TestDay13(unittest.TestCase):

    data = ["[1,1,3,1,1]\n",
"[1,1,5,1,1]\n",
"\n",
"[[1],[2,3,4]]\n",
"[[1],4]\n",
"\n",
"[9]\n",
"[[8,7,6]]\n",
"\n",
"[[4,4],4,4]\n",
"[[4,4],4,4,4]\n",
"\n",
"[7,7,7,7]\n",
"[7,7,7]\n",
"\n",
"[]\n",
"[3]\n",
"\n",
"[[[]]]\n",
"[[]]\n",
"\n",
"[1,[2,[3,[4,[5,6,7]]]],8,9]\n",
"[1,[2,[3,[4,[5,6,0]]]],8,9]\n",
]

    def test_day13_part1(self):
        self.assertEqual(days.day13.part1(self.data), 13)

    def test_day13_part2(self):
        self.assertEqual(days.day13.part2(self.data), 140)

