#!/bin/python3

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almost_sorted(arr):
    # Write your code here

    sorted_arr = sorted(arr)

    if arr == sorted_arr:
        print("yes")
        return

    wrong_indexes = []
    for i, (num, sorted_num) in enumerate(zip(arr, sorted_arr)):
        if num == sorted_num:
            continue
        wrong_indexes.append(i + 1)

    if len(wrong_indexes) == 2:
        print("yes")
        print(f"swap {wrong_indexes[0]} {wrong_indexes[1]}")
        return

    first_wrong_idx = wrong_indexes[0] - 1
    last_wrong_idx = wrong_indexes[-1]
    wrong_subarray = arr[first_wrong_idx:last_wrong_idx]
    reversed_sorted_subarray = sorted_arr[first_wrong_idx:last_wrong_idx][::-1]
    if wrong_subarray == reversed_sorted_subarray:
        print("yes")
        print(f"reverse {wrong_indexes[0]} {last_wrong_idx}")
        return

    print("no")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almost_sorted(arr)
