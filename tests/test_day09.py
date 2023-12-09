import unittest
import days.day9

class TestDay09(unittest.TestCase):

    data = ["0 3 6 9 12 15\n",
"1 3 6 10 15 21\n",
"10 13 16 21 30 45\n"
]

    def test_day09_part1(self):
        self.assertEqual(days.day9.part1(self.data), 114)

    def test_day09_part2(self):
        self.assertEqual(days.day9.part2(self.data), 2)

