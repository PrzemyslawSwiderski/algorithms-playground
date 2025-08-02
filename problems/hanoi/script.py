#!/bin/python3
from collections import deque


# https://www.hackerrank.com/challenges/gena/problem?isFullScreen=true
# Complete the 'hanoi' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY posts as parameter.
#

def no_smaller_disks_on_target(current_disks, target_pole, disk_i):
    while disk_i >= 0:
        disk_i -= 1
        if current_disks[disk_i] == target_pole:
            return False

    return True


def hanoi(disks_arr):
    to_process = deque()
    visited = set()

    to_process.append({"data": disks_arr, "steps": 0})
    visited.add(hashable(disks_arr))

    while True:
        current = to_process.popleft()
        current_disks = current["data"]

        if is_solved(current_disks):
            return current["steps"]

        max_non_set_idx = find_max_idx(current_disks)
        for disk_i in range(max_non_set_idx + 1):
            current_pole = current_disks[disk_i]
            for target_pole in range(1, 5):
                if target_pole != current_pole and not_blocked(current_disks, current_pole, target_pole, disk_i):
                    to_add = current_disks.copy()
                    to_add[disk_i] = target_pole
                    to_add_hash = hashable(to_add)
                    if to_add_hash not in visited:
                        visited.add(to_add_hash)
                        to_process.append({"data": to_add, "steps": current["steps"] + 1})


def find_max_idx(disks):
    disk_idx = len(disks) - 1
    while disk_idx >= 0 and disks[disk_idx] == 1:
        disk_idx -= 1
    return disk_idx


def not_blocked(current_disks, current_pole, target_pole, disk_i):
    while disk_i > 0:
        disk_i -= 1
        if (current_disks[disk_i] == current_pole  # other does not block disk at the same pole
                or current_disks[disk_i] == target_pole  # there is no smaller disk on target
        ):
            return False

    return True


def is_solved(disks):
    return all(x == 1 for x in disks)


def hashable(input_obj):
    return str(input_obj)


if __name__ == '__main__':
    # loc = [1, 4, 1]  # expected 3
    loc = [1, 3, 3]  # expected 5

    res = hanoi(loc)

    print(res)
