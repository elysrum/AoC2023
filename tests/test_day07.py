import unittest
import days.day7

class TestDay07(unittest.TestCase):

    data = ['$ cd /\n',
'$ ls\n',
'dir a\n',
'14848514 b.txt\n',
'8504156 c.dat\n',
'dir d\n',
'$ cd a\n',
'$ ls\n',
'dir e\n',
'29116 f\n',
'2557 g\n',
'62596 h.lst\n',
'$ cd e\n',
'$ ls\n',
'584 i\n',
'$ cd ..\n',
'$ cd ..\n',
'$ cd d\n',
'$ ls\n',
'4060174 j\n',
'8033020 d.log\n',
'5626152 d.ext\n',
'7214296 k\n',
]

    def test_day07_part1(self):
        self.assertEqual(days.day7.part1(self.data), 95437)

    def test_day07_part2(self):
        self.assertEqual(days.day7.part2(self.data), 24933642)

