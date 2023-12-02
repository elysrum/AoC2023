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
    char_value = "0"
    for data_line in data:
        if data_line == "":
            pass
        else:
            char_value = ""
            res_list = re.findall(r"[\d]|[one]+|[two]+|[three]+|[four]+|[five]+|[six]+|[seven]+|[eight]+|[nine]+", data_line)
            if res_list:
                character = res_list[0].index.group()
                if character.isnumeric() : 
                    char_value += character
                else:
                    match character :
                        case "one" : 
                                character = "1"
                        case "two" : 
                                character = "2"
                        case "three" : 
                                character = "3"
                        case "four" : 
                                character = "4"
                        case "five" : 
                                character = "5"
                        case "six" : 
                                character = "6"
                        case "seven" : 
                                character = "7"
                        case "eight" : 
                                character = "8"
                        case "nine" : 
                                character = "9"
                                
                    char_value += character
                
        accum += int(char_value)

    return accum



