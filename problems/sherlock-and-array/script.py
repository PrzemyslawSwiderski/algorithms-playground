#!/bin/python3


# https://www.hackerrank.com/challenges/sherlock-and-array/problem?isFullScreen=true
# Complete the 'balanced_sums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as a parameter.
#

def balanced_sums(input_arr):
    sums = [0]
    arr_len = len(input_arr)

    for i in range(arr_len):
        sums.append(input_arr[i])
        sums[i + 1] += sums[i]

    all_sum = 0
    for i in range(arr_len):
        all_sum += input_arr[i]

    for i in range(arr_len):
        left_sum = sums[i]
        right_sum = all_sum - sums[i] - input_arr[i]
        if right_sum == left_sum:
            return 'YES'

    return 'NO'


if __name__ == '__main__':
    arr = [1, 1, 4, 1, 1]

    result = balanced_sums(arr)

    print(result)
