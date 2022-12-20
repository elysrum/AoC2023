import unittest
import days.day12

class TestDay12(unittest.TestCase):

    data = ["Sabqponm\n",
"abcryxxl\n",
"accszExk\n",
"acctuvwj\n",
"abdefghi\n",
]

    def test_day12_part1(self):
        self.assertEqual(days.day12.part1(self.data), 31)

    def test_day12_part2(self):
        self.assertEqual(days.day12.part2(self.data), 29)

