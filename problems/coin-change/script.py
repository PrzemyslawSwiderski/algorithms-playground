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
    return count[n]


def get_ways(n, c):
    counts = []
    for i in range(n + 1):
        counts.append({"value": 0, "coin_sets": []})
    counts[0]["value"] = 1
    for coin in c:
        for amount in range(coin, n + 1):
            prev_count = counts[amount - coin]
            counts[amount]["value"] += prev_count["value"]

            coin_sets = counts[amount]["coin_sets"]
            if not prev_count["coin_sets"]:
                coin_sets.append([coin])
                continue

            for coins_sets in prev_count["coin_sets"]:
                prev_extended = [*coins_sets, coin]
                coin_sets.append(prev_extended)

    i = 0
    for c in counts:
        value = c["value"]
        coins_sets = c["coin_sets"]
        print(f"{i=} {value=} {coins_sets=}")
        i += 1

    return counts[n]["value"]


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
