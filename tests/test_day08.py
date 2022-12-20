import unittest
import days.day8

class TestDay08(unittest.TestCase):

    data = ["30373\n",
"25512\n",
"65332\n",
"33549\n",
"35390\n"
]

    def test_day08_part1(self):
        self.assertEqual(days.day8.part1(self.data), 21)

    def test_day08_part2(self):
        self.assertEqual(days.day8.part2(self.data), 8)

