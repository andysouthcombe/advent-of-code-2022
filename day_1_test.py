import pytest
from aoc_utils import read_file_of_strings
from day_1 import sum_each_elf, get_elf_with_most_calories, get_calories_top_three_elves

def test_file_read_ok():
    assert len(read_file_of_strings('input/day_1_test_input.txt')) == 14

def test_first_elf_summed_ok():
    assert sum_each_elf('input/day_1_test_input.txt')[0] == 6000

def test_last_elf_summed_ok():
    assert sum_each_elf('input/day_1_test_input.txt')[4] == 10000

def test_return_elf_with_most_calories():
    assert get_elf_with_most_calories('input/day_1_test_input.txt') == 24000

def test_return_calories_for_top_three_elves():
    assert get_calories_top_three_elves('input/day_1_test_input.txt') == 45000