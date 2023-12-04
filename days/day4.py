import re

def part1(data: list[str]) -> int:
    total = 0

    for line in data:
        card = line.strip().split("|")
        left_side = card[0]
        right_side = card[1]
        winning_numbers = sorted([int(x) for x in (re.findall(r"\d+", left_side[9:]))])
        played_numbers = sorted([int(x) for x in (re.findall(r"\d+", right_side))])

        matched_number_count = 0

        for winning_number in winning_numbers :
            for played_number in played_numbers :
                if winning_number == played_number : 
                    matched_number_count += 1

        if matched_number_count == 1 : 
            total += 1
        elif matched_number_count > 1 :
            total += 2 ** (matched_number_count-1)
        else:
            pass

    return total

def part2(data: list[str]) -> int:

    return 4
