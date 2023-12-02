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

    accum = 0
    for data_line in data:
        if data_line == "":
            pass
        else:
            value1 = 0
            value2 = 0
            res_list = re.findall(r"(?=([\d]|one|two|three|four|five|six|seven|eight|nine))", data_line)
            if res_list:
                value1 = calculate_value(res_list[0])
                value2 = calculate_value(res_list[-1]) 
                accum = accum + (value1 * 10) + value2               

    return accum

def calculate_value (input : str) -> int :

    result = 0
    if input.isnumeric() : 
        result = int(input)
    else:
        match input :
            case "one" : 
                    result = 1
            case "two" : 
                    result = 2
            case "three" : 
                    result = 3
            case "four" : 
                    result = 4
            case "five" : 
                    result = 5
            case "six" : 
                    result = 6
            case "seven" : 
                    result = 7
            case "eight" : 
                    result = 8
            case "nine" : 
                    result = 9
            case "zero" :
                    result = 0                        
    return result

