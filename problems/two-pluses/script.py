#!/bin/python3

import os
from itertools import product, combinations


#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def find_max_product(all_pluses):
    max_prod = 0
    for i in combinations(all_pluses, 2):
        plus_1 = i[0]
        plus_2 = i[1]
        # check if the pluses are not overlapping each other
        if not plus_1.intersection(plus_2):
            prod = len(plus_1) * len(plus_2)
            max_prod = max(max_prod, prod)
    return max_prod


def two_pluses(grid):
    all_pluses = []
    # iterate through the grid
    for i, j in product(range(len(grid)), range(len(grid[0]))):
        if grid[i][j] == 'G':
            temp_pluses = set()
            plus_max_length = len(grid) // 2
            for k in range(0, plus_max_length + 1):
                # check if plus is within the grid
                if j - k < 0 or j + k > len(grid[0]) - 1 or i - k < 0 or i + k > len(grid) - 1:
                    break
                # check if plus expanding is doable in all directions
                if grid[i][j - k] == grid[i][j + k] == grid[i - k][j] == grid[i + k][j] == 'G':
                    # update set with the union
                    temp_pluses.update(((i, j - k), (i, j + k,), (i - k, j), (i + k, j)))
                    all_pluses.append(temp_pluses.copy())
                else:
                    break

    max_prod = find_max_product(all_pluses)

    return max_prod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = two_pluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
