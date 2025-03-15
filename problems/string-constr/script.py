#!/bin/python3

import os


#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def two_strings(s1, s2):
    # Write your code here
    s1_chars = set(s1)
    s2_chars = set(s2)
    print(s1_chars)
    print(s2_chars)
    common = s1_chars & s2_chars
    print(common)

    if len(common) > 0:
        return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = two_strings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
