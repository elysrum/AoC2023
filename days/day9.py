from collections import defaultdict

def part1(data: list[str]) -> int:


    Head = (0, 0)
    Tail = (0, 0)

    Tail_loc = {Tail}

    for instruction in data :
        direction, distance = instruction.strip().split()
    
        distance = int(distance)
        for i in range(distance) :

            head0 = Head[0]
            head1 = Head[1]
            if direction == "L" :
                head0 -= 1
            elif direction == "R" :
                head0 += 1
            elif direction == "U" :
                head1 += 1
            elif direction == "D" :
                head1 -= 1
            else : 
                pass

            Head = (head0, head1)
            Tail = move_tail(Head, Tail)
            Tail_loc.add(Tail)

    return len(Tail_loc)


def part2(data: list[str]) -> int:

    Head = (0, 0)

    Rope = [(0,0) for _ in range(9)]
    Tail_loc = set([Rope[8]])

    for instruction in data :
        direction, distance = instruction.strip().split()
    
        distance = int(distance)
        for _ in range(distance) :

            head0 = Head[0]
            head1 = Head[1]
            if direction == "L" :
                head0 -= 1
            elif direction == "R" :
                head0 += 1
            elif direction == "U" :
                head1 += 1
            elif direction == "D" :
                head1 -= 1
            else : 
                pass

            Head = (head0, head1)

            Rope[0] = move_tail(Head, Rope[0])
            for i in range(1, 9) :
                Rope[i] = move_tail(Rope[i-1], Rope[i])

            Tail_loc.add(Rope[8])

    return len(Tail_loc)

def move_tail(Head: tuple, Tail: tuple) -> tuple :


    tail0 = Tail[0]
    tail1 = Tail[1]

    if (Head[0] - Tail[0]) > 1  and (Head[1] - Tail[1]) == 0:
        tail0 += 1
    elif (Head[0] - Tail[0]) < -1 and (Head[1] - Tail[1]) == 0 :
        tail0 -= 1
    elif (Head[0] - Tail[0]) == 0 and (Head[1] - Tail[1]) > 1 :
        tail1 += 1
    elif (Head[0] - Tail[0]) == 0 and (Head[1] -  Tail[1]) < -1 :
        tail1 -= 1
    elif (((Head[0] - Tail[0]) > 1 and (Head[1] - Tail[1]) >= 1) or
          ((Head[0] - Tail[0]) >= 1 and (Head[1] - Tail[1]) > 1)) :
        tail0 += 1
        tail1 += 1
    elif (((Head[0] - Tail[0]) < -1 and (Head[1] - Tail[1]) >= 1) or 
          ((Head[0] - Tail[0]) <= -1 and (Head[1] - Tail[1]) > 1)) :
        tail0 -= 1
        tail1 += 1
    elif (((Head[0] - Tail[0]) > 1 and (Head[1] - Tail[1]) <= -1) or 
          ((Head[0] - Tail[0]) >= 1 and (Head[1] - Tail[1]) < -1 )) :
        tail0 += 1
        tail1 -= 1
    elif (((Head[0] - Tail[0]) < -1 and (Head[1] - Tail[1]) <= -1) or 
          ((Head[0] - Tail[0]) <= -1 and (Head[1] - Tail[1]) < -1)) :
        tail0 -= 1
        tail1 -= 1
    else :   # if Head[0] == Tail[0] and Head[1] == Tail[1] 
        pass

    return (tail0,tail1)