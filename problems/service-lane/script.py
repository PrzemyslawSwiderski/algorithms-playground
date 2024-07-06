#!/bin/python3

import os


# https://www.hackerrank.com/challenges/service-lane/problem
#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(width, cases):
    outputs = []

    print(width)

    for case in cases:
        min = 3
        startIdx = case[0]
        endIdx = case[1]
        while startIdx <= endIdx:
            if width[startIdx] < min:
                min = width[startIdx]
            startIdx = startIdx + 1
        outputs.append(min)

    return outputs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
