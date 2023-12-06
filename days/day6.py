
def part1(data: list) -> int:

    times = [int(x) for x in (data[0].strip().split(":")[1].split())]
    distances = [int(x) for x in (data[1].strip().split(":")[1].split())]

    i = 0
    win_records = []

    while i < len(times) :

        time = times[i]
        distance = distances[i]
        win = 0
        for y in range(1, time) :
            time_to_travel = (time - y)
            max_distance = y * time_to_travel
            if max_distance > distance : 
                win += 1

        win_records.append(win)
        i += 1
    
    result = 1
    for x in win_records:
        result *= x
    
    return result

def part2(data: list) -> int:

    numbers1 = data[0].strip().split(":")[1].split()
    numbers2 = data[1].strip().split(":")[1].split()

    time = int(''.join(numbers1))
    distance = int(''.join(numbers2))

    win = 0
    for y in range(1, time) :
        time_to_travel = (time - y)
        max_distance = y * time_to_travel
        if max_distance > distance : 
            win += 1

    return win

