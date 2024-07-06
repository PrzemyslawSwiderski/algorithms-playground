#!/bin/python3

import os


# https://www.hackerrank.com/challenges/chocolate-feast/problem
#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n money
#  2. INTEGER c cost
#  3. INTEGER m wrappers he can turn in
#

def chocolateFeast(n, c, m):
    bars_count = 0
    wrapper_count = 0

    while n - c >= 0:
        bars_count = bars_count + 1
        n = n - c
        wrapper_count = wrapper_count + 1
        if wrapper_count >= m:
            n = n + c
            wrapper_count = 0

    return bars_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
