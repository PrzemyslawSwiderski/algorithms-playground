#!/bin/python3

# https://www.hackerrank.com/challenges/richie-rich/problem
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#
#
# Strategy:
# 1. Make for each different pair make it
#
def highestValuePalindrome(s, n, k):
    arr = list(s)

    mismatches = 0
    i = 0
    j = n - 1
    while i < j:
        if arr[i] != arr[j]:
            mismatches += 1
        i += 1
        j -= 1

    if mismatches > k:
        return "-1"

    remaining_mismatches = mismatches
    i = 0
    j = n - 1
    while i <= j:
        if i == j:
            if k > 0:
                arr[i] = '9'
                k -= 1
        elif arr[i] == arr[j]:
            if arr[i] != '9' and k >= 2 and k - 2 >= remaining_mismatches:
                arr[i] = '9'
                arr[j] = '9'
                k -= 2
        else:
            remaining_mismatches -= 1
            high = max(arr[i], arr[j])
            if high == '9':
                arr[i] = '9'
                arr[j] = '9'
                k -= 1
            elif k >= 2 and k - 2 >= remaining_mismatches:
                arr[i] = '9'
                arr[j] = '9'
                k -= 2
            else:
                arr[i] = high
                arr[j] = high
                k -= 1
        i += 1
        j -= 1

    return ''.join(arr)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # first_multiple_input = input().rstrip().split()

    n = 6

    k = 4

    s = "109234821"

    result = highestValuePalindrome(s, n, k)

    print(f"Result: {result}")
