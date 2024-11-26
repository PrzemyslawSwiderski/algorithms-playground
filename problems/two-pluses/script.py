#!/bin/python3

import os


#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def valid_plus(max_len, grid, x, y):
    margin = max_len // 2
    i = margin

    while i < x - margin:
        j = margin
        while j < y - margin:
            k = 0
            good = True
            while k <= margin:
                if grid[i + k][j] != 'G':
                    good = False
                if grid[i][j + k] != 'G':
                    good = False
                if grid[i - k][j] != 'G':
                    good = False
                if grid[i][j - k] != 'G':
                    good = False
                k += 1
            if good:
                k = 0
                while k <= margin:
                    grid[i + k][j] = 'B'
                    grid[i][j + k] = 'B'
                    grid[i - k][j] = 'B'
                    grid[i][j - k] = 'B'
                    k += 1
                return True
            j += 1
        i += 1

    return False


def two_pluses(grid):
    # Write your code here
    plus_prod = 1
    x = len(grid)
    y = len(grid[0])
    max_len = min(x, y)
    if max_len % 2 == 0:
        max_len -= 1

    counter = 2

    while max_len >= 1 and counter>0:
        res = valid_plus(max_len, grid, x, y)
        if res:
            counter-=1
            plus_prod*=(2*max_len - 1)
        else:
            max_len-=2

    return plus_prod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(list(grid_item))

    result = two_pluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
