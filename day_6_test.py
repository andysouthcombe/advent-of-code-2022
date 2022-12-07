import pytest
from day_6 import find_position_of_n_different_characters

test_string_1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
test_string_2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

def test_first_test_string_returns_7():
    assert find_position_of_n_different_characters(test_string_1,4) == 7

def test_second_test_string_returns_5():
    assert find_position_of_n_different_characters(test_string_1,4) == 7