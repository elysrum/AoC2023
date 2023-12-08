from collections import defaultdict
from math import gcd

# lowest common multiplier
def lcm(values):
    retVal = 1
    for value in values:
        retVal = (value*retVal)//gcd(value, retVal)
    
    return retVal

def part1(data: list[str]) -> int:

    data_set = ("".join(data))
    posn = {}
        

    instructions, location_set = data_set.strip().split("\n\n")
    locations = location_set.strip().split("\n")

    for locn in locations:
        pos = locn[:3]
        n1 = locn[7:10]
        n2 = locn[12:15]
        posn[pos] = (n1, n2)

    exitFound = False
    i = 0

    next_dest = "AAA"

    while not exitFound:
        lookup = (i % len(instructions))
        i += 1
        curr_pos = posn[next_dest]

        if (instructions[lookup] == "R") :
            next_dest = curr_pos[1]
        else:
            next_dest = curr_pos[0]

        if next_dest == "ZZZ" :
            exitFound = True

    return i

def part2(data: list[str]) -> int:

    data_set = ("".join(data))
    posn = {}
    start_nodes = []
        

    instructions, location_set = data_set.strip().split("\n\n")
    locations = location_set.strip().split("\n")

    for locn in locations:
        pos = locn[:3]
        n1 = locn[7:10]
        n2 = locn[12:15]
        posn[pos] = (n1, n2)
        if pos[2] == "A" :
            start_nodes.append(pos)

    exitFound = False
    i = 0
    end_state = {}

    while not exitFound:
        lookup = (i % len(instructions))
        i += 1
        new_nodes = []
        for node in start_nodes:
            curr_pos = posn[node]

            if (instructions[lookup] == "R") :
                new_pos = curr_pos[1]
            else:
                new_pos = curr_pos[0]

            new_nodes.append(new_pos)

            # We've found and end state, record it and how many iterations it took to get here
            if new_pos[2] == "Z" :
                end_state[new_pos] = i

            # If we have found an end state for all starting nodes, then we are done,
            if len(end_state) == len(start_nodes):
                exitFound = True
        
        start_nodes = new_nodes
    #Multiply all the iteratiosn for the end states together using lowest common multiplier func
    return lcm(end_state.values())

