#!/bin/python3

import os


#
# Complete the 'quick_sort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quick_sort(arr):
    # Write your code here
    pivot = arr[0]
    left_idx = 1
    right_idx = len(arr) - 1

    # 1 2 3 4
    # 4 3 2 1

    # 20
    # 45 25 46 48 28 6 13 5 36 44 7 4 11 30 24 34 15 31 38 49
    # expected:
    # 25 28 6 13 5 36 44 7 4 11 30 24 34 15 31 38 45 46 48 49
    while left_idx <= right_idx:
        if arr[left_idx] > pivot > arr[right_idx]:
            tmp = arr[left_idx]
            arr[left_idx] = arr[right_idx]
            arr[right_idx] = tmp

        if arr[left_idx] < pivot:
            left_idx+=1
        if arr[right_idx] > pivot:
            right_idx-=1

    tmp = arr[right_idx]
    arr[right_idx] = arr[0]
    arr[0] = tmp

    return arr



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quick_sort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
