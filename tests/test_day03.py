import unittest
import days.day3

class TestDay03(unittest.TestCase):

    data = ["467..114..\n",
            "...*......\n",
            "..35..633.\n",
            "......#...\n",
            "617*......\n",
            ".....+.58.\n",
            "..592.....\n",
            "......755.\n",
            "...$.*....\n",
            ".664.598..\n"
]
    data1 = [
        "..10.10...\n",
        "....*.....\n",   # Check Consecutive Matches
        ".......100\n",   # No Match
        "...10*10..\n",  # Check Consecutive matches
        "..10......\n",  # No Match 
        "....*.....\n",  #  No Match
        ".....10...\n",
        "....*.....\n",  #  Check Double Match
        "100.......\n",
        "*........*\n",
        ".......100\n"
]

    data2 = [
        ".100.100..\n",
        "..100*100.\n",  # Check Consecutive matches
        "....*.....\n",  #  Check Double Match
        ".100.100..\n",   # Check Consecutive Matches
        "....*.....\n",  #  Check Double Match
        ".100.100..\n",
        "100.......\n",
        "@........@\n",
        ".......100\n"
]

    def test_day03_part1(self):
        self.assertEqual(days.day3.part1(self.data), 4361)
        self.assertEqual(days.day3.part1(self.data2), 900)
    
    def test_day03_part2(self):
        self.assertEqual(days.day3.part2(self.data1), 300)

        self.assertEqual(days.day3.part2(self.data), 467835)
