import unittest
import days.day22
class TestDay22(unittest.TestCase):

    data = ["        ...#\n",
"        .#..\n",
"        #...\n",
"        ....\n",
"...#.......#\n",
"........#...\n",
"..#....#....\n",
"..........#.\n",
"        ...#....\n",
"        .....#..\n",
"        .#......\n",
"        ......#.\n",
"\n",
"10R5L5R10L4R5L5\n",
]

    def test_day22_part1(self):
        self.assertEqual(days.day22.part1(self.data), 6032)

    def test_day22_part2(self):
        self.assertEqual(days.day22.part2(self.data), 5031)

