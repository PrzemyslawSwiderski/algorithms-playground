#!/bin/python3

import os


# https://www.hackerrank.com/challenges/grid-challenge/problem?isFullScreen=true
# Complete the 'grid_challenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def grid_challenge(grid):
    print(grid)
    output_grid = []
    for row in grid:
        sorted_row = sorted(list(row))
        output_grid.append(sorted_row)

    for i in range(1, len(output_grid)):
        for j in range(len(output_grid[i])):
            if output_grid[i][j] < output_grid[i - 1][j]:
                return 'NO'

    print(output_grid)
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = grid_challenge(grid)

        fptr.write(result + '\n')

    fptr.close()
