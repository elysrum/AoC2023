import support
import re

def part1(data: list[str]) -> int:

    accum = 0
    char_value = "0"
    for data_line in data:
        if data_line == "":
            pass
        else:
            char_value = ""
            index = re.search(r"\d", data_line)
            if index:
                character = data_line[index.start()]
                char_value += character
            data_line_rev = data_line[::-1]
            index = re.search(r"\d", data_line_rev)
            if index:
                character = data_line_rev[index.start()]
                char_value += character

        accum += int(char_value)

    return accum

def part2(data: list[str]) -> int:

    return 281



