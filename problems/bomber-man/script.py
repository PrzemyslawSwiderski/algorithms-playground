#!/bin/python3

import os


#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def _to_strings(grid):
    res = []
    for s in grid:
        res.append(''.join(['.' if x <= 0 else 'O' for x in s]))
    return res


def _detonate(grid, i, j):
    grid[i][j] = 0
    if i > 0 and grid[i - 1][j] != 1:
        grid[i - 1][j] = 0
    if j > 0 and grid[i][j - 1] != 1:
        grid[i][j - 1] = 0
    if i < len(grid) - 1 and grid[i + 1][j] != 1:
        grid[i + 1][j] = 0
    if j < len(grid[0]) - 1 and grid[i][j + 1] != 1:
        grid[i][j + 1] = 0


def _plant(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] <= 0:
                grid[i][j] = 3


def _next_tick(grid, tick):
    if tick == 2:
        return
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 1:
                grid[i][j] -= 1
    if tick == 1 or tick % 2 == 0 and tick != 2:
        _plant(grid)
        return

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                _detonate(grid, i, j)


def _to_grid(grid):
    res = []
    for s in grid:
        res.append([0 if x == '.' else 3 for x in s])
    return res


def bomber_man(n, grid):
    if n % 2 == 0:
        return ['O' * len(grid[0])] * len(grid)
    grid = _to_grid(grid)
    if n == 1:
        return _to_strings(grid)
    for i in range(1, min(8, 4 + n % 4 + 1)):
        _next_tick(grid, i)
    return _to_strings(grid)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomber_man(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
