#!/bin/python3


# https://www.hackerrank.com/challenges/common-child/problem?isFullScreen=true
# Complete the 'common_child' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def common_child(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    m = [[0 for _ in range(s2_len + 1)] for _ in range(s1_len + 1)]

    for i in range(s1_len):
        for j in range(s2_len):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                continue
            m[i + 1][j + 1] = max(m[i + 1][j], m[i][j + 1])

    return m[-1][-1]


if __name__ == '__main__':
    # s1 = "SHINCHAN"
    s1 = "FBDAN"  # asymmetric triangles example
    # s1 = "WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS"
    # s2 = "NOHARAAA"
    s2 = "ABCDF"
    # s2 = "FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC" # 15 expected

    result = common_child(s1, s2)

    print(f"{result=}")
