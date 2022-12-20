def part1(data: list[str]) -> int:
    count = 0

    for line in data:
        ranges = line.strip().split(",")
        x = ranges[0].split("-")
        y = ranges[1].split("-")

        x0 = (int) (x[0])
        x1 = (int) (x[1])
        y0 = (int) (y[0])
        y1 = (int) (y[1])

        if  (((x0 <= y0) and (x1 >= y1)) or 
            ((x0 >= y0) and (x1 <= y1))):
                count += 1
        else:
            pass
    return count

def part2(data: list[str]) -> int:
    count = 0

    for line in data:
        ranges = line.strip().split(",")
        x = ranges[0].split("-")
        y = ranges[1].split("-")

        x0 = (int) (x[0])
        x1 = (int) (x[1])
        y0 = (int) (y[0])
        y1 = (int) (y[1])

        if ((x1 < y0) or (x0 > y1)):
            pass
        else:
            count += 1 
    return count
