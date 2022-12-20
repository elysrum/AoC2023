import os

def read_day_data(day_number: int) -> list[str]:

    mac_file_name = f"/Users/paul/Library/CloudStorage/OneDrive-Personal/Documents/ZZZ - Personal/Advent of Code/2022/input/day{day_number}.txt"
    windows_file_name = f"C:\\Users\\Paul\\OneDrive\\Documents\\ZZZ - Personal\\Advent of Code\\2022\\input\\day{day_number}.txt"
    
    if os.name == "nt" : 
        file_name = windows_file_name
    elif os.name == "posix" :
        file_name = mac_file_name
    else:
        file_name = "linux file name here"
 
    with open(file_name) as f:
        data = f.readlines()
    f.close()

    return data
