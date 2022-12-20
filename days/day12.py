from collections import deque


def process_elevations(grid: list[str]) -> list:

    Elevation = [ [0 for _ in range(0, len(grid[0]))] for _ in range(0, len(grid)) ]

    for r in range(len(grid)) :
        for c in range(len(grid[0])) :
            if grid[r][c] == 'S' :
                Elevation[r][c] = 1
            elif grid[r][c] == 'E' :
                Elevation[r][c] = 26
            else:
                Elevation[r][c] = ord(grid[r][c])-ord('a') + 1

    return Elevation

def create_grid(data: list[str]) -> list:

    grid = [ ]

    for r in data :
        grid.append(r.strip())
        

    return grid



def part1(data: list[str]) -> int:

    grid = create_grid(data)
    elevations = process_elevations(grid)

    queue = deque()
    dist = 0

    grid_height = len(grid)
    grid_width = len(grid[0])
    # find start location and add it to the queue for processing
    for r in range(grid_height) :
        for c in range(grid_width) :
            if grid[r][c] == 'S' :
                queue.append(((r,c),dist))

    traversed = set()
    
    while queue:
        (row, col), dist = queue.popleft()

        if (row,col) in traversed :
            continue

        traversed.add((row,col))

        if grid[row][col] == 'E':
            return dist

        # now check each position around the current coord
        new_row = row - 1
        new_col = col
        if new_row >= 0 and new_row < grid_height and new_col >= 0 and new_col < grid_width and elevations[new_row][new_col] <= 1 + elevations[row][col]:
                queue.append(((new_row,new_col), dist+1))

        new_row = row
        new_col = col - 1
        if new_row >= 0 and new_row < grid_height and new_col >= 0 and new_col < grid_width and elevations[new_row][new_col] <= 1 + elevations[row][col]:
                queue.append(((new_row,new_col), dist+1))

        new_row = row + 1
        new_col = col
        if new_row >= 0 and new_row < grid_height and new_col >= 0 and new_col < grid_width and elevations[new_row][new_col] <= 1 + elevations[row][col]:
                queue.append(((new_row,new_col), dist+1))

        new_row = row
        new_col = col + 1
        if new_row >= 0 and new_row < grid_height and new_col >= 0 and new_col < grid_width and elevations[new_row][new_col] <= 1 + elevations[row][col]:
                queue.append(((new_row,new_col), dist+1))

    return -1



def part2(data: list[str]) -> int:

    grid = create_grid(data)
    elevations = process_elevations(grid)

    queue = deque()
    dist = 0

    grid_height = len(grid)
    grid_width = len(grid[0])
    # find start location and add it to the queue for processing
    for r in range(grid_height) :
        for c in range(grid_width) :
            if elevations[r][c] == 1 :
                queue.append(((r,c),dist))

    traversed = set()
    
    while queue:
        (row, col), dist = queue.popleft()

        if (row,col) in traversed :
            continue

        traversed.add((row,col))

        if grid[row][col] == 'E':
            return dist

        # now check each position around the current coord
        new_row = row - 1
        new_col = col
        if new_row >= 0 and new_row < grid_height and new_col >= 0 and new_col < grid_width and elevations[new_row][new_col] <= 1 + elevations[row][col]:
                queue.append(((new_row,new_col), dist+1))

        new_row = row
        new_col = col - 1
        if new_row >= 0 and new_row < grid_height and new_col >= 0 and new_col < grid_width and elevations[new_row][new_col] <= 1 + elevations[row][col]:
                queue.append(((new_row,new_col), dist+1))

        new_row = row + 1
        new_col = col
        if new_row >= 0 and new_row < grid_height and new_col >= 0 and new_col < grid_width and elevations[new_row][new_col] <= 1 + elevations[row][col]:
                queue.append(((new_row,new_col), dist+1))

        new_row = row
        new_col = col + 1
        if new_row >= 0 and new_row < grid_height and new_col >= 0 and new_col < grid_width and elevations[new_row][new_col] <= 1 + elevations[row][col]:
                queue.append(((new_row,new_col), dist+1))

    return -1
