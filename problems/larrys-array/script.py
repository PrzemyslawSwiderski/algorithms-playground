#!/bin/python3

import os


#
# https://www.hackerrank.com/challenges/larrys-array/problem
# Complete the 'larrys-array' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#
def larrys_array(A):
    # Write your code here

    sorted_A = sorted(A)

    result = can_be_sorted(sorted_A, A, 0, 3)

    if result:
        return "YES"
    else:
        return "NO"


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
