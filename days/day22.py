import re

def move_cube_position(grid: list, x: int, y: int, direction: int, steps: int) -> tuple :

    xx = x
    yy = y
    new_direction = direction

    max_y = len(grid)
    max_x = len(grid[yy])

    for _ in range(steps) :

        # Face 1
        if 0 <= xx <= 49 and 150 <= yy <= 199 : 
            # Move Right (can take us to Face 3)
            if new_direction == 0 :
                cnd = new_direction
                cxx = xx + 1
                cyy = yy
                if ( cxx > 49) :
                    # Move to Face 3
                    cxx = yy - 100
                    cyy = 149
                    cnd = 3
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move down (can take use to Face 6)
            elif new_direction == 1 :
                cnd = new_direction
                cxx = xx
                cyy = yy + 1
                if ( cyy > 199) :
                    # Move to Face 6
                    cxx = xx + 100
                    cyy = 0
                    cnd = 1
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move Left (can take us to Face 5)
            elif new_direction == 2 :
                cnd = new_direction
                cxx = xx - 1
                cyy = yy
                if ( cxx < 0) :
                    # Move to Face 5
                    cxx = yy - 100
                    cyy = 0
                    cnd = 1
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move Up (can take us to Face 2)
            elif new_direction == 3 :
                cnd = new_direction
                cxx = xx
                cyy = yy - 1
                if ( cyy < 150 ) :
                    # Move to Face 2
                    cyy = 149
                    cxx = xx
                    cnd = 3
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            else :
                assert False
        # Face 2
        elif 0 <= xx <= 49 and 100 <= yy <= 149 :
            # Move Right (can take us to Face 3)
            if new_direction == 0 :
                cnd = new_direction
                cxx = xx + 1
                cyy = yy
                if ( cxx > 49) :
                    # Move to Face 3
                    cxx = 50
                    cyy = yy
                    cnd = 0
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move down (can take use to Face 1)
            elif new_direction == 1 :
                cnd = new_direction
                cxx = xx
                cyy = yy + 1
                if ( cyy > 149) :
                    # Move to Face 1
                    cxx = xx 
                    cyy = 150
                    cnd = 1
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move Left (can take us to Face 5)
            elif new_direction == 2 :
                cnd = new_direction
                cxx = xx - 1
                cyy = yy
                if ( cxx < 0) :
                    # Move to Face 5
                    cxx = 50
                    cyy = 149 - yy
                    cnd = 0
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move Up (can take us to Face 4)
            elif new_direction == 3 :
                cnd = new_direction
                cxx = xx
                cyy = yy - 1
                if ( cyy < 100 ) :
                    # Move to Face 4
                    cyy = cxx + 50
                    cxx = 50
                    cnd = 0
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            else :
                assert False
        # Face 3
        elif 50 <= xx <= 99 and 100 <= yy <= 149 :
            # Move Right (can take us to Face 6)
            if new_direction == 0 :
                cnd = new_direction
                cxx = xx + 1
                cyy = yy
                if ( cxx > 99) :
                    # Move to Face 6
                    cxx = 149
                    cyy = 149 - yy
                    cnd = 2
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move down (can take use to Face 1)
            elif new_direction == 1 :
                cnd = new_direction
                cxx = xx
                cyy = yy + 1
                if ( cyy > 149) :
                    # Move to Face 1
                    cxx = 49 
                    cyy = xx + 100
                    cnd = 2
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move Left (can take us to Face 2)
            elif new_direction == 2 :
                cnd = new_direction
                cxx = xx - 1
                cyy = yy
                if ( cxx < 50) :
                    # Move to Face 2
                    cxx = 49
                    cyy = yy
                    cnd = 2
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move Up (can take us to Face 4)
            elif new_direction == 3 :
                cnd = new_direction
                cxx = xx
                cyy = yy - 1
                if ( cyy < 100 ) :
                    # Move to Face 4
                    cyy = 99
                    cxx = xx
                    cnd = 3
                if grid[cyy][xx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            else :
                assert False
        # Face 4
        elif 50 <= xx <= 99 and 50 <= yy <= 99 :
            # Move Right (can take us to Face 6)
            if new_direction == 0 :
                cnd = new_direction
                cxx = xx + 1
                cyy = yy
                if ( cxx > 99) :
                    # Move to Face 6
                    cxx = yy + 50
                    cyy = 49
                    cnd = 3
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move down (can take use to Face 3)
            elif new_direction == 1 :
                cnd = new_direction
                cxx = xx
                cyy = yy + 1
                if ( cyy > 99) :
                    # Move to Face 3
                    cnd = 1
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move Left (can take us to Face 2)
            elif new_direction == 2 :
                cnd = new_direction
                cxx = xx - 1
                cyy = yy
                if ( cxx < 50) :
                    # Move to Face 2
                    cxx = yy - 50
                    cyy = 100
                    cnd = 1
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move Up (can take us to Face 5)
            elif new_direction == 3 :
                cnd = new_direction
                cxx = xx
                cyy = yy - 1
                if ( cyy < 50 ) :
                    # Move to Face 5
                    cyy = 49
                    cxx = xx
                    cnd = 3
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            else :
                assert False
        # Face 5
        elif 50 <= xx <= 99 and 0 <= yy <= 49 :
            # Move Right (can take us to Face 6)
            if new_direction == 0 :
                cnd = new_direction
                cxx = xx + 1
                cyy = yy
                if ( cxx > 99) :
                    # Move to Face 6
                    cnd = 0
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move down (can take use to Face 4)
            elif new_direction == 1 :
                cnd = new_direction
                cxx = xx
                cyy = yy + 1
                if ( cyy > 49) :
                    # Move to Face 4
                    cnd = 1
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move Left (can take us to Face 2)
            elif new_direction == 2 :
                cnd = new_direction
                cxx = xx - 1
                cyy = yy
                if ( cxx < 50) :
                    # Move to Face 2
                    cxx = 0
                    cyy = 149 - yy
                    cnd = 0
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd

                else :
                    # Should not get here
                    assert False
            # Move Up (can take us to Face 1)
            elif new_direction == 3 :
                cnd = new_direction
                cxx = xx
                cyy = yy - 1
                if ( cyy < 0) :
                    # Move to Face 1
                    cyy = 100 + xx
                    cxx = 0
                    cnd = 0
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            else :
                assert False
        # Face 6
        elif 100 <= xx <= 149 and 0 <= yy <= 49 :
            # Move Right (can take us to Face 3)
            if new_direction == 0 :
                cnd = new_direction
                cxx = xx + 1
                cyy = yy
                if ( cxx > 149) :
                    # Move to Face 3
                    cxx = 99
                    cyy = 149 - yy
                    cnd = 2
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move down (can take use to Face 4)
            elif new_direction == 1 :
                cnd = new_direction
                cxx = xx
                cyy = yy + 1
                if ( cyy > 49) :
                    # Move to Face 4
                    cxx = 99 
                    cyy = xx - 50
                    cnd = 2
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move Left (can take us to Face 5)
            elif new_direction == 2 :
                cnd = new_direction
                cxx = xx - 1
                cyy = yy
                if ( cxx < 100) :
                    # Move to Face 5
                    cxx = 99
                    cyy = yy
                    cnd = 2
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            # Move Up (can take us to Face 1)
            elif new_direction == 3 :
                cnd = new_direction
                cxx = xx
                cyy = yy - 1
                if ( cyy < 0 ) :
                    # Move to Face 1
                    cyy = 199
                    cxx = xx - 100
                    cnd = 3
                if grid[cyy][cxx] == '#' :
                    break
                elif grid[cyy][cxx] == '.' :
                        # Move
                        xx = cxx
                        yy = cyy
                        new_direction = cnd
                else :
                    # Should not get here
                    assert False
            else :
                assert False
        else :
            # no longer in known space
            print (xx, yy, new_direction)
            assert False

    return (xx, yy, new_direction)


def move_position(grid: list, x: int, y: int, direction: int, steps: int) -> tuple :

    xx = x
    yy = y

    max_y = len(grid)
    max_x = len(grid[yy])

    for _ in range(steps) :

        # Move right
        if direction == 0 :
            if ((xx + 1) > max_x) or (grid[yy][xx + 1] == " ") :
                new_xx = find_xstart_pos(grid, yy)
                if grid[yy][new_xx] == "." :
                    xx = new_xx
                else :
                    break
            elif grid[yy][xx + 1] == "." :
                xx += 1
            elif grid[yy][xx + 1] == "#" :
                break
        # Move down
        elif direction == 1 :
            if ((yy + 1) == max_y) or (xx >= len(grid[yy + 1])) or (grid[yy + 1][xx] == " ") :
                new_yy = find_ystart_pos(grid, xx)
                if grid[new_yy][xx] == "." :
                    yy = new_yy
                else :
                    break
            elif grid[yy + 1][xx] == "." :
                yy += 1
            elif grid[yy + 1][xx] == "#" :
                break
        # Move left 
        elif direction == 2 :
            if (xx - 1 < 0) or (grid[yy][xx - 1] == " ") :
                new_xx = find_xstart_pos(grid, yy, True)
                if grid[yy][new_xx] == "." :
                    xx = new_xx
                else :
                    break
            elif grid[yy][xx - 1] == "." :
                xx -= 1
            elif grid[yy][xx - 1] == "#" :
                break
        # Move Up 
        elif direction == 3 :
            if (yy-1) < 0 or grid[yy - 1][xx] == " " :
                new_yy = find_ystart_pos(grid, xx, True)
                if grid[new_yy][xx] == "." :
                    yy = new_yy
                else :
                    break
            elif grid[yy - 1][xx] == "." :
                yy -= 1
            elif grid[yy - 1][xx] == "#" :
                break

    return (xx, yy)

def find_xstart_pos(grid: list, y: int, reverse = False) -> int:

    x = 0

    if not reverse : 
        for i in range(len(grid[y])) :
            if grid[y][i] == ' ' :
                pass
            else :
                x = i
                break
    else :
        for i in range(len(grid[y]) - 1, 0 , -1) :
            if grid[y][i] == ' ' :
                pass
            else :
                x = i
                break
    return x

def find_ystart_pos(grid: list, x: int, reverse = False) -> int:

    y = 0

    if not reverse : 
        for i in range(len(grid)) :
            if (x >= len(grid[i])) or (grid[i][x] == ' ') :
                pass
            else :
                y = i
                break
    else :
        for i in range(len(grid) - 1, 0 , -1) :
            if (x >= len(grid[i])) or (grid[i][x] == ' ') :
                pass
            else :
                y = i
                break

    return y

def part1(data: list[str]) -> int:

    retval = -1
    grid = []
    instructions = []
    tmp = ""
    instr = False

    pattern = re.compile(r"-?\d+")

    for line in data:
        line = line.strip("\n")
        line = line + " "

        if instr :
            tmp = line.strip()
            continue
        if line == " " : 
            instr = True
            continue
        grid.append(line)

    i = 0
    
    while i < len(tmp) :
        if tmp[i] == " " :
            break
        if tmp[i] == "R" or tmp[i] == "L" :
            instructions.append(tmp[i])
            i += 1
        else :
            m = pattern.search(tmp[i:])

            if m is not None :
                instructions.append(m.group())
                i += m.span()[1]

    x = find_xstart_pos(grid, 0)
    y = 0
    facing = 0

    for i in range(len (instructions)) :

        instruction = instructions[i]

        # Rotate clockwise
        if instruction == "R" :
            facing = (facing + 1) % 4
        # Rotate CounterClockwise
        elif instruction == "L" :
            facing = (facing - 1) % 4
        # Move
        elif instruction.isnumeric() :
            steps = int(instruction)
            (x,y) = move_position(grid, x, y, facing, steps)
        else :
            continue

    retval = (1000 * (y + 1)) + (4 * (x + 1)) + facing
    return retval

def part2(data: list[str]) -> int:

    retval = -1
    grid = []
    instructions = []
    tmp = ""
    instr = False

    pattern = re.compile(r"-?\d+")

    for line in data:
        line = line.strip("\n")
        line = line + " "

        if instr :
            tmp = line.strip()
            continue
        if line == " " : 
            instr = True
            continue
        grid.append(line)

    i = 0
    
    while i < len(tmp) :
        if tmp[i] == " " :
            break
        if tmp[i] == "R" or tmp[i] == "L" :
            instructions.append(tmp[i])
            i += 1
        else :
            m = pattern.search(tmp[i:])

            if m is not None :
                instructions.append(m.group())
                i += m.span()[1]

    x = find_xstart_pos(grid, 0)
    y = 0
    facing = 0

    for i in range(len (instructions)) :

        instruction = instructions[i]

        # Rotate clockwise
        if instruction == "R" :
            facing = (facing + 1) % 4
        # Rotate CounterClockwise
        elif instruction == "L" :
            facing = (facing - 1) % 4
        # Move
        elif instruction.isnumeric() :
            steps = int(instruction)
            (x,y,facing) = move_cube_position(grid, x, y, facing, steps)
        else :
            continue

    retval = (1000 * (y + 1)) + (4 * (x + 1)) + facing
    return retval
