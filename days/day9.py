from functools import reduce
import operator

# Are all elements in the list the same?
def all_same(lst):
    if len(lst) < 0:
        res = True
    res = all(ele == lst[0] for ele in lst)
    return res

def part1_recurse(num_list: list[int]) -> list[int]:
    new_list = []
    for i in range(1, len(num_list)):
        new_list.append(num_list[i] - num_list[i-1])

    if all_same(new_list) :
        pass
    else:
        part1_recurse(new_list)
    
    num_list.append(num_list[len(num_list) - 1] + int(new_list[len(new_list) - 1]))
    return num_list

def part1(data: list[str]) -> int:
    number_list = []

    retVal = 0

    for line in data :
        number_list = [int(x) for x in line.strip().split()]
        new_list = part1_recurse(number_list)
        retVal += new_list[len(new_list) - 1]

    return retVal

def part2_recurse(num_list: list[int]) -> list[int]:
    new_list = []
    for i in range(1, len(num_list)):
        new_list.append(num_list[i] - num_list[i-1])

    if all_same(new_list) :
        pass
    else:
        part2_recurse(new_list)
    
    num_list.insert(0, num_list[0] - new_list[0])
    return num_list


def part2(data: list[str]) -> int:

    number_list = []

    retVal = 0

    for line in data :
        number_list = [int(x) for x in line.strip().split()]
        new_list = part2_recurse(number_list)
        retVal += new_list[0]

    return retVal

