import pytest
from day_5 import load_stacks, load_moves, move_stacks, run_moves_and_return_top_crates, move_stacks_part_two

def test_starting_stacks_read_correctly():
    assert load_stacks('input/day_5_test_input_stacks.txt') == [['N', 'Z'], ['D', 'C', 'M'], ['P']]

def test_moves_read_correctly():
    assert load_moves('input/day_5_test_input_moves.txt')[0] == [1,2,1]

def test_first_move_of_single_crate_works():
    starting_stacks=[['N', 'Z'], ['D', 'C', 'M'], ['P']]
    first_move = [1,2,1]
    expected_stacks = [['D','N', 'Z'], ['C', 'M'], ['P']]
    assert move_stacks(starting_stacks, first_move) == expected_stacks
    
def test_second_move_of_three_crates_works():
    starting_stacks=[['D','N', 'Z'], ['C', 'M'], ['P']]
    first_move = [3,1,3]
    expected_stacks = [[], ['C', 'M'], ['Z','N', 'D','P']]
    assert move_stacks(starting_stacks, first_move) == expected_stacks

def test_run_moves_and_return_top_crates_works_for_test_input():
    assert run_moves_and_return_top_crates('input/day_5_test_input_moves.txt','input/day_5_test_input_stacks.txt') == ['C','M','Z']

def test_first_move_of_single_crate_works_part_2():
    starting_stacks=[['N', 'Z'], ['D', 'C', 'M'], ['P']]
    first_move = [1,2,1]
    expected_stacks = [['D','N', 'Z'], ['C', 'M'], ['P']]
    assert move_stacks_part_two(starting_stacks, first_move) == expected_stacks

def test_second_move_of_single_crate_works_part_2():
    starting_stacks=[['D','N', 'Z'], ['C', 'M'], ['P']]
    first_move = [3,1,3]
    expected_stacks = [[], ['C', 'M'], ['D','N', 'Z', 'P']]
    assert move_stacks_part_two(starting_stacks, first_move) == expected_stacks