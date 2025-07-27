#!/bin/python3


# Count Sort
# https://www.hackerrank.com/challenges/countingsort4/problem?isFullScreen=true
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def count_sort(arr):
    size = len(arr)
    val_map = {}

    for idx, entry in enumerate(arr):
        num_str, str_val = entry
        num = int(num_str)
        if idx < (size / 2):
            str_val = '-'

        if num in val_map:
            val_map[num] += [str_val]
        else:
            val_map[num] = [str_val]

    output_str = ""
    vals = sorted(val_map.keys())
    print(vals)
    for k in vals:
        str_val = " ".join(val_map[k])
        output_str += str_val
        output_str += " "

    print(output_str)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    count_sort(arr)
