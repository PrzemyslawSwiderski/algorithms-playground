#!/bin/python3

from collections import Counter


# https://www.hackerrank.com/challenges/bear-and-steady-gene/problem
# Complete the 'steady_gene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def steady_gene(genes):
    genes_size = len(genes)
    goal = genes_size // 4
    curr = Counter(genes)
    ans = genes_size
    left_ptr = 0
    right_ptr = 0
    min_left_ptr = 0
    min_right_ptr = 0
    while right_ptr < genes_size:
        curr[genes[right_ptr]] -= 1
        while left_ptr < genes_size and max(curr.values()) <= goal:
            window_size = right_ptr - left_ptr + 1
            if window_size < ans:
                ans = window_size
                min_left_ptr = left_ptr
                min_right_ptr = right_ptr
            curr[genes[left_ptr]] += 1
            left_ptr += 1
        right_ptr += 1

    print(f"{min_left_ptr=} -> {min_right_ptr=}")
    return ans


if __name__ == '__main__':
    # gene = "GAAATAAA" # res = 5
    gene = "TTGTTCCGTTTT" # res = 8
    # gene = "TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC"  # res = 5

    result = steady_gene(gene)

    print(result)
