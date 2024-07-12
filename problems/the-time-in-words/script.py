#!/bin/python3

import os

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#
# https://www.hackerrank.com/challenges/the-time-in-words/problem

hours_to_word = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
}

minutes_to_word = {
    1: "one minute",
    2: "two minutes",
    3: "three minutes",
    4: "four minutes",
    5: "five minutes",
    6: "six minutes",
    7: "seven minutes",
    8: "eight minutes",
    9: "nine minutes",
    10: "ten minutes",
    11: "eleven minutes",
    12: "twelve minutes",
    13: "thirteen minutes",
    14: "fourteen minutes",
    15: "quarter",
    16: "sixteen minutes",
    17: "seventeen minutes",
    18: "eighteen minutes",
    19: "nineteen minutes",
    20: "twenty minutes",
    21: "twenty one minutes",
    22: "twenty two minutes",
    23: "twenty three minutes",
    24: "twenty four minutes",
    25: "twenty five minutes",
    26: "twenty six minutes",
    27: "twenty seven minutes",
    28: "twenty eight minutes",
    29: "twenty nine minutes",
    30: "half",
}


def time_in_words(h, m):
    if m == 0:
        return f"{hours_to_word[h]} o' clock"

    if m > 30:
        return minutes_to_word[60 - m] + " to " + hours_to_word[h + 1]
    else:
        return minutes_to_word[m] + " past " + hours_to_word[h]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = time_in_words(h, m)

    fptr.write(result + '\n')

    fptr.close()
