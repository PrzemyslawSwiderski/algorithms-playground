#!/bin/python3
from collections import deque


# https://www.hackerrank.com/challenges/cut-the-tree/problem
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

def cutTheTree(data, edges):
    min_sum = 100000
    for e in edges:
        t1 = {}
        t2 = {}
        print(e)
        left, right = e
        t1[left] = data[left - 1]
        t2[right] = data[right - 1]
        edges_d = deque(edges)

        while edges_d:
            e2 = edges_d.pop()
            if e == e2:
                continue

            left, right = e2
            if left in t1:
                t1[right] = data[right - 1]
                continue
            if left in t2:
                t2[right] = data[right - 1]
                continue

            if right in t1:
                t1[left] = data[left - 1]
                continue
            if right in t2:
                t2[left] = data[left - 1]
                continue

            e2 = edges_d.appendleft(e2)

        # for e2 in edges:
        #     if e == e2:
        #         continue
        #     left, right = e2
        #     if left in t1:
        #         t1[right] = data[right-1]
        #     if left in t2:
        #         t2[right] = data[right-1]

        #     if right in t1:
        #         t1[left] = data[left-1]
        #     if right in t2:
        #         t2[left] = data[left-1]

        print(f"{t1=}")
        print(f"{t2=}")

        t1_sum = sum(t1.values())
        t2_sum = sum(t2.values())
        abs_diff = abs(t1_sum - t2_sum)
        if min_sum > abs_diff:
            min_sum = abs_diff

        print(f"{t1_sum=}")
        print(f"{t2_sum=}")

    return min_sum


if __name__ == '__main__':
    data =  [100, 200, 100, 500, 100, 600]

    edges =  [[1, 2], [2, 3], [2, 5], [4, 5], [5, 6]]

    result = cutTheTree(data, edges)

    print(f"{result=}")
