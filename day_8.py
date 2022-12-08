from aoc_utils import read_file_of_strings

def load_grid(filename):
    raw_grid = read_file_of_strings(filename)
    ints_grid = []
    for line in raw_grid:
        line_ints = [int(tree)  for tree in line]
        ints_grid.append(line_ints)
    return ints_grid

def get_trees_above_and_below(x,y,grid):
    return [grid[y_coord][x] for y_coord in range(0,y)], [grid[y_coord][x] for y_coord in range(y+1,len(grid))]


def get_coords_of_visible_trees(grid):
    output_coords = []
    grid_y_size = len(grid) - 1
    grid_x_size = len(grid[0]) - 1
    for y, line in enumerate(grid):
        for x, tree in enumerate(line):
            if x in [0,grid_x_size] or y in [0,grid_y_size]:
                output_coords.append((x,y))
            else:
                highest_tree_to_left = max(line[:x])
                highest_tree_to_right = max(line[x+1:])
                trees_above, trees_below = get_trees_above_and_below(x,y,grid)
                highest_tree_above = max(trees_above)
                highest_tree_below = max(trees_below)
                if tree > highest_tree_to_left or tree > highest_tree_to_right or tree > highest_tree_above or tree > highest_tree_below:
                    output_coords.append((x, y))
    return output_coords

if __name__ == '__main__':
    part_1_grid = load_grid('input/day_8_input.txt')
    print(len(set(get_coords_of_visible_trees(part_1_grid))))