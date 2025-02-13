#!/bin/python3
import os


# https://www.hackerrank.com/challenges/coin-change/problem?isFullScreen=true
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def get_ways_old(n, c):
    count = [0] * (n + 1)
    count[0] = 1
    for coin in c:
        for i in range(coin, n + 1):
            count[i] += count[i - coin]

    for amount, ways in enumerate(count):
        print(f"{amount=} {ways=}")
    return count[n]


def get_ways(n, c):
    counts = []
    for i in range(n + 1):
        counts.append({"ways_count": 0, "coin_sets": []})
    counts[0]["ways_count"] = 1
    for coin in c:
        for amount in range(coin, n + 1):
            prev_count = counts[amount - coin]
            counts[amount]["ways_count"] += prev_count["ways_count"]

            coin_sets = counts[amount]["coin_sets"]
            if not prev_count["coin_sets"] and prev_count["ways_count"] > 0:
                coin_sets.append([coin])

            for coins_set in prev_count["coin_sets"]:
                prev_extended = [*coins_set, coin]
                coin_sets.append(prev_extended)

    for amount, c in enumerate(counts):
        ways = c["ways_count"]
        coin_sets = c["coin_sets"]
        print(f"{amount=} {ways=} {coin_sets=}")

    return counts[n]["ways_count"]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = get_ways(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
