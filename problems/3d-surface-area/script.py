#!/bin/python3

import os


#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#
# https://www.hackerrank.com/challenges/3d-surface-area/problem
def surface_area(A):
    transposed_A = [list(row) for row in zip(*A)]
    down_up = 2 * H * W
    init_left_right = sum(A[0]) + sum(A[H - 1])
    init_front_back = sum(transposed_A[0]) + sum(transposed_A[W - 1])
    total_area = down_up + init_left_right + init_front_back
    for h in range(H):
        for w in range(W):
            current_block = A[h][w]
            if w != W - 1:
                # resolve additional front / back surfaces
                next_block = A[h][w + 1]
                total_area += abs(next_block - current_block)
            if h != H - 1:
                # resolve additional side surfaces
                next_block = A[h + 1][w]
                total_area += abs(next_block - current_block)
    return total_area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surface_area(A)

    fptr.write(str(result) + '\n')

    fptr.close()
