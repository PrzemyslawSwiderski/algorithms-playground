#!/bin/python3


# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decent_number(n):
    output_str = ''

    if n in [1, 2, 4, 7]:
        output_str = ''
    elif n == 5:
        output_str += '33333'
    else:
        r = n % 3
        if r == 2:
            c = n - 5
            output_str += '5' * c
            output_str += '33333'
        elif r == 1:
            c = n - 10
            output_str += '5' * c
            output_str += '33333'
            output_str += '33333'
        else:
            output_str += '5' * n

    if output_str == '':
        print('-1')
    else:
        print(output_str)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decent_number(n)
