from aoc_utils import read_file_of_strings_into_one_string

def find_position_of_n_different_characters(input_string, n):
    for c in range(n-1,len(input_string)):
        if len(set(input_string[c-(n-1):c+1])) == n:
            return c+1
    return -1

if __name__ == '__main__':
    print(find_position_of_n_different_characters(read_file_of_strings_into_one_string('input/day_6_input.txt'),4))
    print(find_position_of_n_different_characters(read_file_of_strings_into_one_string('input/day_6_input.txt'),14))