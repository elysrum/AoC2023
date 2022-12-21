import os

def read_day_data(day_number: int) -> list[str]:

    mac_file_name = f"input/day{day_number}.txt"
    windows_file_name = f"input/day{day_number}.txt"
    
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
