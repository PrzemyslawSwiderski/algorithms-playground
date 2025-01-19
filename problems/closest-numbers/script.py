#!/bin/python3

import os
import sys


# https://www.hackerrank.com/challenges/closest-numbers/problem
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closest_numbers(arr):
    output_arr = []
    arr.sort()

    min_val = sys.maxsize
    i = 0
    while i < (len(arr) - 1):
        diff = abs(arr[i + 1] - arr[i])
        if diff < min_val:
            min_val = diff
        i += 1

    i = 0
    while i < (len(arr) - 1):
        diff = abs(arr[i + 1] - arr[i])
        if diff == min_val:
            output_arr.append(arr[i])
            output_arr.append(arr[i + 1])
        i += 1
    return output_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closest_numbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
