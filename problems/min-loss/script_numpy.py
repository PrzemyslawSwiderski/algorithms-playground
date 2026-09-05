#!/bin/python3

import numpy as np


# https://www.hackerrank.com/challenges/minimum-loss/problem
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#


def minimumLoss(price):
    arr = np.array(price)
    order = np.argsort(-arr, kind='stable')  # descending sort, indices
    sorted_vals = arr[order]
    sorted_idx = order

    diffs = sorted_vals[:-1] - sorted_vals[1:]
    valid = sorted_idx[:-1] < sorted_idx[1:]

    diffs = np.where(valid, diffs, np.iinfo(np.int64).max)
    best = np.argmin(diffs)

    return sorted_idx[best], sorted_idx[best + 1], diffs[best]


if __name__ == '__main__':
    n = 5

    price = list([20, 7, 8, 2, 5])

    best_i, best_j, min_loss = minimumLoss(price)

    print(min_loss)
