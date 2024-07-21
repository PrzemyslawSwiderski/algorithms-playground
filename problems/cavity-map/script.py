#!/bin/python3

import os


#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#
# https://www.hackerrank.com/challenges/cavity-map/problem
#

def cavity_map(grid):
    size = len(grid)
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            if (grid[i - 1][j] < grid[i][j]
                    and grid[i + 1][j] < grid[i][j]
                    and grid[i][j + 1] < grid[i][j]
                    and grid[i][j - 1] < grid[i][j]):
                grid[i][j] = 'X'
    return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = list()

    for _ in range(n):
        grid_item = list(input())
        grid.append(grid_item)

    result = cavity_map(grid)

    for i in range(n):
        for j in range(n):
            fptr.write(result[i][j])
        fptr.write('\n')

    fptr.close()
