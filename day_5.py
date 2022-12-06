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

def move_stacks(stacks, move):
    number_of_crates=move[0]
    from_stack=move[1] - 1
    to_stack=move[2] - 1
    for crate in range(0,number_of_crates):
        stacks[to_stack] = [stacks[from_stack].pop(0)] + stacks[to_stack]
    return stacks

def move_stacks_part_two(stacks, move):
    number_of_crates=move[0]
    from_stack=move[1] - 1
    to_stack=move[2] - 1
    crates_being_moved = []
    for crate in range(0,number_of_crates):
        crates_being_moved += [stacks[from_stack].pop(0)]
    stacks[to_stack] = crates_being_moved + stacks[to_stack]
    return stacks

def run_moves_and_return_top_crates(moves_filename, stacks_filename):
    moves = load_moves(moves_filename)
    stacks = load_stacks(stacks_filename)
    for move in moves:
        move_stacks(stacks, move)
    return [stack[0] for stack in stacks]

def run_moves_and_return_top_crates_part_two(moves_filename, stacks_filename):
    moves = load_moves(moves_filename)
    stacks = load_stacks(stacks_filename)
    for move in moves:
        move_stacks_part_two(stacks, move)
    return [stack[0] for stack in stacks]


if __name__ == '__main__':
    print(''.join(run_moves_and_return_top_crates('input/day_5_input_moves.txt','input/day_5_input_stacks.txt')))
    print(''.join(run_moves_and_return_top_crates_part_two('input/day_5_input_moves.txt','input/day_5_input_stacks.txt')))