
def part1(data: list[str]) -> int:

    x = 1
    cycle = 1
    cycle_interval = 20
    cycle_ceiling = 240
    total = 0

    for command_line in data :
        commands = command_line.strip().split()
        for op in commands :
            if op == "noop" :
                pass
            elif op == "addx" : 
                pass
            else :
                x = x + int(op)
            cycle += 1
            if cycle == cycle_interval and cycle <= cycle_ceiling:
                total += (x *  cycle)
                cycle_interval += 40


    return total


def part2(data: list[str]) -> str:

    x = 1
    cycle = 1
    screen_width = 40
    cycle_ceiling = 240
    screen_row = 0
    total = 0
    screen = [["." for _ in range(40)] for _ in range(6)]


    xpos = cycle

    for command_line in data :
        commands = command_line.strip().split()
        for op in commands :

            # Is sprite visible
            if x == xpos or x+1 == xpos or (x+2) == xpos :
                screen[screen_row][xpos-1] = "#"

            if op == "noop" :
                pass
            elif op == "addx" : 
                pass
            else :
                x += int(op)
                pass

            cycle += 1
            screen_row, xpos = divmod(cycle, screen_width)
            if (xpos == 0 ) : 
                screen_row -= 1
                xpos = 40


    ret_val = str("".join(screen[0][:])) + str("".join(screen[1][:])) + str("".join(screen[2][:])) + str("".join(screen[3][:])) + str("".join(screen[4][:])) + str("".join(screen[5][:]))

    return ret_val
