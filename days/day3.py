import re
def part1(data: list[str]) -> int:
    parts_list = []
    parts_sum = 0

    # For every line in the data set
    parts_in_line = []
    prev_parts_in_line = []
    symbol_locn = []
    prev_symbol_locn = []

    for line in data:

        part_number = ""
        start_found = False
        end_found = False
        start_loc = 0
        part_length = 0

        # Extract every numnber on the line with start and length
        for index, char in enumerate(line.strip()) :
            
            # Is the character a number, yes build the number string
            if char.isnumeric() :
                part_number += char
                part_length += 1
                if not start_found : 
                    start_loc = index
                    start_found = True
            elif char == '.':
                if start_found :
                    end_found = True
            else :
                symbol_locn.append((char, index))
                if start_found :
                    end_found = True
           
            if start_found and end_found :
                start_found = False
                end_found = False
                parts_in_line.append((part_number, start_loc, part_length))
                part_number = ""
                start_loc = 0
                part_length = 0
        
        #Need to cater for the case where we run out of string
        if start_found and not end_found :
            parts_in_line.append((part_number, start_loc, part_length))

        # Match Current Line Numbers against Current Line Symbols

        for (part_number, start_loc, part_length) in parts_in_line[:] :
            for (symbol, symbol_index) in symbol_locn :
                if (symbol_index >= start_loc - 1) and (symbol_index <= start_loc + part_length) : 
                    parts_list.append(part_number)
                    parts_in_line.remove((part_number, start_loc, part_length))

            # Match against previous line symbols
        for (part_number, start_loc, part_length) in parts_in_line[:] :
            for (symbol, symbol_index) in prev_symbol_locn :
                if (symbol_index >= start_loc - 1) and (symbol_index <= start_loc + part_length) : 
                    parts_list.append(part_number)
                    parts_in_line.remove((part_number, start_loc, part_length))

        #Match previous numbers agains current symbols
        for (part_number, start_loc, part_length) in prev_parts_in_line :
            for (symbol, symbol_index) in symbol_locn :
                if (symbol_index >= start_loc - 1) and (symbol_index <= start_loc + part_length) : 
                    parts_list.append(part_number)



        # Copy Current Symbols to Previous Symbols
        prev_symbol_locn = symbol_locn.copy()
        prev_parts_in_line = parts_in_line.copy()
        parts_in_line = []
        symbol_locn = []

    for part in parts_list :
        parts_sum += int(part)

    return parts_sum

def part2(data: list[str]) -> int:
    parts_list = []
    parts_sum = 0

    # For every line in the data set
    parts_in_line = []
    prev_parts_in_line = []
    symbol_locn = []
    prev_symbol_locn = []

    line_number = 0
    for line in data:

        part_number = ""
        start_found = False
        end_found = False
        start_loc = 0
        part_length = 0

        # Extract every numnber on the line with start and length
        for index, char in enumerate(line.strip()) :
            
            # Is the character a number, yes build the number string
            if char.isnumeric() :
                part_number += char
                part_length += 1
                if not start_found : 
                    start_loc = index
                    start_found = True
            elif char == '.':
                if start_found :
                    end_found = True
            else :
                if start_found :
                    end_found = True
                if char == '*' :
                    symbol_locn.append((char, index))
            
            if start_found and end_found :
                start_found = False
                end_found = False
                parts_in_line.append((part_number, start_loc, part_length))
                part_number = ""
                start_loc = 0
                part_length = 0
        
        #Need to cater for the case where we run out of string
        if start_found and not end_found :
            parts_in_line.append((part_number, start_loc, part_length))

        # Match Current Line Numbers against Current Line Symbols

        for (part_number, start_loc, part_length) in parts_in_line[:] :
            for (symbol, symbol_index) in symbol_locn :
                if (symbol_index >= start_loc - 1) and (symbol_index <= start_loc + part_length) : 
                    parts_list.append((line_number, symbol_index, part_number))
                    parts_in_line.remove((part_number, start_loc, part_length))

            # Match against previous line symbols
        for (part_number, start_loc, part_length) in parts_in_line[:] :
            for (symbol, symbol_index) in prev_symbol_locn :
                if (symbol_index >= start_loc - 1) and (symbol_index <= start_loc + part_length) : 
                    parts_list.append((line_number, symbol_index, part_number))
                    parts_in_line.remove((part_number, start_loc, part_length))

        #Match previous numbers agains current symbols
        for (part_number, start_loc, part_length) in prev_parts_in_line :
            for (symbol, symbol_index) in symbol_locn :
                if (symbol_index >= start_loc - 1) and (symbol_index <= start_loc + part_length) : 
                    parts_list.append((line_number, symbol_index, part_number))



        # Copy Current Symbols to Previous Symbols
        prev_symbol_locn = symbol_locn.copy()
        prev_parts_in_line = parts_in_line.copy()
        parts_in_line = []
        symbol_locn = []
        line_number += 1
    
    for (line_number1, index1, part1) in parts_list[:] :
        parts_list.remove((line_number1, index1, part1))
        for (line_number2, index2, part2) in parts_list :
            if index1 == index2 and (line_number1 == line_number2 or line_number1 == line_number2 - 1) :
                parts_sum += int(part1) * int(part2)

    return parts_sum