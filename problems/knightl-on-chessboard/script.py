#!/bin/python3

from collections import deque


# https://www.hackerrank.com/challenges/knightl-on-chessboard/problem?isFullScreen=true
#
# Complete the 'knightl_on_a_chessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#
#   INPUT: 13
#   EXPECTED_OUT:
# 12 8 6 8 4 4 8 12 6 20 2 24
# 8 6 6 4 10 4 12 8 12 2 12 12
# 6 6 4 8 6 4 8 8 2 8 8 8
# 8 4 8 3 8 4 12 2 36 16 -1 3
# 4 10 6 8 -1 4 2 -1 -1 -1 -1 -1
# 4 4 4 4 4 2 4 4 4 4 4 4
# 8 12 8 12 2 4 -1 -1 -1 -1 -1 -1
# 12 8 8 2 -1 4 -1 -1 -1 -1 -1 -1
# 6 12 2 36 -1 4 -1 -1 -1 -1 -1 -1
# 20 2 8 16 -1 4 -1 -1 -1 -1 -1 -1
# 2 12 8 -1 -1 4 -1 -1 -1 -1 -1 -1
# 24 12 8 3 -1 4 -1 -1 -1 -1 -1 1
#

def knightl_on_a_chessboard(n):
    result = []
    for i in range(0, n - 1):
        r = []
        for j in range(0, n - 1):
            r.append(0)
        result.append(r)

    for a in range(1, n):
        for b in range(1, n):
            a_idx = a - 1
            b_idx = b - 1
            if result[b_idx][a_idx]:
                min_steps = result[b_idx][a_idx]
            else:
                min_steps = bfs(n, a, b)
            result[a_idx][b_idx] = min_steps

    return result


def bfs(n, a, b):
    directions = [
        (a, b),
        (a, -b),
        (-a, b),
        (-a, -b),
        (b, a),
        (b, -a),
        (-b, a),
        (-b, -a),
    ]
    visited = {(0, 0)}
    to_check = deque([(0, 0, 0)])

    while to_check:
        current = to_check.popleft()
        if current[0] == n - 1 and current[1] == n - 1:
            return current[2]

        for dx, dy in directions:
            new_x = current[0] + dx
            new_y = current[1] + dy
            new_pos = (new_x, new_y)
            if 0 <= new_x < n and 0 <= new_y < n and new_pos not in visited:
                new_step = current[2] + 1
                to_check.append((new_x, new_y, new_step))
                visited.add((current[0], current[1]))

    return -1


if __name__ == '__main__':

    size = 13
    res = knightl_on_a_chessboard(size)
    for i in res:
        print(i)
