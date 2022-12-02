from aoc_utils import read_file_of_strings
opponent = {
            'A': 'Rock',
            'B': 'Paper',
            'C': 'Scissors'
    }

player = {
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

player_result_part2 = {
    'X': 'Lose',
    'Y': 'Draw',
    'Z': 'Win'
}

scores = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

beats = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}

loses = dict((value,key) for key,value in beats.items())

def did_player_win(opponent_move, player_move):
    return beats[player_move]== opponent_move

def read_inputs(filename):
    return [tuple(line.split(' ')) for line in read_file_of_strings(filename)]

def get_player_score(round):
    opponent_move, player_move = opponent[round[0]], player[round[1]]
    score = 0
    if opponent_move == player_move:
        score += 3
    if did_player_win(opponent_move, player_move):
        score += 6
    return score + scores[player_move]

def get_total_score_part1(filename):
    rounds = read_inputs(filename)
    return sum([get_player_score(round) for round in rounds])

def get_player_move_required(round):
    opponent_move, player_result = opponent[round[0]], player_result_part2[round[1]]
    if player_result == 'Draw':
        return opponent_move

if __name__ == '__main__':
    print(get_total_score_part1('input/day_2_input.txt'))