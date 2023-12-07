import collections
import functools

suite = {"A" : 14,
        "K" : 13, 
        "Q" : 12,
        "J" : 11,
        "T" : 10,
        "9" : 9,
        "8" : 8,
        "7" : 7,
        "6" : 6,
        "5" : 5,
        "4" : 4,
        "3" : 3,
        "2" : 2}

jokerSuite = {"A" : 14,
        "K" : 13, 
        "Q" : 12,
        "J" : 1,
        "T" : 10,
        "9" : 9,
        "8" : 8,
        "7" : 7,
        "6" : 6,
        "5" : 5,
        "4" : 4,
        "3" : 3,
        "2" : 2}


class Hand():

    def __init__(self, cards: str, bid: int) -> None:
        self.cards = cards
        self.card_count = collections.Counter()
        self.bid = bid
        self.value = 0

        for card in self.cards:
            self.card_count[card] += 1

        #Work out value

        num = len(self.card_count)

        # Five of a kind
        if num == 1:
            value = 6
        # Four of a kind or Full Nhouse
        elif num == 2:
            # Four of a kind
            if (self.card_count.most_common()[0][1] == 4):
                value = 5
            else :
                value = 4 
        # Three of a Kind or Two Pair
        elif num == 3:
            # Three of a Kind
            if (self.card_count.most_common()[0][1] == 3) :
                value = 3
            else :
                value = 2
        # One Pair
        elif num == 4:
            value = 1
        else:
            value = 0

        self.value = value

        return
    
    def __str__(self) -> str:

        return "{" + self.cards + ":" + str(self.value) + ":" + str(self.bid) + "}"


class JokerHand():

    def __init__(self, cards: str, bid: int) -> None:
        self.cards = cards
        self.card_count = collections.Counter()
        self.bid = bid
        self.value = 0
        self.numJokers = 0

        for card in self.cards:
            self.card_count[card] += 1

        #Work out value
        self.numJokers = self.card_count['J']

        if self.numJokers > 0 and self.numJokers < 5:
            self.card_count['J'] = 0
            self.card_count = +self.card_count
            mostCommon = self.card_count.most_common()[0]
            self.card_count[mostCommon[0]] += self.numJokers


        # if self.numJokers == 5:
        #      num = 1
        # else:
        #      num = len(self.card_count)
        num = len(self.card_count)

        # Five of a kind
        if num == 1:
            value = 6
        # Four of a kind or Full Nhouse
        elif num == 2:
            # Four of a kind
            if (self.card_count.most_common()[0][1] == 4):
                value = 5
            else :
                value = 4 
        # Three of a Kind or Two Pair
        elif num == 3:
            # Three of a Kind
            if (self.card_count.most_common()[0][1] == 3) :
                value = 3
            else :
                value = 2
        # One Pair
        elif num == 4:
            value = 1
        else:
            value = 0

        self.value = value

        return
    
    def __str__(self) -> str:

        return "{" + str(self.cards) + ":" + str(self.value) + "}"
    
    
def comparehands (left: Hand, right: Hand) -> int:

    cmp = left.value - right.value

    if cmp != 0:
        return cmp
    else:
        for i in range (0, 6):
            if left.cards[i] == right.cards[i] :
                cmp = 0
            else:
                cmp = suite[left.cards[i]] - suite[right.cards[i]]
                if cmp != 0 :
                    return cmp
    return cmp

def compareJokerhands (left: JokerHand, right: JokerHand) -> int:

    cmp = left.value - right.value

    if cmp != 0:
        return cmp
    else:
        for i in range (0, 6):
            if left.cards[i] == right.cards[i] :
                cmp = 0
            else:
                    cmp = jokerSuite[left.cards[i]] - jokerSuite[right.cards[i]]
                    if cmp != 0 :
                        return cmp
                    else:
                        cmp = 0
    return cmp

def part1(data: list[str]) -> int:

    hands = []

    for line in data:
        parts = line.split()
        hands.append(Hand(parts[0], int(parts[1])))

    sorted_hands = sorted(hands, key=functools.cmp_to_key(comparehands))

    retVal = 0
    i = 1
    for hand in sorted_hands:
        retVal = retVal + (i * hand.bid)
        i += 1

    return retVal

def part2(data: list[str]) -> int:
    hands = []

    for line in data:
        parts = line.split()
        hands.append(JokerHand(parts[0], int(parts[1])))

    sorted_hands = sorted(hands, key=functools.cmp_to_key(compareJokerhands))

    retVal = 0
    i = 1
    for hand in sorted_hands:
        retVal = retVal + (i * hand.bid)
        i += 1

    return retVal