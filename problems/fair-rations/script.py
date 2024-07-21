#!/bin/python3

import os


#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#
# https://www.hackerrank.com/challenges/fair-rations/problem
#

def is_even(num):
    return num % 2 == 0


def fair_rations(B):
    arr_size = len(B)
    loafs = 0
    for i in range(arr_size):
        if not is_even(B[i]):
            if i + 1 < arr_size:
                B[i] = B[i] + 1
                B[i + 1] = B[i + 1] + 1
                loafs = loafs + 2
            else:
                return 'NO'

    return str(loafs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fair_rations(B)

    fptr.write(result + '\n')

    fptr.close()
