import pytest
from day_3 import read_backpacks_split, get_common_item_type, score_common_item_type, sum_common_items,sum_badge_labels

backpacks = read_backpacks_split('input/day_3_test_input.txt')

def test_backpack_1_split_correctly():
    assert backpacks[0] == ('vJrwpWtwJgWr','hcsFMMfFFhFp')

def test_backpack_6_split_correctly():
    assert backpacks[5] == ('CrZsJsPPZsGz','wwsLwLmpwMDw')

def test_get_common_item_type():
    assert get_common_item_type(backpacks[0]) == 'p'
    assert get_common_item_type(backpacks[2]) == 'P'

def test_score_common_item_type():
    assert score_common_item_type('b') == 2
    assert score_common_item_type('L') == 38

def test_sum_common_items():
    assert sum_common_items('input/day_3_test_input.txt') == 157

def test_badge_labels_summed_correctly():
    assert sum_badge_labels('input/day_3_test_input.txt') == 70