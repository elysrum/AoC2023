import unittest
import days.day6

class TestDay06(unittest.TestCase):

    data = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb\n",
    "bvwbjplbgvbhsrlpgdmjqwftvncz\n",
    "nppdvjthqldpwncqszvftbrmjlhg\n",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg\n",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw\n"]

    def test_day06_part1(self):
        self.assertEqual(days.day6.part1(self.data[0]), 7)
        self.assertEqual(days.day6.part1(self.data[1]), 5)
        self.assertEqual(days.day6.part1(self.data[2]), 6)
        self.assertEqual(days.day6.part1(self.data[3]), 10)
        self.assertEqual(days.day6.part1(self.data[4]), 11)

    def test_day06_part2(self):
        self.assertEqual(days.day6.part2(self.data[0]), 19)
        self.assertEqual(days.day6.part2(self.data[1]), 23)
        self.assertEqual(days.day6.part2(self.data[2]), 23)
        self.assertEqual(days.day6.part2(self.data[3]), 29)
        self.assertEqual(days.day6.part2(self.data[4]), 26)
