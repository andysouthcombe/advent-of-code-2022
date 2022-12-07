from aoc_utils import read_file_of_strings

def build_tree(filename):
    input = read_file_of_strings(filename)
    row_limit = len(input) -1
    directories = {}
    dir_tree = []
    for row, line in enumerate(input):
        if line == '$ ls':
            directory = input[row-1].split(' ')[2]
            dir_tree.append(directory)
            directory_contents = []
            while row < row_limit and input[row+1][2:4] != 'cd':
                scan_ahead_line = input[row+1]
                if scan_ahead_line[0:3] != 'dir':
                    filesize = int(scan_ahead_line.split(' ')[0])
                    directory_contents.append(filesize)
                row += 1
            directories[','.join(dir_tree)] = sum(directory_contents)
        if line == '$ cd ..':
            dir_tree.pop()
    return directories

def get_total_size_inc_subfolders(tree):
    dict_size = len(tree)
    tree_as_list = list(tree.items())
    output_dict = {}
    for index,dir_pair in enumerate(tree_as_list):
        dir = dir_pair[0]
        filesize = dir_pair[1]
        look_ahead_index = index + 1
        while look_ahead_index < dict_size:
            if dir in tree_as_list[look_ahead_index][0]:
                filesize += tree_as_list[look_ahead_index][1]
            look_ahead_index += 1
        output_dict[dir] = filesize
    return output_dict
            
def sum_totals_over_limit(folders,limit):
    return sum(filter(lambda size: (size <= limit), [size for size in folders.values()]))

def find_smallest_dir_to_delete(folders):
    sizes = list(folders.values())
    root_folder_size = sizes[0]
    total_space = 70000000
    required_free_space = 30000000
    current_free_space = total_space - root_folder_size
    folders_that_meet_criteria = []
    for size in sizes:
        if current_free_space + size >= required_free_space:
            folders_that_meet_criteria.append(size)
    return min(folders_that_meet_criteria)

        


if __name__ == '__main__':
    tree = build_tree('input/day_7_test_input.txt')
    totalled_size = get_total_size_inc_subfolders(tree)
    print(list(tree.items()))
    print(totalled_size)
    print(sum_totals_over_limit(totalled_size,100000))
    print(find_smallest_dir_to_delete(totalled_size))
    tree = build_tree('input/day_7_input.txt')
    totalled_size = get_total_size_inc_subfolders(tree)
    print(list(tree.items()))
    print(totalled_size)
    print(sum_totals_over_limit(totalled_size,100000))
    print(find_smallest_dir_to_delete(totalled_size))