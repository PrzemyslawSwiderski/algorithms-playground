#!/bin/python3

import os


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compare_triplets(a, b):
    alice_score = 0
    bob_score = 0

    i = 0
    while i < len(a):
        if a[i]>b[i]:
            alice_score+=1
        if a[i]<b[i]:
            bob_score+=1
        i+=1

    return [alice_score, bob_score]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compare_triplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
