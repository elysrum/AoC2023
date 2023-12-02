import support

def part1(data: list[str]) -> int:

    accum = 0
    for data_line in data:
        if data_line == "":
            pass
        else:
            char_value = ""
            for index, character in enumerate(data_line):
                if character.isdigit():
                    char_value += character
                    break
            for index, character in enumerate(reversed(data_line)):
                if character.isdigit():
                    char_value += character
                    break

        accum += int(char_value)

    return accum

def part2(data: list[str]) -> int:

    return True



