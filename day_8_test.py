import pytest

from day_8 import get_coords_of_visible_trees, get_trees_above_and_below, load_grid

simple_input_grid = [[0,1],
                     [0,1]]

simple_input_grid_with_one_hidden_tree = [[1,1,1],
                                          [1,0,1],
                                          [1,1,1]]

simple_input_grid_with_no_hidden_trees = [[1,1,1],
                                          [1,2,1],
                                          [1,1,1]]

test_grid = load_grid('input/day_8_test_input.txt')

def test_get_coord_of_visible_trees_4x4_grid():
    assert get_coords_of_visible_trees(simple_input_grid) == [(0,0),(1,0),(0,1),(1,1)]

def test_get_trees_above_and_below():
    assert get_trees_above_and_below(1,1,simple_input_grid_with_no_hidden_trees) == ([1],[1])

def test_grid_has_21_trees():
    visible_trees = get_coords_of_visible_trees(test_grid)
    print(visible_trees)
    assert len(visible_trees) == 21

def test_get_trees_above_and_below():
    print(test_grid)
    assert get_trees_above_and_below(2,1,test_grid) == ([3],[3,5,3])