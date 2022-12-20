from collections import deque

def part1(data: list[str]) -> int:

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
        if valve != "AA" and not valves[valve] :
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

    print(distances)

    return -1


def part2(data: list[str]) -> int:

    return  -1
