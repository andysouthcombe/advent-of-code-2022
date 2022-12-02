import pytest
from day_2 import did_player_win, read_inputs, get_player_score, get_total_score

def test_paper_beats_rock():
    assert did_player_win('Rock', 'Paper') == True

def test_rock_beats_scissors():
    assert did_player_win('Scissors', 'Rock') == True

def test_scissors_beats_paper():
    assert did_player_win('Paper', 'Scissors') == True

def test_paper_loses_to_scissors():
    assert did_player_win('Scissors', 'Paper') == False

def test_scissors_loses_to_rock():
    assert did_player_win('Rock', 'Scissors') == False

def test_rock_loses_to_paper():
    assert did_player_win('Paper', 'Rock') == False

def test_file_read_ok():
    assert read_inputs('input/day_2_test_input.txt') == [('A', 'Y'), ('B', 'X'), ('C', 'Z')]

def test_first_round_scored_ok():
    assert get_player_score(('A', 'Y')) == 8

def test_second_round_scored_ok():
    assert get_player_score(('B', 'X')) == 1

def test_third_round_scored_ok():
    assert get_player_score(('C', 'Z')) == 6

def test_total_score_correct():
    assert get_total_score('input/day_2_test_input.txt') == 15