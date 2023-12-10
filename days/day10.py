from collections import defaultdict


# Direction is one of:
#   0       1        2       3
# East    West     South   North
def calc_start_direction(grid : list[list], start_pos ) -> int:

    (y, x) = start_pos
    direction = 0

    if  (grid[y][x + 1] == "-" or grid[y][x + 1] == "7" or grid[y][x + 1] == "J") : 
        direction = 0
    elif  (grid[y][x - 1] == "-" or grid[y][x - 1] == "L" or grid[y][x - 1] == "F") : 
        direction = 1
    elif  (grid[y + 1][x] == "|" or grid[y + 1][x] == "L" or grid[y + 1][x] == "J") : 
        direction = 2
    elif  (grid[y - 1][x] == "|" or grid[y - 1][x] == "F" or grid[y - 1][x] == "7") : 
        direction = 3

    return direction

def part1(data: list[str]) -> int:

    start_coord = (0,0)

    # Initialise the array with "."
    pipes = [["." for i in range(len(data[0]))] for i in range(len(data))]

    # Build the map in memory
    y = 0
    for line in data:
        x = 0
        for pipe in line.strip():
            pipes[y][x] = pipe

            # This is the position we start in
            if pipe == "S":
                start_coord = (y,x)

            x = x + 1
        y = y + 1

    # So, from the start, follow the pipes until we get back to the start.
    # We dont care what pipe the start is, only whether the next pipe brings
    # us back to the start
    #            
    cardinals = [(0,1), (0,-1), (1,0), (-1,0)]

    found = False
    ny, nx = start_coord
    retVal = steps = 0

    delta = calc_start_direction(pipes, start_coord)
    steps = 0

    while not found:

        # Work out which direction to go 
        # Only four cardinal directions should be considered
        #   0       1        2       3
        # East    West     South   North
        # [0][1], [0][-1]. [1][0], [-1][0]

        (dy, dx) = cardinals[delta]

        y = ny + dy
        x = nx + dx

        # If East, then easterly pipe must be one of -, J, 7
        if      dx == 1 and \
                (pipes[y][x] == "-" or \
                pipes[y][x] == "J" or \
                pipes[y][x] == "7" ):
            if (pipes[y][x] == "-") : 
                    #delta unchanged
                    pass
            elif pipes[y][x] == "J" : 
                    #  Now Heading North
                    delta = 3
            elif pipes[y][x] == "7" :
                    # Now Heading South
                    delta = 2
            nx = x
        # If West, then Westerly pipe must be one of -. L, F
        elif    dx == -1 and \
                (pipes[y][x] == "-" or \
                pipes[y][x] == "L" or \
                pipes[y][x] == "F") :
            if (pipes[y][x] == "-") : 
                    #delta unchanged
                    pass
            elif pipes[y][x] == "L" : 
                    #  Now Heading North
                    delta = 3
            elif pipes[y][x] == "F" :
                    # Now Heading South
                    delta = 2
            nx = x
        # If North, then Northerly pipe must be one of |, F, 7
        elif    dy == -1 and \
                (pipes[y][x] == "|" or \
                pipes[y][x] == "F" or \
                pipes[y][x] == "7") :
            if (pipes[y][x] == "|") : 
                    #delta unchanged
                    pass
            elif pipes[y][x] == "F" : 
                    #  Now Heading East
                    delta = 0
            elif pipes[y][x] == "7" :
                    # Now Heading West
                    delta = 1
            ny = y
        # If South, then Southerly pipe must be one of |. L, J
        elif    dy == 1 and \
                (pipes[y][x] == "|" or \
                pipes[y][x] == "L" or \
                pipes[y][x] == "J") :
            if (pipes[y][x] == "|") : 
                    #delta unchanged
                    pass
            elif pipes[y][x] == "L" : 
                    #  Now Heading East
                    delta = 0
            elif pipes[y][x] == "J" :
                    # Now Heading West
                    delta = 1
            ny = y
        elif    pipes[y][x] == "S":
            # We are back at the beginning - hooray
            found = True
            ny = y
            nx = x

        steps = steps + 1

    if steps > retVal:
        retVal = steps

    return retVal//2


# Point in Polygon Algorithm
# Count how many points are inside the polygon
# If crossings is Even Point is OUTSIDE, else INSIDE
def PIP_line(input: list[str]) -> int:
      
    score = 0
    crossings = 0

    for c in input:
        match  c:
                case "." :
                    # Not part of loop, so is it inside or outside?
                    if crossings % 2 != 0:
                            score = score + 1
                case "S" :
                    pass
                    # crossings += 1
                case "|" :
                    crossings += 1
                case "7" :
                    crossings += 1
                case "F" :
                    crossings += 1
                #The rest are part of the horizontal pieces, so not technically a wall crossing
                # L and J because we are counting down the grid, not up the grid (7 & F)
                case "L" :
                    pass
                    #crossings += 1
                case "J" :
                    pass
                    #crossings += 1
                case "-" :
                    pass
    return score

def part2(data: list[str]) -> int:

    start_coord = (0, 0)
    # Initialise the array with "."
    ROWS = len(data)
    COLS = (len(data[0].strip()))
    pipes = [["." for i in range(COLS)] for i in range(ROWS)]

    # Build the map in memory
    count = y = 0
    for line in data:
        x = 0
        for pipe in line.strip():
            pipes[y][x] = pipe

            # This is the position we start in
            if pipe == "S":
                start_coord = (y,x)

            x = x + 1
        y = y + 1

    ######## TODO 
    ### Need to work out what pipe tile S actuall is 
    ### and replace it in the loop with correct tile
    ### then chenge test below to check for start_coord not S

    # Need to walk the loop, to capture every tile in the loop
    # So, from the start, follow the pipes until we get back to the start.
    # We dont care what pipe the start is, only whether the next pipe brings
    # us back to the start
    #            
    cardinals = [(0,1), (0,-1), (1,0), (-1,0)]

    found = False
    ny, nx = start_coord

    LOOP = []

    delta = calc_start_direction(pipes, start_coord)

    while not found:

        # Work out which direction to go 
        # Only four cardinal directions should be considered
        #   0       1        2       3
        # East    West     South   North
        # [0][1], [0][-1]. [1][0], [-1][0]

        (dy, dx) = cardinals[delta]

        y = ny + dy
        x = nx + dx

        # If East, then easterly pipe must be one of -, J, 7
        if      dx == 1 and \
                (pipes[y][x] == "-" or \
                pipes[y][x] == "J" or \
                pipes[y][x] == "7" ):
            if (pipes[y][x] == "-") : 
                    #delta unchanged
                    pass
            elif pipes[y][x] == "J" : 
                    #  Now Heading North
                    delta = 3
            elif pipes[y][x] == "7" :
                    # Now Heading South
                    delta = 2
            nx = x
        # If West, then Westerly pipe must be one of -. L, F
        elif    dx == -1 and \
                (pipes[y][x] == "-" or \
                pipes[y][x] == "L" or \
                pipes[y][x] == "F") :
            if (pipes[y][x] == "-") : 
                    #delta unchanged
                    pass
            elif pipes[y][x] == "L" : 
                    #  Now Heading North
                    delta = 3
            elif pipes[y][x] == "F" :
                    # Now Heading South
                    delta = 2
            nx = x
        # If North, then Northerly pipe must be one of |, F, 7
        elif    dy == -1 and \
                (pipes[y][x] == "|" or \
                pipes[y][x] == "F" or \
                pipes[y][x] == "7") :
            if (pipes[y][x] == "|") : 
                    #delta unchanged
                    pass
            elif pipes[y][x] == "F" : 
                    #  Now Heading East
                    delta = 0
            elif pipes[y][x] == "7" :
                    # Now Heading West
                    delta = 1
            ny = y
        # If South, then Southerly pipe must be one of |. L, J
        elif    dy == 1 and \
                (pipes[y][x] == "|" or \
                pipes[y][x] == "L" or \
                pipes[y][x] == "J") :
            if (pipes[y][x] == "|") : 
                    #delta unchanged
                    pass
            elif pipes[y][x] == "L" : 
                    #  Now Heading East
                    delta = 0
            elif pipes[y][x] == "J" :
                    # Now Heading West
                    delta = 1
            ny = y
        elif    pipes[y][x] == "S":
            # We are back at the beginning - hooray
            found = True
            ny = y
            nx = x

        #Store Coordinate of loop tile
        LOOP.append((ny, nx))

    # Build a new Grid with only loop tiles present
    new_grid = [["." for i in range(COLS)] for i in range(ROWS)]

    # Populate the loop
    for (ty, tx) in LOOP:
        new_grid[ty][tx] = pipes[ty][tx]

    # for y in range(ROWS):
    #       print("".join(new_grid[y]))
    count = 0
    for row in new_grid:
        print("".join(row))
        count += PIP_line(row)
        print(count)

    return count