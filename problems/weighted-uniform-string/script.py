#!/bin/python3

import os


#
# Complete the 'weighted_uniform_strings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#
def weighted_uniform_strings(s, queries):
    # Write your code here
    res = []
    idx = set()

    idx.add(weight(s[0]))
    i = 1
    tmp_ord = weight(s[0])

    while i < len(s):
        if s[i] == s[i - 1]:
            tmp_ord += weight(s[i])
            idx.add(tmp_ord)
        else:
            tmp_ord = weight(s[i])
            idx.add(tmp_ord)
        i += 1

    print(idx)
    for q in queries:
        if q in idx:
            res.append("Yes")
        else:
            res.append("No")
    return res


def weight(input_char):
    return ord(input_char) - ord('a') + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weighted_uniform_strings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
