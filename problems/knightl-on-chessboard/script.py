#!/bin/python3

from collections import deque


# https://www.hackerrank.com/challenges/knightl-on-chessboard/problem?isFullScreen=true
#
# Complete the 'knightl_on_a_chessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def knightl_on_a_chessboard(n):
    result = []
    for i in range(1, n):
        row = []
        for j in range(1, n):
            row.append(bfs(n, i, j))
        result.append(row)

    return result


def bfs(n, a, b):
    directions = [(a, b), (a, -b), (-a, b), (-a, -b),
                  (b, a), (b, -a), (-b, a), (-b, -a)]
    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}

    while queue:
        x, y, dist = queue.popleft()
        if x == n - 1 and y == n - 1:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    return -1


if __name__ == '__main__':

    size = 5
    res = knightl_on_a_chessboard(size)
    for i in res:
        print(i)
