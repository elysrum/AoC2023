from collections import deque
import json


def dfs(cache: dict, valves: dict, distances: dict, opened: dict, time: int, valve: str) -> int : 

    maxtime = 0
    hash_val = hash(json.dumps(opened, sort_keys=True))

    if (valve, time, hash_val) in cache :
        return cache[(valve, time, hash_val)]

    opened[valve] = 1

    for neighbour in distances[valve] :
    
        if neighbour in opened: 
            continue

        remaining_time = time - distances[valve][neighbour] - 1

        if remaining_time <= 0 :
            continue
        maxtime = max(maxtime, dfs(cache, valves, distances, opened, remaining_time, neighbour) + int(valves[neighbour]) * remaining_time)

    cache[(valve, time, hash_val)] = maxtime

    del opened[valve]

    return maxtime


def part1(data: list[str]) -> int:

    retval = -1
    valves = {}
    tunnels = {}

    for line in data :
        line = line.strip()
        words = line.split(" ")
        valve = words[1]
        rate = words[4]
        rate = rate.removeprefix("rate=").strip(";")
        targets = words[9:]

        for i in range(len(targets)) :
            target = targets[i].strip(",")
            targets[i] = target

        valves[valve] = int(rate)
        tunnels[valve] = targets

    distances= {}

    for valve in valves:
        # if we are not AA or the Valve has 0 flow rate, we want to ignore it
        if valve != "AA" and valves[valve] == 0:
            continue

        #Store DIstance from valve to istelf = 0
        #Also Add Start position
        distances[valve] = {valve: 0, "AA": 0}
        visited = {valve}

        searchQ = deque([(valve, int(0))])
        
        while searchQ :
            v,d = searchQ.popleft()

            for neighbour in tunnels[v] :
                if neighbour in visited:
                    continue
                visited.add(neighbour)

                if valves[neighbour] != 0:
                    distances[valve][neighbour] = d + 1

                searchQ.append((neighbour, d+1))

        del distances[valve][valve]
        if valve != "AA" :
            del distances[valve]["AA"]

    opened = {}
    cache = {}

    retval = dfs(cache, valves, distances, opened, 30, "AA")

    return retval


def part2(data: list[str]) -> int:

    return  -1
