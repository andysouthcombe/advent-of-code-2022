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

def get_total_score(filename):
    rounds = read_inputs(filename)
    return sum([get_player_score(round) for round in rounds])

if __name__ == '__main__':
    print(get_total_score('input/day_2_input.txt'))