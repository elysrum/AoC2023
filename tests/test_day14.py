import unittest
import days.day14

class TestDay14(unittest.TestCase):

    data = ["498,4 -> 498,6 -> 496,6\n",
"503,4 -> 502,4 -> 502,9 -> 494,9\n",
]

    def test_day14_part1(self):
        self.assertEqual(days.day14.part1(self.data), 24)

    def test_day14_part2(self):
        self.assertEqual(days.day14.part2(self.data), 93)

