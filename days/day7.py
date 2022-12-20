from collections import defaultdict


def part1(data: list[str]) -> int:


    dirs = walk_file_system(data)
    total = 0
 
    for dir, size in dirs.items() :
        if size <= 100000:
            total += size
    
    return total

def part2(data: list[str]) -> int:

    dirs = walk_file_system(data)
    total_avail = 70000000
    target_space = 30000000
    actual_space = dirs["/"]

    space_req = (target_space - (total_avail - actual_space))

    delete_amount = 999999999
    for dir, size in dirs.items() :
        if size >= space_req:
            delete_amount = min(delete_amount, size)
    
    return delete_amount

def walk_file_system(data: list[str]) -> defaultdict :
    
    dirs = defaultdict(int)
    current_dir = []
    sz = 0
    for command_line in data:
        words = command_line.strip().split()
        if words[0] == "$" :
            if words[1] == "ls" :
                pass
            elif words[1] == "cd" :
                if words[2] == ".." :
                    # move up the directory
                    current_dir.pop()
                else :
                    current_dir.append(words[2])
                    # move down directory
        elif words[0] == "dir" :
            pass
        elif words[0].isnumeric() :
            # file size and name
            sz = int(words[0])
            for i in range(1, len(current_dir)+1) : 
                dirs["/".join(current_dir[:i])] += sz
    
    return dirs


 