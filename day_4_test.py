import pytest
from day_4 import read_assignments  

test_assignments = read_assignments('input/day_4_test_input.txt')

def test_file_read_ok():
    assert test_assignments[0] == ['2-4','6-8']
    assert test_assignments[5] == ['2-6','4-8']
