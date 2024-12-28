#!/bin/python3

# https://www.hackerrank.com/challenges/separate-the-numbers/problem?isFullScreen=true
# Complete the 'separate_numbers' function below.
#
# The function accepts STRING s as parameter.
def separate_numbers(s):
    i = 1
    while i <= len(s) / 2:
        num = int(s[:i])
        if others_increasing(num, s):
            print(f"YES {num}")
            return
        i += 1
    print("NO")


def others_increasing(start_num, input_s):
    current_num = start_num
    prev_str = input_s
    tmp_str = input_s.removeprefix(str(start_num))

    while prev_str != tmp_str:
        current_num = current_num + 1
        prev_str = tmp_str
        tmp_str = tmp_str.removeprefix(str(current_num))

    if tmp_str == "":
        return True
    else:
        return False


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separate_numbers(s)
