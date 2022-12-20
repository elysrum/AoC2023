def part1(data: list[str]) -> int:
    score = 0
    lowScoreDict = "abcdefghijklmnopqrstuvwxyz"
    highscoreDict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for sack in data:
        s=sack.strip()
        mid = round(len(s)/2)
        
        comp1 = set(s[:mid])
        comp2 = set(s[mid:])

        dupItem = (comp1 & comp2).pop()

        x = lowScoreDict.find(dupItem)
        if x == -1:
            x = highscoreDict.find(dupItem)
            x += 26
        
        score += x + 1

    return score

def part2(data: list[str]) -> int:
    score = 0
    lowScoreDict = "abcdefghijklmnopqrstuvwxyz"
    highscoreDict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(0, len(data), 3):
        sack1=set(data[i].strip())
        sack2=set(data[i+1].strip())
        sack3=set(data[i+2].strip())

        dupItem = (sack1 & sack2 & sack3).pop()

        x = lowScoreDict.find(dupItem)
        if x == -1:
            x = highscoreDict.find(dupItem)
            x += 26
        
        score += x + 1 # because find is 0 based

    return score