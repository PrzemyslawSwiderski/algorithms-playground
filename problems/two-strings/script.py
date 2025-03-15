#!/bin/python3

import os


# https://www.hackerrank.com/challenges/string-construction/problem?isFullScreen=true
# Complete the 'string_construction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def string_construction(s):
    # Write your code here
    s = list(s)
    p = []
    min_cost = 0
    i = 0
    while len(p) < len(s):
        max_substr = max_substring(p, s[i:])
        print(f'{max_substr=}')
        if i > 0 and len(max_substr) > 0:
            p.extend(max_substr)
            i += len(max_substr)
        else:
            p.append(s[i])
            i += 1
            min_cost += 1

    return min_cost


def max_substring(p, i_s):
    sub_str = []

    p_str = ''.join(p)
    i_s_str = ''.join(i_s)

    i = 1
    while i <= len(i_s) and i_s_str[:i] in p_str:
        sub_str = i_s_str[:i]
        i += 1

    print(f'{sub_str=}')
    return sub_str

def string_construction_proper_one(s):
    # Write your code here
    return len(set(s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = string_construction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
