import unittest
import days.day9

class TestDay09(unittest.TestCase):

    data = ["R 4\n",
"U 4\n",
"L 3\n",
"D 1\n",
"R 4\n",
"D 1\n",
"L 5\n",
"R 2\n",
]

    def test_day09_part1(self):
        self.assertEqual(days.day9.part1(self.data), 13)

    def test_day09_part2(self):

        self.data = ["R 5\n",
"U 8\n",
"L 8\n",
"D 3\n",
"R 17\n",
"D 10\n",
"L 25\n",
"U 20\n"
]

        self.assertEqual(days.day9.part2(self.data), 36)

