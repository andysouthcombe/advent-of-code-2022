import pytest
from aoc_utils import read_file_of_strings
from day_1 import sum_each_elf

def test_file_read_ok():
    assert len(read_file_of_strings('day_1_test_input.txt')) == 14

def test_first_elf_summed_ok():
    assert sum_each_elf('day_1_test_input.txt')[0] == (1, 6000)

def test_last_elf_summed_ok():
    assert sum_each_elf('day_1_test_input.txt')[4] == (5, 10000)