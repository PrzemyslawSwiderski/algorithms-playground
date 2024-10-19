#!/bin/python3

import os


#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#
# https://www.hackerrank.com/challenges/strange-code/problem
def strange_counter(t):
    previous_cycle_start_time = 0
    current_cycle_start_time = 1
    cycle_size = 3
    # finding cycle after the one covering 't' value
    while current_cycle_start_time <= t:
        previous_cycle_start_time = current_cycle_start_time
        current_cycle_start_time += cycle_size
        cycle_size *= 2

    # the previous one covers 't'
    previous_cycle_size = cycle_size // 2
    return previous_cycle_size - (t - previous_cycle_start_time)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strange_counter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
