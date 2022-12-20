from collections import defaultdict

def part1(data: list[str]) -> int:

    num_rows = len(data)
    num_cols = len(data[0].strip())

    grid = []
    Visible = defaultdict(bool)

    for line in data :
        grid.append(line.strip())
    
    for a in range(num_rows) :
        for b in range(num_cols) :

            # Trees on the edge of the grid are visible by default
            if a == 0 or b == 0 or a == (num_rows - 1) or b == (num_cols - 1):
                Visible[(a,b)] = True
            else :
                Visible[(a,b)] = False

            ax = b + 1
            east = True
            while ax < num_cols : # Walk along x Axis and see if anything obscures us from the east
                if grid[a][b] <= grid[a][ax] :
                    east = False # Current tree is obscured in this direction, no need to look further
                    break                    
                else :
                    east = True 
                ax += 1

            ax = b - 1
            west = True
            while ax >= 0  : # Walk backwards along x Axis and see if anything obscures us from the west
                if grid[a][b] <= grid[a][ax] :
                    west = False
                    break
                else :
                    west = True
                ax -= 1

            # Now repeat, but for Y axis
            ay = a + 1
            south = False
            while ay < num_rows : # Walk along y Axis and see if anything obscures us from the south
                if grid[a][b] <= grid[ay][b] :
                    south = False
                    break                    
                else :
                    south = True
                ay += 1

            ay = a - 1
            north = False
            while ay >= 0 : # Walk backwards along y Axis and see if anything obscures us from the north
                if grid[a][b] <= grid[ay][b] :
                    north = False
                    break                    
                else :
                    north = True
                ay -= 1

            if north or south or west or east :
                Visible[(a,b)] = True

    count = sum(1 for item in Visible.items() if item[1])

    return count

def part2(data: list[str]) -> int:

    num_rows = len(data)
    num_cols = len(data[0].strip())

    grid = []
    scenic_store = 0
    scenic_score = 0

    for line in data :
        grid.append(line.strip())
    
    for a in range(num_rows) :
        for b in range(num_cols) :

            ax = b + 1
            east_dist = 0
            while ax < num_cols : # Walk along x Axis and see if anything obscures us from the east
                if grid[a][b] <= grid[a][ax] :
                    east_dist += 1
                    break                    
                else :
                    east_dist += 1
                ax += 1

            ax = b - 1
            west_dist = 0
            while ax >= 0  : # Walk backwards along x Axis and see if anything obscures us from the west
                if grid[a][b] <= grid[a][ax] :
                    west_dist += 1
                    break
                else :
                    west_dist += 1
                ax -= 1

            # Now repeat, but for Y axis
            ay = a + 1
            south_dist = 0
            while ay < num_rows : # Walk along y Axis and see if anything obscures us from the south
                if grid[a][b] <= grid[ay][b] :
                    south_dist += 1
                    break                    
                else :
                    south_dist += 1
                ay += 1

            ay = a - 1
            north_dist = 0
            while ay >= 0 : # Walk backwards along y Axis and see if anything obscures us from the north
                if grid[a][b] <= grid[ay][b] :
                    north_dist += 1
                    break                    
                else :
                    north_dist += 1
                ay -= 1

            scenic_score = (north_dist) * (south_dist) * (west_dist) * (east_dist)

            scenic_store = max(scenic_score, scenic_store)

    return scenic_store

