
def part1(data: list[str]) -> int:

    pipes = [][]
    start_coord = (0,0)

    y = 0
    for line in data:
        x = 0
        for pipe in line.strip():
            pipes[x][y] = pipe
            y = y + 1

            if pipe == "S":
                start_coord = (x,y)

        x = x + 1

    print(start_coord)


    return 4


def part2(data: list[str]) -> int:


    return 10
