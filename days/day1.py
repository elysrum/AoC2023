import support

def part1(data: list[str]) -> int:

    sorted_elfs = sumupelves(data)
    return sorted_elfs[-1]

def part2(data: list[str]) -> int:

    sorted_elfs = sumupelves(data)
    return sorted_elfs[-1] + sorted_elfs[-2] + sorted_elfs[-3]

def sumupelves(data: list[str]):
    elf_cal = 0
    elfs = []

    for calories in data:
        if calories == '\n':
            elfs.append(elf_cal)
            elf_cal = 0
        else:
            elf_cal = elf_cal + int(calories)

    return sorted(elfs)

