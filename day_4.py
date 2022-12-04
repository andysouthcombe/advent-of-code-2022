from aoc_utils import read_file_of_strings

def read_assignments(filename):
    return [assignment.split(',') for assignment in read_file_of_strings(filename)]