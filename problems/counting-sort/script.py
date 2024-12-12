#!/bin/python3

import os


#
# Complete the 'counting_sort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def counting_sort(input_arr):
    freqs = [0] * len(input_arr)

    for num in input_arr:
        freqs[num] += 1

    return freqs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = counting_sort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
