#!/bin/python3

import os


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesar_cipher(input_s, k):
    letters_count = ord('z') - ord('a') + 1
    for c in range(len(input_s)):
        if 'a' <= input_s[c] <= 'z':
            next_letter_ord = ord(input_s[c]) + k % letters_count
            new_ord = next_letter_ord - letters_count if next_letter_ord > ord('z') else next_letter_ord
            new_char = chr(new_ord)
        elif 'A' <= input_s[c] <= 'Z':
            next_letter_ord = ord(input_s[c]) + k % letters_count
            new_ord = next_letter_ord - letters_count if next_letter_ord > ord('Z') else next_letter_ord
            new_char = chr(new_ord)
        else:
            new_char = input_s[c]
        input_s = input_s[:c] + new_char + input_s[c + 1:]
    return input_s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesar_cipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
