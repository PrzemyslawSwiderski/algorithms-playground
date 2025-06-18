#!/bin/python3

import os


#
# https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecream_parlor(m, arr):
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] + arr[j] == m:
                return [i + 1, j + 1]
            j += 1
        i += 1
    return None


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecream_parlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
