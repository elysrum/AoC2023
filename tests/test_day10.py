import unittest
import days.day10

class TestDay10(unittest.TestCase):

    data1 = [".....\n",
".S-7.\n",
".|.|.\n",
".L-J.\n",
"....."]


    data2 = ["..F7.\n",
            ".FJ|.\n",
            "SJ.L7\n",
            "|F--J\n",
            "LJ..."
]
    data3 = ["...........\n",
             ".S-------7.\n",
             ".|F-----7|.\n",
             ".||.....||.\n",
             ".||.....||.\n",
             ".|L-7.F-J|.\n",
             ".|..|.|..|.\n",
             ".L--J.L--J.\n",
             "...........\n"]

    data4 = ["..........\n",
             ".S------7.\n",
             ".|F----7|.\n",
             ".||....||.\n",
             ".||....||.\n",
             ".|L-7F-J|.\n",
             ".|..||..|.\n",
             ".L--JL--J.\n",
             "..........\n"]
    data5 = [".F----7F7F7F7F-7....\n",
".|F--7||||||||FJ....\n",
".||.FJ||||||||L7....\n",
"FJL7L7LJLJ||LJ.L-7..\n",
"L--J.L7...LJS7F-7L7.\n",
"....F-J..F7FJ|L7L7L7\n",
"....L7.F7||L7|.L7L7|\n",
".....|FJLJ|FJ|F7|.LJ\n",
"....FJL-7.||.||||...\n",
"....L---J.LJ.LJLJ...\n"]


    data6 = [
"FF7FSF7F7F7F7F7F---7\n",
"L|LJ||||||||||||F--J\n",
"FL-7LJLJ||||||LJL-77\n",
"F--JF--7||LJLJ7F7FJ-\n",
"L---JF-JLJ.||-FJLJJ7\n",
"|F|F-JF---7F7-L7L|7|\n",
"|FFJF7L7F-JF7|JL---7\n",
"7-L-JL7||F7|L7F-7F7|\n",
"L.L7LFJ|||||FJL7||LJ\n",
"L7JLJL-JLJLJL--JLJ.L\n"]

    def test_day10_part1(self):
        self.assertEqual(days.day10.part1(self.data1), 4)
        self.assertEqual(days.day10.part1(self.data2), 8)

    def test_day10_part2(self):
        self.assertEqual(days.day10.part2(self.data1), 1)
        self.assertEqual(days.day10.part2(self.data4), 4)
        self.assertEqual(days.day10.part2(self.data5), 8)
        self.assertEqual(days.day10.part2(self.data6), 10)
