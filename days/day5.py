def part1(data: list[str]) -> str:

    num_stacks, remainder = divmod(len(data[0]), 4)
    process_stacks = True

    stacks = [[] for _ in range(num_stacks)]
    stack_strings = []
    

    for row in data:
        if row.find("[") >= 0 :
            #  Still in the Stack Building Phase
            stack_strings.insert(0,row)
        elif row.find("move") >= 0:
            # Now in the stack movement phase
            instructions = row.split()
            count = int(instructions[1])
            from_stack = int(instructions[3]) - 1
            to_stack = int(instructions[5]) - 1

            i = 0
            while i < count :
                stacks[to_stack].append(stacks[from_stack].pop())
                i += 1
        else:
            # Ignore blank lines and stack numbers
            if process_stacks :
                for string_row in stack_strings :
                    for i in range(0, num_stacks):
                        offset = i*4
                        if string_row[offset] == "[" :
                            stacks[i].append(string_row[offset+1 : offset+2])
                        else:
                            pass
                process_stacks = False
            else :
                pass
    
    output = ""
    for i in range(0, num_stacks) :
        output = output + stacks[i].pop()
     
    return output

def part2(data: list[str]) -> str:

    num_stacks, remainder = divmod(len(data[0]), 4)
    process_stacks = True

    stacks = [[] for _ in range(num_stacks)]
    stack_strings = []
    

    for row in data:
        if row.find("[") >= 0 :
            #  Still in the Stack Building Phase
            stack_strings.insert(0,row)
        elif row.find("move") >= 0:
            # Now in the stack movement phase
            instructions = row.split()
            count = int(instructions[1])
            from_stack = int(instructions[3]) - 1
            to_stack = int(instructions[5]) - 1

            i = 0
            temp_stack = []
            while i < count :
                temp_stack.append(stacks[from_stack].pop())
                i += 1

            temp_stack.reverse()
            for z in temp_stack:
                stacks[to_stack].append(z)

        else:
            # Ignore blank lines and stack numbers
            if process_stacks :
                for string_row in stack_strings :
                    for i in range(0, num_stacks):
                        offset = i*4
                        if string_row[offset] == "[" :
                            stacks[i].append(string_row[offset+1 : offset+2])
                        else:
                            pass
                process_stacks = False
            else :
                pass
    
    output = ""
    for i in range(0, num_stacks) :
        output = output + stacks[i].pop()
     
    return output

