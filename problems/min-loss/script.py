#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/minimum-loss/problem
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    min_loss = 10**16
    min_i = -1
    min_j = -1

    for i in range(0, len(price)):
        for j in range(i+1, len(price)):
            val1 = price[i]
            val2 = price[j]
            loss = val1 - val2
            if 0 < loss < min_loss:
                min_loss = loss
                min_i = i
                min_j = j

    print(min_i)
    print(min_j)
    return min_loss


if __name__ == '__main__':
    n = 5

    price = list([20, 7, 8, 2, 5])

    result = minimumLoss(price)

    print(result)
