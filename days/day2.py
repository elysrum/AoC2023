
def part1(data: list[str]) -> int:
    games_total = 0

    max_red = 12
    max_blue = 14
    max_green = 13

    for game in data:
        bust = False
        line_parts = game.strip().split(":")
        game_number = line_parts[0].split()[-1]

        game_data = line_parts[1].split(";")

        
        for game in game_data :
            red_count = 0
            blue_count = 0
            green_count = 0

            cubes = game.split(",")

            for cube in cubes :
                hand = cube.split()
                match hand[1] :
                    case "red" :
                        red_count += int(hand[0])

                    case "green" :
                        green_count += int(hand[0])

                    case "blue" :
                        blue_count += int(hand[0])
            if red_count > max_red or \
                blue_count > max_blue or \
                green_count > max_green :
                bust = True
        
        if not bust :
            games_total += int(game_number)

    return games_total

def part2(data: list[str]) -> int:

    games_total = 0

    max_red = 1
    max_blue = 1
    max_green = 1

    for game in data:

        line_parts = game.strip().split(":")
        game_number = line_parts[0].split()[-1]

        game_data = line_parts[1].split(";")
        power_val = 0

        for game in game_data :
            red_count = 0
            blue_count = 0
            green_count = 0

            cubes = game.split(",")

            for cube in cubes :
                hand = cube.split()
                match hand[1] :
                    case "red" :
                        red_count += int(hand[0])
                        if red_count > max_red :
                            max_red = red_count

                    case "green" :
                        green_count += int(hand[0])
                        if green_count > max_green :
                            max_green = green_count
                    case "blue" :
                        blue_count += int(hand[0])
                        if blue_count > max_blue:
                            max_blue = blue_count
            power_val = max_red * max_blue * max_green    
        
        games_total += power_val 
        max_red = 1
        max_blue = 1
        max_green = 1


    return games_total
