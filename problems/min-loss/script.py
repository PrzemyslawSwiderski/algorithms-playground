#!/bin/python3

import numpy as np


# https://www.hackerrank.com/challenges/minimum-loss/problem
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#


def minimumLoss(price):
    indexed = sorted(((p, i) for i, p in enumerate(price)), reverse=True)

    min_loss = 10**17
    min_i = -1
    min_j = -1

    for k in range(len(indexed) - 1):
        val1, idx1 = indexed[k]
        val2, idx2 = indexed[k + 1]
        if idx1 < idx2:
            loss = val1 - val2
            if loss < min_loss:
                min_loss = loss
                min_i = idx1
                min_j = idx2

    print(min_i)
    print(min_j)
    return min_loss

if __name__ == '__main__':
    n = 5

    price = list([20, 7, 8, 2, 5])

    result = minimumLoss(price)

    print(result)
