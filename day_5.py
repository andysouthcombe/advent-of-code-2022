import re
from aoc_utils import read_file_of_strings_into_one_string

def load_stacks(filename):
    raw_stacks = read_file_of_strings_into_one_string(filename).splitlines()
    number_of_stacks = int(max(raw_stacks[-1].split(' ')))
    list_of_stacks = []
    for stack in range(0,number_of_stacks):
        this_stack = []
        for line in raw_stacks[:-1]:
            if line[1+(stack*4)] != ' ':
                this_stack.append(line[1+(stack*4)])
        list_of_stacks.append(this_stack)
    return list_of_stacks
    
def load_moves(filename):
    string_moves = [re.findall(r'[0-9]+',move) for move in read_file_of_strings_into_one_string(filename).splitlines()]
    return [[int(move) for move in moves]  for moves in string_moves]
    