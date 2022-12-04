from aoc_utils import read_file_of_strings

def read_assignments(filename):
    return [assignments.split(',') for assignments in read_file_of_strings(filename)]

def expand_assignment_range(assignments):
    range_one_text = assignments[0].split('-')
    range_two_text = assignments[1].split('-')
    range_one_int = [int(range_one) for range_one in range_one_text]
    range_two_int = [int(range_one) for range_one in range_two_text]
    return [list(range(range_one_int[0],range_one_int[1]+1)),list(range(range_two_int[0],range_two_int[1]+1))]

def do_assignments_fully_overlap(assignments):
    return set(assignments[0]).issuperset(set(assignments[1])) or set(assignments[1]).issuperset(set(assignments[0]))

def do_assignments_overlap_at_all(assignments):
    return len(set(assignments[0]).intersection(set(assignments[1]))) > 0

def count_fully_overlapping_ranges(assignments):
    assignment_ranges = [expand_assignment_range(assignment) for assignment in assignments]
    return sum([int(do_assignments_fully_overlap(ass_range)) for ass_range in assignment_ranges])

def count_any_overlapping_ranges(assignments):
    assignment_ranges = [expand_assignment_range(assignment) for assignment in assignments]
    return sum([int(do_assignments_overlap_at_all(ass_range)) for ass_range in assignment_ranges])

if __name__ == '__main__':
    print(count_fully_overlapping_ranges(read_assignments('input/day_4_input.txt')))
    print(count_any_overlapping_ranges(read_assignments('input/day_4_input.txt')))