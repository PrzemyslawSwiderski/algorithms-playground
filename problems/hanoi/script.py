#!/bin/python3
from collections import deque
from copy import deepcopy


# https://www.hackerrank.com/challenges/gena/problem?isFullScreen=true
# Complete the 'hanoi' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY posts as parameter.
#

def hanoi(posts):
    disks_count = len(posts)
    to_process = deque()
    visited = set()

    disks_by_pole = disk_map(posts)

    init_poles = deepcopy(disks_by_pole)
    to_process.append({"data": init_poles, "steps": 0})
    visited.add(hashable(init_poles))
    # print(disks_by_pole)

    while True:
        current = to_process.popleft()
        current_data = current["data"]

        if is_solved(current_data, disks_count):
            return current["steps"]
        for i in range(1, 5):
            for j in range(1, 5):
                if j != i and current_data[i]:
                    if (current_data[j] and current_data[j][0] > current_data[i][0]) or not current_data[j]:
                        to_add = deepcopy(current_data)
                        to_move = to_add[i].popleft()
                        to_add[j].appendleft(to_move)
                        to_add_hash = hashable(to_add)
                        if to_add_hash not in visited:
                            visited.add(to_add_hash)
                            to_process.append({"data": to_add, "steps": current["steps"] + 1})


def disk_map(arr):
    disks = {}
    for i in range(1, 5):
        disks[i] = deque()
    for idx, e in enumerate(arr):
        disk_num = idx + 1
        disks[e].append(disk_num)
    return disks


def is_solved(disks, disks_count):
    if len(disks[1]) == disks_count:
        return True
    else:
        return False


def hashable(input_dict):
    output = ()
    for it in input_dict.items():
        output += (it[0], tuple(it[1]),)
    return output


if __name__ == '__main__':
    # loc = [1, 4, 1] # expected 3
    loc = [1, 3, 3]  # expected 5

    res = hanoi(loc)

    print(res)
