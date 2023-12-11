from collections import Counter

def expand_universe(data: list[list], expanse: int) -> list[list]:

    new_universe = []
    # Expand the number of rows first - its the easier of the two
    for row in range(len(data)):
        line = data[row]
        # Is the whole line "."
        new_universe.append(line)
        if all(char == "." for char in line) :
            for _ in range(0, expanse - 1):
                new_universe.append(line[:]) # make sure we append a copy otherwise we reference same thing

    offset = 0
    for col in range(len(new_universe[0])):
        count = Counter()
        for row in range(len(new_universe)):
            count[new_universe[row][col + offset]] += 1
        if count["."] == len(new_universe) :
            # Entire Column is "."
            for nrow in range(len(new_universe)):
                for o in range (0, expanse - 1):
                    new_universe[nrow].insert(col + offset + o, ".")
            offset += expanse - 1

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
    new_universe = expand_universe(universe, 1)

    ROWS = len(new_universe)
    COLS = len(new_universe[0])

    galaxies = []

    for r in range(ROWS):
        for c in range(COLS):
            if new_universe[r][c] =="#":
                galaxies.append((r, c))

    num_galaxies =  len(galaxies)

    sumDist = 0

    for i in range(0, num_galaxies):
        (x, y) = galaxies[i]
        for j in range(i, num_galaxies):
            (dx, dy) = galaxies[j]
            sumDist += abs(x - dx) + abs(y - dy)
            

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
    new_universe = expand_universe(universe, 1000000)

    ROWS = len(new_universe)
    COLS = len(new_universe[0])

    galaxies = []

    for r in range(ROWS):
        for c in range(COLS):
            if new_universe[r][c] =="#":
                galaxies.append((r, c))

    num_galaxies =  len(galaxies)

    sumDist = 0

    for i in range(0, num_galaxies):
        (x, y) = galaxies[i]
        for j in range(i, num_galaxies):
            (dx, dy) = galaxies[j]
            sumDist += abs(x - dx) + abs(y - dy)
            

    return sumDist
