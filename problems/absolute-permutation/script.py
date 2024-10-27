#!/bin/python3

import os


#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#
# https://www.hackerrank.com/challenges/absolute-permutation/problem
def absolute_permutation(n, k):
    answer = []
    visited = set()
    for v in range(1, n + 1):
        d1, d2 = v - k, v + k
        if d1 > 0 and d1 not in visited:
            answer.append(d1)
            visited.add(d1)
        elif d2 <= n and d2 not in visited:
            answer.append(d2)
            visited.add(d2)
        else:
            return [-1]
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolute_permutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
