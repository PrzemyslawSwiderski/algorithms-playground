#!/bin/python3


# https://www.hackerrank.com/challenges/marcs-cakewalk/problem
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcs_cakewalk(calorie):
    calorie.sort(reverse=True)

    sum_all = 0
    for i, n in enumerate(calorie):
        sum_all += pow(2, i) * n

    return sum_all


if __name__ == '__main__':
    calorie = [3, 8, 11]

    result = marcs_cakewalk(calorie)

    print(result)
