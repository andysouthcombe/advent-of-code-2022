from aoc_utils import read_file_of_strings,read_file_of_strings_into_one_string

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

def sum_each_elf_simple(file_name):
    elf_text = read_file_of_strings_into_one_string(file_name)
    elf_list = [sum(map(int,elf.split('\n'))) for elf in elf_text.split('\n\n')]
    print
    return elf_list

def get_elf_with_most_calories(file_name):
    elf_calories_list = sum_each_elf_simple(file_name)
    return max(elf_calories_list)

def get_calories_top_three_elves(file_name):
    elf_calories_list = sum_each_elf_simple(file_name)
    return sum(sorted(elf_calories_list,reverse=True)[0:3])

if __name__ == '__main__':
    print(get_elf_with_most_calories('input/day_1_input.txt'))
    print(get_calories_top_three_elves('input/day_1_input.txt'))