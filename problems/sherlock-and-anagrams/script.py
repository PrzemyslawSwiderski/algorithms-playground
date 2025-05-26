#!/bin/python3

import os
from collections import Counter


# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true
# Complete the 'sherlock_and_anagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlock_and_anagrams(s):
    count = 0
    s_len = len(s)

    step = 0

    while step < s_len:
        pairs = list()

        i = 0
        while i + step < s_len:
            pairs.append((i, i + step))
            i += 1

        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                p_1 = pairs[i]
                p_2 = pairs[j]
                lower_start = p_1[0]
                lower_end = p_1[1]
                higher_start = p_2[0]
                higher_end = p_2[1]

                s1 = s[lower_start:lower_end + 1]
                s2 = s[higher_start:higher_end + 1]
                if Counter(s1) == Counter(s2):
                    # print(f"found pairs: {s1} {s2}")
                    # print(f"{lower_start} {lower_end} -- {higher_start} {higher_end}")
                    count += 1

        step += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlock_and_anagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
