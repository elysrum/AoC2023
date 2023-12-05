def part1(data: list[str]) -> int:
     
    #Extract the Seeds first
    line = data[0]
    seeds = line.split()
    seeds = seeds[1:]
    map_values = []
    locn = []


    for seed in seeds :

        value = next_value = int(seed)
        value_found = False
        
        for line in data[1:]:

            # If we hit new line, then start a new map
            if line[0] == '\n':
                # Whatever this looks like
                map_values.clear()
            elif line[0].isalpha() :
                #This is the map name
                if not value_found and next_value == -1 :
                    next_value = value
                value = next_value
                map_values.append(value)
                value_found = False
            elif line[0].isnumeric() :
                # This is the set of ranges
                line_values = [int(x) for x in (line.split())]

                if not value_found and value_in_range(value, line_values[0], line_values[1], line_values[2]) :
                    next_value = mapped_value(value, line_values[0], line_values[1], line_values[2])
                    map_values.append(next_value)
                    value_found = True
                else:
                    if not value_found :
                        next_value = -1
            else:
                return -1

        locn.append(map_values.pop())

    retVal = sorted(locn)[0]

    return retVal

def part2(data: list[str]) -> int:

     
    return 35

# Given a value and a range definitions
# determine if the value is in the range

def value_in_range(value :int, left :int, right :int, length :int) -> bool:
    retVal = False

    if (value < right) or (value > (right + length - 1)):
        retVal = False
    else:
        retVal = True

    return retVal

def mapped_value(value :int, left :int, right :int, length :int) -> int:

    retVal = value - right + left

    return retVal

