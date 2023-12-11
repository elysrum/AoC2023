import unittest
import days.day11

class TestDay11(unittest.TestCase):

    data = ["...#......\n",
".......#..\n",
"#.........\n",
"..........\n",
"......#...\n",
".#........\n",
".........#\n",
"..........\n",
".......#..\n",
"#...#.....",
]

    def test_day11_part1(self):
        self.assertEqual(days.day11.part1(self.data), 374)

    def test_day11_part2(self):
        self.assertEqual(days.day11.part2(self.data), 82000210)

