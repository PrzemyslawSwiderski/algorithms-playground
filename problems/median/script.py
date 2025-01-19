#!/bin/python3

import os


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def find_median(arr):
    arr.sort()
    return arr[int(len(arr) / 2)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = find_median(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
