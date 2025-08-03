#!/bin/python3


# https://www.hackerrank.com/challenges/xor-quadruples/problem
# Complete the beautifulQuadruples function below.
#
def beautiful_quadruples(a, b, c, d):
    """
    ALGORITHM EXPLANATION:

    The key insight is to avoid generating all O(abcd) quadruples by using:

    1. SORTING: Sort bounds so a≤b≤c≤d to eliminate duplicate counting

    2. PAIR DECOMPOSITION:
       - Split quadruple (w,x,y,z) into two pairs: (w,x) and (y,z)
       - Condition w^x^y^z ≠ 0 becomes (w^x) ≠ (y^z)

    3. PRECOMPUTATION:
       - Build frequency table of all XOR values for pairs from larger ranges [1,c]×[1,d]
       - For each XOR value v, count how many pairs (y,z) have y^z = v

    4. COUNTING:
       - For each pair (w,x) from smaller ranges [1,a]×[1,b]:
         * Calculate forbidden XOR value: w^x
         * Count pairs (y,z) where y^z ≠ w^x
         * This equals: total_pairs - frequency[w^x]

    5. DYNAMIC UPDATE:
       - Remove processed pairs to avoid double counting
       - As we finish with each w value, remove all pairs (w,z) from our counts

    TIME COMPLEXITY: O(cd + ab + bd) instead of O(abcd)
    SPACE COMPLEXITY: O(max_xor_value)

    This is much faster for large inputs!
    """
    # Sort to ensure we only count each unique quadruple once
    bounds = sorted([a, b, c, d])
    a, b, c, d = bounds

    # Maximum XOR value possible
    max_xor = 1
    while max_xor <= d:
        max_xor <<= 1

    # Count frequency of XOR values for pairs in larger ranges
    xor_count = [0] * max_xor
    total_pairs = 0

    # Build initial frequency table for pairs from [1,c] × [1,d]
    for first in range(1, c + 1):
        for second in range(first, d + 1):
            xor_val = first ^ second
            xor_count[xor_val] += 1
            total_pairs += 1

    result = 0

    # For each pair from smaller ranges [1,a] × [1,b]
    for first in range(1, b + 1):
        for second in range(1, min(a + 1, first + 1)):
            # Find pairs from larger ranges that make XOR ≠ 0
            forbidden = first ^ second
            valid_completions = total_pairs - xor_count[forbidden]
            result += valid_completions

        # Remove pairs starting with 'first' to avoid double counting
        for second in range(first, d + 1):
            xor_val = first ^ second
            xor_count[xor_val] -= 1
            total_pairs -= 1

    return result


if __name__ == '__main__':
    # 1212 3000 233 122 -> 52302691480
    # a = 1212
    # b = 3000
    # c = 233
    # d = 122

    # 1150 1547 853 423 -> 127535297312
    # a = 1150
    # b = 1547
    # c = 853
    # d = 423

    # 1 2 3 4 -> 11
    a = 1
    b = 2
    c = 3
    d = 4

    result = beautiful_quadruples(a, b, c, d)
    print(result)
