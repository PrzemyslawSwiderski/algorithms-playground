#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    length = len(arr)
    sorted_arr = sorted(arr, reverse=True)
    if k > length:
        return sorted_arr

    values_idx = {}

    for i, num in enumerate(arr):
        values_idx[num] = i

    swaps = 0
    i = 0
    while True:
        if i>= length - 1:
            break
        if swaps>=k:
            break

        next_max  = sorted_arr[i]
        if arr[i] != next_max:

            #print(f"swapping {next_max=} with idx {i=}")
            max_idx = values_idx[next_max]
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
            values_idx[arr[max_idx]] = max_idx
            swaps+=1
        i+=1

    print(arr[:10])
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
