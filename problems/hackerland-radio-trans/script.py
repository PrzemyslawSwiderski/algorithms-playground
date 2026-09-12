#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#
def hackerlandRadioTransmitters(x, k):
    x = sorted(x)
    n = len(x)
    i = 0
    transmitters = 0

    while i < n:
        loc = x[i] + k
        j = i
        while j + 1 < n and x[j + 1] <= loc:
            j += 1
        transmitter_pos = x[j]
        transmitters += 1

        coverage_end = transmitter_pos + k
        while i < n and x[i] <= coverage_end:
            i += 1

    return transmitters

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # first_multiple_input = input().rstrip().split()

    n = 8

    k = 2

    x = [7, 2, 4, 6, 5, 9, 12, 11]

    result = hackerlandRadioTransmitters(x, k)

    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
