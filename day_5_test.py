import pytest
from day_5 import load_stacks, load_moves

def test_starting_stacks_read_correctly():
    assert load_stacks('input/day_5_test_input_stacks.txt') == [['N', 'Z'], ['D', 'C', 'M'], ['P']]

def test_moves_read_correctly():
    assert load_moves('input/day_5_test_input_moves.txt')[0] == [1,2,1]
    