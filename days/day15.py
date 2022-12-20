
def process_sensors(data: list[str], beacon_coords: set) -> list:

    r = 0
    sensor_loc = (0,0)
    beacon_loc = (0,0)
    sensor_coords = []

    for line in data :
        words = line.split()
        sensor_loc = (int(words[2][2:-1]), int(words[3][2:-1]))
        beacon_loc = (int(words[8][2:-1]), int(words[9][2:]))

        r = abs(sensor_loc[0]-beacon_loc[0]) + abs(sensor_loc[1]-beacon_loc[1])

        sensor_coords.append((sensor_loc, r))
        beacon_coords.add(beacon_loc)

    return sensor_coords

def overlay_sensor_footprint(sensor_data: list, beacons: set, row: int) -> set :

    grid = set()

    for sensor in sensor_data :
        (x,y), r = sensor

        for yd in range(r) :
            if (y+yd) == row or (y-yd) == row :
                        
                for xd in range(-(r-yd), (r-yd)+1) :
                    if (y+yd) == row and ((x + xd, y + yd) not in beacons):
                        grid.add((x + xd, y + yd))
                    elif (y-yd) == row and ((x + xd, y - yd) not in beacons): 
                        grid.add((x + xd, y - yd))
                    else:
                        pass

    return grid

def find_distress_beacon(sensor_data: list, max_xy: int) -> int :

    for y in range(max_xy + 1) :
        intervals = []

        for sensor, d in sensor_data :

            offset = d - abs(sensor[1] - y)

            if offset < 0: 
                continue

            low_x = sensor[0] - offset
            high_x = sensor[0] + offset

            intervals.append((low_x, high_x))

        intervals.sort()

        merged_intervals = []

        for start, end in intervals:
            if not merged_intervals :
                merged_intervals.append([start, end])
                continue
            
            prev_start, prev_end = merged_intervals[-1]

            if start > prev_end + 1:
                merged_intervals.append([start, end])
                continue

            merged_intervals[-1][1] = max(prev_end, end)

        x = 0
        for start, end in merged_intervals :
            if x < start:
                return  x * 4000000 + y

            x = max(end + 1, x)

            if x > max_xy : 
                break

    return -1

def part1(data: list[str], row: int) -> int:

    beacons = set()

    sensor_data = process_sensors(data, beacons)

    grid = overlay_sensor_footprint(sensor_data, beacons, row)

    return len(grid)


def part2(data: list[str], row: int) -> int:

    beacons = set()

    sensor_data = process_sensors(data, beacons)

    val = find_distress_beacon(sensor_data, row)

    return  val
