#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'renameFile' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING newName
#  2. STRING oldName
#

def rename_file(new_name, old_name):
    modulo = 10**9 + 7  # Modulo to prevent integer overflow
    len_new, len_old = len(new_name), len(old_name)

    # DP array: dp[j] represents the number of ways to form new[:i] using old[:j]
    dp = [1] * (len_old + 1)  # Base case: An empty new can be formed in 1 way

    for i in range(1, len_new + 1):
        new_dp = [0] * (len_old + 1)  # New DP row for the current new prefix

        for j in range(1, len_old + 1):
            # Carry over previous result
            new_dp[j] = new_dp[j - 1]

            # If characters match, add previous count
            if new_name[i - 1] == old_name[j - 1]:
                new_dp[j] = (new_dp[j] + dp[j - 1]) % modulo

        dp = new_dp  # Move to next row

    return dp[len_old]  # The final result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    newName = input()

    oldName = input()

    result = rename_file(newName, oldName)

    fptr.write(str(result) + '\n')

    fptr.close()
