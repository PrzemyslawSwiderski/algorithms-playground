#!/bin/python3

import os


# https://www.hackerrank.com/challenges/luck-balance/problem
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#
def luck_balance(k, contests):
    important = []
    lost = []
    for l, t in contests:
        # print(f"{l} {t}")
        if t == 1:
            important.append(l)
        else:
            lost.append(l)

    important.sort(reverse=True)

    i = 0
    while i < k and i < len(important):
        lost.append(important[i])
        important[i] = 0
        i += 1

    min_luck = sum(lost) - sum(important)

    return min_luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luck_balance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
