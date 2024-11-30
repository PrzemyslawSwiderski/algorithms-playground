#!/bin/python3

import os
from itertools import count


#
# https://www.hackerrank.com/challenges/larrys-array/problem
# Complete the 'larrys-array' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#
def larrys_array(A):

    # Checking if the inversions count is even.
    # Similar to 15 Puzzle Problem -> https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/.
    # An inversion occurs when a given value in an array precedes another value in the array.
    # For instance, in an array of: 3 1 4 5 6 2
    # 1 is preceded by higher value 3, so that's 1 inversion. 3, 4, 5, and 6 each precede the lower value 2, so that's 1 inversion each.
    # For this problem, the array can be solved with the given formula if the total number of inversions is even/divisible by 2.

    count = len([i for i in range(len(A)) for j in range(i + 1, len(A)) if A[i] > A[j]])

    return 'YES' if count % 2 == 0 else 'NO'


def rotate(A, i):
    tmp = A[i]
    A[i] = A[i + 2]
    tmp2 = A[i + 1]
    A[i + 1] = tmp
    A[i + 2] = tmp2


def can_be_sorted(sorted_A, A, i, counter):
    if sorted_A == A:
        return True
    if counter < 0:
        return False
    print(f"i: {i}, counter:{counter}, input: {A}")
    rotate(A, i)
    j = 0
    while j < len(A) - 2:
        res = can_be_sorted(sorted_A, A, j, counter - 1)
        if res:
            return True
        j += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrys_array(A)

        fptr.write(result + '\n')

    fptr.close()
