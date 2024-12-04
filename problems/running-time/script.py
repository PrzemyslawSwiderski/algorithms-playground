#!/bin/python3

import os


#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def running_time(arr):
    all_shifts = 0
    i = 1

    while i < len(arr):
        current_shifts = 0
        if arr[i] < arr[i - 1]:
            elem = arr[i]
            j = i
            while j > 0 and arr[j - 1] > elem:
                arr[j] = arr[j - 1]
                j -= 1
                current_shifts += 1

            arr[j] = elem

        all_shifts += current_shifts
        i += 1
    return all_shifts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = running_time(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
