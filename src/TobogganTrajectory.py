# Day 3: Toboggan Trajectory

"""
Takes a filepath (default = my path) and generates a 2D array of the environment

...#
.#..
#...

Becomes
[[., ., ., #],
 [., #, ., .],
 [#, ., ., .]]
"""


def get_env(filepath="../assets/trees.txt"):
    env = []

    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            env.append(list(line))

    return env


# Counts the number of trees in a given slope using tuple locations (dx, dy) and (x,y)
def count_trees(env, slope: tuple, location=(0, 0)):
    # Get dimensions of the environment
    height = len(env) - 1
    width = len(env[0]) - 1
    num_trees = 0

    # Since the x direction repeats infinitely, loop until the toboggan reaches the end of the y direction
    while location[1] < height:

        # Calculate the new coordinates after the toboggan moves, looping x if needed using x mod(height)
        location = ((location[0] + slope[0]) % width, location[1] + slope[1])

        # Check for a tree and count if necessary
        if env[location[1]][location[0]] == '#':
            num_trees += 1

    return num_trees


# Automates the process for checking multiple slopes starting at a single location, taking a list of tuple slopes
def check_slopes(slopes, location=(0, 0)):
    slope_product = 1
    env = get_env()

    # This code could easily be modified to give other, more interesting info than just the product of the trees :)
    for slope in slopes:
        slope_product *= count_trees(env, slope, location)

    return slope_product


candidate_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(f'Part1: {check_slopes([(3, 1)])} \nPart2: {check_slopes(candidate_slopes)}')
