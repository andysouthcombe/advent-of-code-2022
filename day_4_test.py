import pytest
from day_4 import read_assignments, expand_assignment_range, do_assignments_fully_overlap, count_fully_overlapping_ranges, do_assignments_overlap_at_all

test_assignments = read_assignments('input/day_4_test_input.txt')

def test_file_read_ok():
    assert test_assignments[0] == ['2-4','6-8']
    assert test_assignments[5] == ['2-6','4-8']

def test_single_digit_range_expanded_ok():
    assert expand_assignment_range(['2-4','6-8']) == [[2,3,4],[6,7,8]]

def test_two_digit_range_expanded_ok():
    assert expand_assignment_range(['2-4','6-10']) == [[2,3,4],[6,7,8,9,10]]

def test_non_overlapping_range_returns_false():
    assert do_assignments_fully_overlap([[2,3,4],[6,7,8]]) == False

def test_fully_overlapping_range_returns_true():
    assert do_assignments_fully_overlap([[7,8],[6,7,8,9,10]]) == True

def test_count_fully_overlapping_assignments():
    assert count_fully_overlapping_ranges(test_assignments) == 2

def test_assignment_no_overlap_at_all():
    assert do_assignments_overlap_at_all([[2,3,4],[6,7,8]]) == False

def test_assignment_some_overlap():
    assert do_assignments_overlap_at_all([[2,3,4],[4,5,6]]) == True