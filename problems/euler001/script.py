#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

def get_arithmetic_sum(step, max_limit):
    nums_count = max_limit // step
    return nums_count * (step + step * nums_count) // 2


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    max_num = n - 1

    sum_of_3 = get_arithmetic_sum(3, max_num)
    sum_of_5 = get_arithmetic_sum(5, max_num)
    sum_of_15 = get_arithmetic_sum(15, max_num)

    overall = sum_of_3 + sum_of_5 - sum_of_15
    print(overall)
