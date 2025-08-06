#!/bin/python3

from collections import deque


#
# Complete the 'printShortestPath' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start
#  4. INTEGER i_end
#  5. INTEGER j_end
#

def is_on_board(left_i, left_j, max_size):
    if 0 <= left_i < max_size and 0 <= left_j < max_size:
        return True
    else:
        return False


def move_knight(to_process, pos, step, dir, n, current):
    pos_i, pos_j = pos
    if is_on_board(pos_i, pos_j, n):
        to_process.append([pos_i, pos_j, step + 1, dir, current])


def print_shortest_path(n, i_start, j_start, i_end, j_end):
    to_process = deque()
    visited = set()
    to_process.appendleft([i_start, j_start, 0, None, None])

    while to_process:
        current = to_process.popleft()
        current_i, current_j, step, direction, prev_ref = current
        current_pos = (current_i, current_j,)

        if current_pos in visited:
            continue

        if current_i == i_end and current_j == j_end:
            print(step)
            positions = [current[3]]
            prev_pos = prev_ref
            while prev_pos[3]:
                positions.append(prev_pos[3])
                prev_pos = prev_pos[4]
            for p in reversed(positions):
                print(p, end=" ")
            return
        else:
            visited.add(current_pos)

        up_left_i = current_i - 2
        up_left_j = current_j - 1
        move_knight(to_process, (up_left_i, up_left_j,), step, 'UL', n, current)

        up_right_i = current_i - 2
        up_right_j = current_j + 1
        move_knight(to_process, (up_right_i, up_right_j,), step, 'UR', n, current)

        right_i = current_i
        right_j = current_j + 2
        move_knight(to_process, (right_i, right_j,), step, 'R', n, current)

        low_right_i = current_i + 2
        low_right_j = current_j + 1
        move_knight(to_process, (low_right_i, low_right_j,), step, 'LR', n, current)

        low_left_i = current_i + 2
        low_left_j = current_j - 1
        move_knight(to_process, (low_left_i, low_left_j,), step, 'LL', n, current)

        left_i = current_i
        left_j = current_j - 2
        move_knight(to_process, (left_i, left_j,), step, 'L', n, current)

    print("Impossible")


if __name__ == '__main__':
    n = 7

    i_start = 0

    j_start = 3

    i_end = 4

    j_end = 3

    print_shortest_path(n, i_start, j_start, i_end, j_end)
