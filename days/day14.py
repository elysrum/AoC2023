
min_x_coord = 500
max_x_coord = 500
max_y_coord = 0


def build_map(data: list[str]) -> set:

    global min_x_coord 
    global max_x_coord 
    global max_y_coord 

    grid = set()

    coords = []

    point = (int, int)
    for line in data : 
        coords = line.split("->")
    
        i = 1
        start_point = eval(coords[i-1])
        while i < len(coords) :
            new_x = max_x_coord
            end_point = eval(coords[i])

            if start_point[0] == end_point[0] and start_point[1] < end_point[1]:
                # iterate +ve along y axis
                new_y = start_point[1]
                while new_y <= end_point[1] :
                    grid.add((start_point[0], new_y))
                    new_y += 1
            elif start_point[0] == end_point[0] and start_point[1] > end_point[1]: 
                # iterate -ve along y axis
                new_y = start_point[1]
                while new_y >= end_point[1] :
                    grid.add((start_point[0], new_y))
                    new_y -= 1
            elif start_point[1] == end_point[1] and start_point[0] < end_point[0]:
                # iterate +ve along x axis
                new_x = start_point[0]
                while new_x <= end_point[0] :
                    grid.add((new_x, start_point[1]))
                    new_x += 1
            elif start_point[1] == end_point[1] and start_point[0] > end_point[0]: 
                # iterate -ve along x axis
                new_x = start_point[0]
                while new_x >= end_point[0] :
                    grid.add((new_x, start_point[1]))
                    new_x -= 1

            min_x_coord = min(min_x_coord, start_point[0], end_point[0])
            max_x_coord = max(max_x_coord, start_point[0], end_point[0])
            max_y_coord = max(max_y_coord, start_point[1], end_point[1])

            start_point = end_point
            i += 1


    # Add a Floor into map
    max_y_coord += 2

    for x in range(min_x_coord-2000, max_x_coord+2000) :
         grid.add((x, max_y_coord))

    return grid

def drop_sand_grain_pt1(grid, start) -> int :

    global min_x_coord
    global max_x_coord

    start_point = start

    ret = 0

    if start_point[0] < min_x_coord or start_point[0] > max_x_coord :
        ret = -1
    else :
        if start_point not in grid:
            # nothing blocking, drop
            ret = drop_sand_grain_pt1(grid, (start_point[0], start_point[1] + 1))
        elif (start_point[0] - 1, start_point[1]) not in grid :
            # something blocking, can we go left
            ret =  drop_sand_grain_pt1(grid, (start_point[0] - 1, start_point[1]))
        elif (start_point[0] + 1, start_point[1]) not in grid :
            # something blocking, can we go left
            ret =  drop_sand_grain_pt1(grid, (start_point[0] + 1, start_point[1]))
        else :
            grid.add((start_point[0], start_point[1] - 1))
            ret = 0

    return ret

def drop_sand_grain_pt2(grid, start) -> int :

    global min_x_coord
    global max_x_coord
    global max_y_coord

    start_point = start

    ret = 0

        
    if (500,0) in grid:
        ret = -1
    else :
        if start_point not in grid :
            # nothing blocking, drop
            ret = drop_sand_grain_pt2(grid, (start_point[0], start_point[1] + 1))
        elif (start_point[0] - 1, start_point[1]) not in grid :
            # something blocking, can we go left
            ret =  drop_sand_grain_pt2(grid, (start_point[0] - 1, start_point[1]))
        elif (start_point[0] + 1, start_point[1]) not in grid :
            # something blocking, can we go right
            ret =  drop_sand_grain_pt2(grid, (start_point[0] + 1, start_point[1]))
        else :
            grid.add((start_point[0], start_point[1] - 1))
            ret = 0
    
    if start_point[1] >= max_y_coord :
        grid.add((start_point[0], start_point[1] - 1))
        ret = 0

        
    return ret

def part1(data: list[str]) -> int:


    grid_map = build_map(data)
    start_point = (500,0)

    grains = 0
    while True :
        grains += 1
        ret = drop_sand_grain_pt1(grid_map, start_point)
        if ret == -1 :
            break

    return grains - 1




def part2(data: list[str]) -> int:

    grid_map = build_map(data)
    start_point = (500,0)

    grains = 0
    while True :
        grains += 1
        ret = drop_sand_grain_pt2(grid_map, start_point)
        if ret == -1 :
            break

    return grains - 1
