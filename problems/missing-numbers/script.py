#!/bin/python3

import os


#
# Complete the 'missing_numbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts the following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missing_numbers(arr, brr):
    # Write your code here
    idx = {}

    for i in brr:
        if i in idx:
            idx[i] += 1
        else:
            idx[i] = 1

    for j in arr:
        if j in idx:
            idx[j] -= 1

    print(idx)
    out = []
    for (k, v) in idx.items():
        print(f"{k=} {v=}")
        if v > 0:
            out.append(k)

    return sorted(out)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missing_numbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
