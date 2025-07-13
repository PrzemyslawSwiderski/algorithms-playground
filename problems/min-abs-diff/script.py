#!/bin/python3

import os


#
# Complete the 'minimum_absolute_difference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimum_absolute_difference(arr):
    min_diff = 2 * pow(10, 9)
    # print(min_diff)
    arr = sorted(arr)
    # print(arr)

    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i - 1])
        if diff < min_diff:
            min_diff = diff

    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimum_absolute_difference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
