from aoc_utils import read_file_of_strings

def sum_each_elf(file_name):
    raw_elves = read_file_of_strings(file_name)
    elf_calories = 0
    elf_calories_list = []
    for calories in raw_elves:
        if calories == '':
            elf_calories_list.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(calories)
    elf_calories_list.append(elf_calories)
    return elf_calories_list

def get_elf_with_most_calories(file_name):
    elf_calories_list = sum_each_elf(file_name)
    return max(elf_calories_list)

if __name__ == '__main__':
    print(get_elf_with_most_calories('input/day_1_input.txt'))