import support.support
import days.day1
import days.day2
import days.day3
import days.day4
import days.day5
import days.day6
import days.day7
import days.day8
import days.day9
import days.day10
import days.day11
import days.day12
import days.day13
import days.day14
import days.day15
import days.day16


def main() -> int:
    #  Run Days
    data = support.support.read_day_data(1)
    print (f"Day 1 - Part 1: {days.day1.part1(data)} - Part 2: {days.day1.part2(data)}")
    data = support.support.read_day_data(2)
    print (f"Day 2 - Part 1: {days.day2.part1(data)} - Part 2: {days.day2.part2(data)}")
    data = support.support.read_day_data(3)
    print (f"Day 3 - Part 1: {days.day3.part1(data)} - Part 2: {days.day3.part2(data)}")
    data = support.support.read_day_data(4)
    print (f"Day 4 - Part 1: {days.day4.part1(data)} - Part 2: {days.day4.part2(data)}")
    data = support.support.read_day_data(5)
    print (f"Day 5 - Part 1: {days.day5.part1(data)} - Part 2: {days.day5.part2(data)}")
    data = support.support.read_day_data(6)
    print (f"Day 6 - Part 1: {days.day6.part1(data[0])} - Part 2: {days.day6.part2(data[0])}")
    data = support.support.read_day_data(7)
    print (f"Day 7 - Part 1: {days.day7.part1(data)} - Part 2: {days.day7.part2(data)}")
    data = support.support.read_day_data(8)
    print (f"Day 8 - Part 1: {days.day8.part1(data)} - Part 2: {days.day8.part2(data)}")
    data = support.support.read_day_data(9)
    print (f"Day 9 - Part 1: {days.day9.part1(data)} - Part 2: {days.day9.part2(data)}")
    # data = support.support.read_day_data(10)
    # res = days.day10.part2(data)
    # print (f"Day 10 - Part 1: {days.day10.part1(data)} - Part 2: \n{res[0:39]}\n{res[40:79]}\n{res[80:119]}\n{res[120:159]}\n{res[160:199]}\n{res[200:]}\n")
    # data = support.support.read_day_data(11)
    # print (f"Day 11 - Part 1: {days.day11.part1(data)} - Part 2: {days.day11.part2(data)}")
    # data = support.support.read_day_data(12)
    # print (f"Day 12 - Part 1: {days.day12.part1(data)} - Part 2: {days.day12.part2(data)}")
    # data = support.support.read_day_data(13)
    # print (f"Day 13 - Part 1: {days.day13.part1(data)} - Part 2: {days.day13.part2(data)}")
    # data = support.support.read_day_data(14)
    # print (f"Day 14 - Part 1: {days.day14.part1(data)} - Part 2: {days.day14.part2(data)}")
    # data = support.support.read_day_data(15)
    # print (f"Day 15 - Part 1: {days.day15.part1(data, 2000000)} - Part 2: {days.day15.part2(data, 4000000)}")
    data = support.support.read_day_data(16)
    print (f"Day 16 - Part 1: {days.day16.part1(data)} - Part 2: {days.day16.part2(data)}")
    return 0


if __name__ == "__main__":
     exit(main())
