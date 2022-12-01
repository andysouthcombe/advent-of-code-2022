from aoc_utils import read_file_of_strings

def sum_each_elf(file_name):
    raw_elves = read_file_of_strings(file_name)
    elf = 1
    elf_calories = 0
    elf_list = []
    for calories in raw_elves:
        if calories == '':
            elf_list.append((elf,elf_calories))
            elf += 1
            elf_calories = 0
        else:
            elf_calories += int(calories)
    elf_list.append((elf,elf_calories))
    return elf_list

