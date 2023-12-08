from collections import defaultdict

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

    starting_count = len(start_nodes)
    exitFound = False
    i = 0

    while not exitFound:
        lookup = (i % len(instructions))
        i += 1
        new_nodes = []
        for node in start_nodes:
            curr_pos = posn[node]

            if (instructions[lookup] == "R") :
                new_nodes.append(curr_pos[1])
            else:
                new_nodes.append(curr_pos[0])

        count = len(list((filter(lambda x: x[2] == "Z", new_nodes))))
        if count == starting_count:
             exitFound = True
        
        start_nodes = new_nodes

    return i

