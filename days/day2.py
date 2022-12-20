def part1(data: list[str]) -> int:
    score = 0

    for game in data:
        your_hand = game[0]
        my_hand = game[2]

        match your_hand:
            case 'A': # Rock
                match my_hand:
                    case 'X': # Rock - Draw
                        score += 1
                        score += 3 
                    case 'Y': # Paper - Win
                        score += 2
                        score += 6 # Draw 
                    case 'Z': # Scissors - Lose
                        score += 3
                        score += 0 
            case 'B': # Paper
                match my_hand:
                    case 'X': # Rock - Lose
                        score += 1
                        score += 0 
                    case 'Y': # Paper - Draw
                        score += 2
                        score += 3 
                    case 'Z': # Scissors - Win
                        score += 3
                        score += 6 
            case 'C': # Scissors
                match my_hand:
                    case 'X': # Rock - Win
                        score += 1
                        score += 6
                    case 'Y': # Paper - Lose
                        score += 2
                        score += 0 
                    case 'Z': # Scissors - Draw
                        score += 3
                        score += 3 
            case _:
                pass
    return score

def part2(data: list[str]) -> int:
    score = 0

    for game in data:
        your_hand = game[0]
        my_hand = game[2]

        match your_hand:
            case 'A': # Rock
                match my_hand:
                    case 'X': 
                        score += 3
                        score += 0 # Lose
                    case 'Y': 
                        score += 1
                        score += 3 # Draw 
                    case 'Z': 
                        score += 2
                        score += 6 # Win
            case 'B': # Paper
                match my_hand:
                    case 'X': 
                        score += 1
                        score += 0 # Lose
                    case 'Y': 
                        score += 2
                        score += 3 # Draw
                    case 'Z': 
                        score += 3
                        score += 6 # Win
            case 'C': # Scissors
                match my_hand:
                    case 'X': 
                        score += 2
                        score += 0 # Lose
                    case 'Y': 
                        score += 3
                        score += 3 # Draw
                    case 'Z': 
                        score += 1
                        score += 6 # Win
            case _:
                pass
    return score
