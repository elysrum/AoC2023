import re

def part1(data: list[str]) -> int:
    total = 0

    for line in data:
        card = line.strip().split("|")
        left_side = card[0]
        right_side = card[1]
        winning_numbers = sorted([int(x) for x in (re.findall(r"\d+", left_side[9:]))])
        played_numbers = sorted([int(x) for x in (re.findall(r"\d+", right_side))])

        matched_number_count = 0

        for winning_number in winning_numbers :
            for played_number in played_numbers :
                if winning_number == played_number : 
                    matched_number_count += 1

        if matched_number_count == 1 : 
            total += 1
        elif matched_number_count > 1 :
            total += 2 ** (matched_number_count-1)
        else:
            pass

    return total

def part2(data: list[str]) -> int:
    total = 0
    card_number = 1

    card_count_dictionary = { }

    for line in data:
        card = line.strip().split("|")
        left_side = card[0]
        right_side = card[1]
        winning_numbers = sorted([int(x) for x in (re.findall(r"\d+", left_side[9:]))])
        played_numbers = sorted([int(x) for x in (re.findall(r"\d+", right_side))])

        matched_number_count = 0

        for winning_number in winning_numbers :
            for played_number in played_numbers :
                if winning_number == played_number : 
                    matched_number_count += 1

        card_count_dictionary[card_number] = (1, matched_number_count)

        card_number += 1

    for key, value in card_count_dictionary.items() :
        card_instances, additional_cards = value
        
        for _ in range (0, card_instances) :
            for index in range (key + 1, key + additional_cards + 1) :
                new_card_instances, new_additional_cards = card_count_dictionary[index]
                card_count_dictionary[index] = (new_card_instances + 1, new_additional_cards)

    for _, (card_instances, _) in card_count_dictionary.items() :
        total += card_instances

    return total
