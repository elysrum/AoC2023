from collections import Counter

EmptyRows = []
EmptyColumns = []

def expand_universe(data: list[list]) -> list[list]:

    new_universe = []

    # Clean out empty rows and columns - important if this is part2 running after part1
    EmptyRows.clear()
    EmptyColumns.clear()

    # Expand the number of rows first - its the easier of the two
    for row in range(len(data)):
        line = data[row]
        # Is the whole line "."
        new_universe.append(line)
        if all(char == "." for char in line) :
            EmptyRows.append(row)



    offset = 0
    for col in range(len(new_universe[0])):
        count = Counter()
        for row in range(len(new_universe)):
            count[new_universe[row][col + offset]] += 1

        if (count["."] + count["o"]) == len(new_universe) :
            # Entire Column is "."
            EmptyColumns.append(col)


    return new_universe

def part1(data: list[str]) -> int:

    # INgest the universe
    universe = [["." for i in range(len(data[0]) - 1)] for i in range(len(data))]
    # Build the map in memory
    y = 0
    for line in data:
        x = 0
        for tile in line.strip():
            universe[y][x] = tile
            x = x + 1
        y = y + 1

    # First Expand the Universe
    new_universe = expand_universe(universe)

    ROWS = len(new_universe)
    COLS = len(new_universe[0])

    galaxies = []

    for r in range(ROWS):
        for c in range(COLS):
            if new_universe[r][c] =="#":
                galaxies.append((r, c))

    num_galaxies =  len(galaxies)

    sumDist = 0

    empty_cost = 1

    for i in range(num_galaxies):
        y, x = galaxies[i]
        for j in range(i + 1, num_galaxies):
            dy, dx = galaxies[j]
            
            steps = abs(x - dx) + abs(y - dy)

            for empty_row in EmptyRows:
                if min(y, dy) <= empty_row <= max(y, dy):
                    steps += empty_cost
            for empty_col in EmptyColumns:
                if min(x, dx) <= empty_col <= max(x, dx):
                    steps += empty_cost
            # Algo here
            sumDist += steps

            
    return sumDist

def part2(data: list[str]) -> int:

    # INgest the universe
    universe = [["." for i in range(len(data[0]) - 1)] for i in range(len(data))]
    # Build the map in memory
    y = 0
    for line in data:
        x = 0
        for tile in line.strip():
            universe[y][x] = tile
            x = x + 1
        y = y + 1

    # First Expand the Universe
    new_universe = expand_universe(universe)

    ROWS = len(new_universe)
    COLS = len(new_universe[0])

    galaxies = []

    for r in range(ROWS):
        for c in range(COLS):
            if new_universe[r][c] =="#":
                galaxies.append((r, c))

    num_galaxies =  len(galaxies)

    sumDist = 0

    empty_cost = 10**6 - 1

    for i in range(num_galaxies):
        y, x = galaxies[i]
        for j in range(i + 1, num_galaxies):
            dy, dx = galaxies[j]
            
            steps = abs(x - dx) + abs(y - dy)

            for empty_row in EmptyRows:
                if min(y, dy) <= empty_row <= max(y, dy):
                    steps += empty_cost
            for empty_col in EmptyColumns:
                if min(x, dx) <= empty_col <= max(x, dx):
                    steps += empty_cost
            # Algo here
            sumDist += steps

    return sumDist
