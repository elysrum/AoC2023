from functools import cmp_to_key

def compare_packets(left, right) -> int:

    if isinstance(left, int) and isinstance(right, int) :
        if left < right :
            return -1
        elif left == right :
            return 0
        else :
            return 1
    elif isinstance(left, list) and isinstance(right, list) :
        i = 0
        while i < len(left) and i < len(right) :
            cmp = compare_packets(left[i], right[i])

            if cmp == -1:
                return -1
            if cmp == 1:
                return  1
            #equal
            i += 1
        if i == len(left) and i < len(right) :
            return -1
        elif i == len(right) and i < len(left) :
            return 1
        else : 
            return 0

    elif isinstance(left, int) and isinstance(right, list) :
        return compare_packets([left], right)
    else :
        return compare_packets(left, [right])

    return 0


def part1(data: list[str]) -> int:

    r = 0
    count = 0
    while r < len(data) : 

        if data[r] == "\n" :
            r +=1
        else : 
            packet1 = eval(data[r].strip())
            packet2 = eval(data[r+1].strip())
            ret_val = compare_packets(packet1, packet2)

            if (ret_val == -1) :
                count += (r // 3) + 1

            r += 2

    return count



def part2(data: list[str]) -> int:

    r = 0
    count = 1
    packets = []

    while r < len(data) : 

        if data[r] == "\n" :
            r +=1
        else : 
            packet1 = eval(data[r].strip())
            packet2 = eval(data[r+1].strip())

            packets.append(packet1)
            packets.append(packet2)
            
            r += 2
            
    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key=cmp_to_key(compare_packets))

    for i, packet in enumerate(packets) :
        if packet == [[2]] or packet == [[6]] :
            count *= (i + 1)

    return count
