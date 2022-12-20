import unittest
import days.day5

class TestDay05(unittest.TestCase):

    data = [
    "    [D]    \n",
    "[N] [C]    \n",
    "[Z] [M] [P]\n",
    " 1   2   3 \n",
    "\n",
    "move 1 from 2 to 1\n",
    "move 3 from 1 to 3\n",
    "move 2 from 2 to 1\n",
    "move 1 from 1 to 2\n"]

    def test_day05_part1(self):
        self.assertEqual(days.day5.part1(self.data), "CMZ")

    def test_day05_part2(self):
        self.assertEqual(days.day5.part2(self.data), "MCD")
