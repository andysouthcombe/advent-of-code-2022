from aoc_utils import read_file_of_strings
import string


def read_backpacks_split(filename):
    return [(backpack[:len(backpack)//2], backpack[len(backpack)//2:])  for backpack in read_file_of_strings(filename)]

def read_backpacks_non_split(filename):
    return read_file_of_strings(filename)

def get_common_item_type(backpack):
    compartment_1, compartment_2 = backpack
    return set(compartment_1).intersection(set(compartment_2)).pop()

def get_common_badge_type(backpacks):
    backpack_1, backpack_2, backpack_3 = backpacks
    return (set(backpack_1) & set(backpack_2) & set(backpack_3)).pop()

def score_common_item_type(item_type):
    return string.ascii_letters.find(item_type)+1

def sum_common_items(filename):
    backpacks = read_backpacks_split(filename)
    return sum([score_common_item_type(get_common_item_type(backpack)) for backpack in backpacks])

def sum_badge_labels(filename):
    backpacks = read_backpacks_non_split(filename)
    number_groups = len(backpacks)//3
    return sum([score_common_item_type(get_common_badge_type((backpacks[(0+(3*group_num))], backpacks[(1+(3*group_num))], backpacks[(2+(3*group_num))]))) for group_num in range(0,number_groups)])



if __name__ == '__main__':
    print(sum_common_items('input/day_3_input.txt'))
    print(sum_badge_labels('input/day_3_input.txt'))