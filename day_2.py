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

player_codes = dict((value,key) for key,value in player.items())


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

loses_to = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}

beats = dict((value,key) for key,value in loses_to.items())

def did_player_win(opponent_move, player_move):
    return opponent_move == loses_to[player_move]

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
    if player_result == 'Lose':
        return loses_to[opponent_move]
    if player_result == 'Win':
        return beats[opponent_move]

def get_total_score_part2(filename):
    rounds = read_inputs(filename)
    moves = [(opponent, player_codes[get_player_move_required((opponent,player_result))])  for opponent, player_result in rounds]
    return sum([get_player_score(move) for move in moves])

if __name__ == '__main__':
    print(get_total_score_part1('input/day_2_input.txt'))
    print(get_total_score_part2('input/day_2_input.txt'))