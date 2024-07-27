#!/bin/python3

import os


#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#
# https://www.hackerrank.com/challenges/happy-ladybugs/problem
#

def happy_ladybugs(b):
    # Write your code here
    if '_' in b:
        b = sorted(b)
        b = ''.join(b)
        b = b.rstrip("_")

    all_idx = set(b)
    happy_idx = set()
    for i in range(len(b) - 1):
        current_lady = b[i]
        next_lady = b[i + 1]
        if current_lady in happy_idx:
            continue

        if current_lady != next_lady:
            return 'NO'
        else:
            happy_idx.add(current_lady)

    print(f'all_idx = {all_idx}')
    print(f'happy_idx = {happy_idx}')

    if len(all_idx) == len(happy_idx):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happy_ladybugs(b)

        fptr.write(result + '\n')

    fptr.close()
