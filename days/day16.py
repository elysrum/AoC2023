from collections import deque

def dfs(cache: dict, valves: dict, indices: dict, distances: dict, bitmask: int, time: int, valve: str) -> int : 

    maxtime = 0

    if (valve, time, bitmask) in cache :
        return cache[(valve, time, bitmask)]


    for neighbour in distances[valve] :

        bit = 1 << indices[neighbour]

        if bit & bitmask:
            continue

        remaining_time = time - distances[valve][neighbour] - 1

        if remaining_time <= 0 :
            continue

        maxtime = max(maxtime, dfs(cache, valves, indices, distances, bit | bitmask, remaining_time, neighbour) + int(valves[neighbour]) * remaining_time)

        print (remaining_time)
    cache[(valve, time, bitmask)] = maxtime
    # print((valve, time, bitmask) ,  maxtime)
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

        valves[valve] = rate
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

    cache = {}
    indices = {}

    for i, valve in enumerate(valves) :
        if valve != "AA" and valves[valve] != 0 :
            indices[valve] = i

    retval = dfs(cache, valves, indices, distances, 0, 30, "AA")

    return retval


# def part1(data: list[str]) -> int :
#     valves = {}
#     tunnels = {}

#     for line in data:
#         line = line.strip()
#         valve = line.split()[1]
#         flow = int(line.split(";")[0].split("=")[1])
#         targets = line.split("to ")[1].split(" ", 1)[1].split(", ")
#         valves[valve] = flow
#         tunnels[valve] = targets

#     dists = {}
#     nonempty = []

#     for valve in valves:
#         if valve != "AA" and not valves[valve]:
#             continue
        
#         if valve != "AA":
#             nonempty.append(valve)

#         dists[valve] = {valve: 0, "AA": 0}
#         visited = {valve}
        
#         queue = deque([(0, valve)])
        
#         while queue:
#             distance, position = queue.popleft()
#             for neighbor in tunnels[position]:
#                 if neighbor in visited:
#                     continue
#                 visited.add(neighbor)
#                 if valves[neighbor]:
#                     dists[valve][neighbor] = distance + 1
#                 queue.append((distance + 1, neighbor))

#         del dists[valve][valve]
#         if valve != "AA":
#             del dists[valve]["AA"]

#     indices = {}

#     for index, element in enumerate(nonempty):
#         indices[element] = index

#     # cache = {}

#     def dfs(time, valve, bitmask):
#         # if (time, valve, bitmask) in cache:
#         #     return cache[(time, valve, bitmask)]
        
#         maxval = 0
#         for neighbor in dists[valve]:
#             bit = 1 << indices[neighbor]
#             if bitmask & bit:
#                 continue
#             remtime = time - dists[valve][neighbor] - 1
#             if remtime <= 0:
#                 continue
#             maxval = max(maxval, dfs(remtime, neighbor, bitmask | bit) + valves[neighbor] * remtime)
#             # maxval = max(maxval, dfs(remtime, neighbor, bitmask) + valves[neighbor] * remtime)
            
            
#         # cache[(time, valve, bitmask)] = maxval
#         return maxval

#     return dfs(30, "AA", 0)


def part2(data: list[str]) -> int:

    return  -1
