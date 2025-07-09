#!/bin/python3
from collections import deque


def list_perms(input_str):
    # Initialize with the first permutation (input string as a list)
    perms = deque([[]])  # Start with an empty list
    chars = list(input_str)

    # For each position, add each character to all existing partial permutations
    for _ in range(len(chars)):
        new_perms = deque()
        while perms:
            current = perms.popleft()
            # Try each character not yet used in the current permutation
            for c in chars:
                if c not in current:  # Avoid duplicates in permutation
                    new_perm = current + [c]
                    new_perms.append(new_perm)
        perms = new_perms

    # Convert character lists to strings
    return [''.join(perm) for perm in perms]


if __name__ == '__main__':

    test_input = 'ABCD'
    result = list_perms(test_input)

    for i in result:
        print(i)
