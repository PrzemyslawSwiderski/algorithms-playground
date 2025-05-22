#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def game_of_thrones(s):
    letters = {}

    for c in s:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    odd_count = 0

    for key, count in letters.items():
        if count % 2 != 0:
            odd_count += 1

    if len(s) % 2 == 0 and odd_count == 0:
        return 'YES'
    elif len(s) % 2 != 0 and odd_count == 1:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = game_of_thrones(s)

    fptr.write(result + '\n')

    fptr.close()
