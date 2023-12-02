import unittest
import days.day1

class TestDay01(unittest.TestCase):

    data1 = ["1abc2\n",
"pqr3stu8vwx\n",
"a1b2c3d4e5f\n",
"treb7uchet\n"]

    data2 = ["two1nine\n",
"eightwothree\n",
"abcone2threexyz\n",
"xtwone3four\n",
"4nineeightseven2\n",
"zoneight234\n",
"7pqrstsixteen\n"]
    
    data3 = ["fivezg8jmf6hrxnhgxxttwoneg\n",   #51
             "342\n",  #32
             "x8\n",   #88
             "3c2\n",  #32
             "g7\n",   #77
             "17\n",   #17
             "5c1\n",   #51
             ]

    def test_day01_part1(self):
        self.assertEqual(days.day1.part1(self.data1), 142)
    
    def test_day01_part2(self):
        self.assertEqual(days.day1.part2(self.data2), 281)
        self.assertEqual(days.day1.part2(self.data3), 348)
