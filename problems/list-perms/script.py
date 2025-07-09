#!/bin/python3
from collections import deque


def list_perms(input_str):
    output_perms = deque([[]])

    chars = list(input_str)

    for _ in range(len(chars)):
        new_perms = deque()

        while output_perms:
            current = ''.join(output_perms.popleft())
            for c in chars:
                if c not in current:
                    new_perms.append(current + c)

        output_perms = new_perms


    return output_perms


if __name__ == '__main__':

    test_input = 'ABCD'
    result = list_perms(test_input)

    for i in result:
        print(i)
