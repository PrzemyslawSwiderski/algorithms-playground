#!/bin/python3

import os


#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#
# https://www.hackerrank.com/challenges/the-grid-search/problem
#

def grid_search(G, P):
    for g_i in range(len(G) - len(P) + 1):
        for g_j in range(len(G[0]) - len(P[0]) + 1):

            pattern_matches = check_pattern(G, P, g_i, g_j)

            if pattern_matches is True:
                return 'YES'

    return 'NO'


def check_pattern(G, P, g_i, g_j):
    size_p = len(P)
    for p_i in range(size_p):
        for p_j in range(len(P[p_i])):
            if G[g_i + p_i][g_j + p_j] != P[p_i][p_j]:
                return False
    return True


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = grid_search(G, P)

        fptr.write(result + '\n')

    fptr.close()
