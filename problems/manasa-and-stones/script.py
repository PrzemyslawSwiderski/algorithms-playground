#!/bin/python3

import os


#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#
# https://www.hackerrank.com/challenges/manasa-and-stones/problem
#


def stones(n, a, b):
    if a == b:
        return [a * (n - 1)]

    last_stones = [a * i + b * (n - 1 - i) for i in range(n)]

    return sorted(last_stones)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
