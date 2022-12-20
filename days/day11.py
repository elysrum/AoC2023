from collections import namedtuple
from math import trunc

def build_monkey_list(data: list[str]) -> list:

    items = []
    Monkey = namedtuple('Monkey', ['id', 'items', 'divisor', 'true_monkey', 'false_monkey', 'operation'])
    monkey_list = []
    divis = 1
    tmnk = 0
    fmnk = 0
    mnk = 0
    op = ""

    for row in data :
        words = row.strip().split()

        if len(words) == 0 :
            monkey_list.append(Monkey(mnk, items, divis, tmnk, fmnk, op))
        elif words[0] == "Monkey" :
            mnk = words[1].strip(":,")
        elif words[0] == "Starting":
            items = []
            for i in range(2, len(words)):
                items.append(int(words[i].strip(":,")))
        elif words[0] == "Operation:" :
            op = "".join([words[3], words[4], words[5]])
        elif words[0] == "Test:" :
            divis = int(words[3])
        elif words[1] == "true:" : 
            tmnk = int(words[5])
        elif words[1] == "false:" : 
            fmnk = int(words[5])

    monkey_list.append(Monkey(mnk, items, divis, tmnk, fmnk, op))

    return monkey_list

def process_monkeys(monkey_list: list, monkey_counts: list, lcm: int, div_amount: int) -> list:
   
    monkey = 0
    op = ""
    wl = 0

    for m in monkey_list :
        for _ in range(0, len(m.items)) :
            i = m.items.pop(0)
            op = m.operation.replace("old", f"{i}")
            wl = eval(op)
            if div_amount == 1 :
                wl %= lcm
            else :
                wl = (wl // 3)

            if (wl % m.divisor) == 0 :
                monkey_list[m.true_monkey].items.append(wl)
            else :
                monkey_list[m.false_monkey].items.append(wl)

            monkey_counts[monkey] += 1

        monkey += 1

    return monkey_list

def part1(data: list[str]) -> int:

    monkey_counts = []
    lcm = 1

    monkey_list = build_monkey_list(data)
    for _ in range(0, len(monkey_list)) :
        monkey_counts.append(0)
     
    for _ in range (0,20) :
        monkey_list = process_monkeys(monkey_list, monkey_counts, lcm, 3)

    monkey_counts.sort(reverse=True)

    return monkey_counts[0] * monkey_counts[1]


def part2(data: list[str]) -> int:

    monkey_counts = []
    
    monkey_list = build_monkey_list(data)

#   lcm = lowest common modulo
#   mutliplying all divisors together should give us this
    lcm = 1
    for m in monkey_list:
        lcm *= m.divisor

    for _ in range(0, len(monkey_list)) :
        monkey_counts.append(0)
     
    for i in range (0,10000) :
        monkey_list = process_monkeys(monkey_list, monkey_counts, lcm, 1)

    monkey_counts.sort(reverse=True)

    return monkey_counts[0] * monkey_counts[1]
