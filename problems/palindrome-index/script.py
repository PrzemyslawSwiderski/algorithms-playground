#!/bin/python3

import os


# https://www.hackerrank.com/challenges/palindrome-index/problem?isFullScreen=true
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def palindrome_index(input_str):
    i = 0
    while i < len(input_str) / 2:
        j = len(input_str) - 1 - i
        if input_str[i] != input_str[j]:
            left_removed = s[:i] + s[i+1:]
            if is_palindrome(left_removed):
                return i
            else:
                return j
        i += 1
    return -1

def is_palindrome(input_str):
    i = 0
    while i < len(input_str) / 2:
        j = len(input_str) - 1 - i
        if input_str[i] != input_str[j]:
            return False
        i += 1
    return True


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindrome_index(s)
        print(result)
        fptr.write(str(result) + '\n')

    fptr.close()
