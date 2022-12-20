from collections import Counter

def part1(data: str) -> int:

    i = 0
    while i < len(data):
        sequence = data [i:i+4]
        if find_dups(sequence):
            i+=1
        else :
            return (i + 4)
    return 0

def part2(data: str) -> int:

    i = 0
    while i < len(data):
        sequence = data [i:i+14]
        if find_dups(sequence):
            i+=1
        else :
            return (i + 14)
    return 0

    return 0

def find_dups(input):
 
    # create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    WC = Counter(input)
 
    # Finding no. of  occurrence of a character
    # and get the index of it.
    dupes = False
    for letter, count in WC.items():
        if (count > 1):
            dupes = True
            break
    
    return dupes
 