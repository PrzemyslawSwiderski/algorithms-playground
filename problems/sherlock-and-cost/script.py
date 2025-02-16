#!/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-cost/problem
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
def cost(B):
    b_len = len(B)

    # Initialize sums and path trackers
    max_sum, min_sum = 0, 0
    max_path, min_path = [B[0]], [1]  # Assume first element is either original or 1

    for i in range(1, b_len):
        # Compute possible new costs
        sum_with_min_prev_1 = min_sum + abs(1 - 1)
        sum_with_max_prev_1 = max_sum + abs(1 - B[i - 1])

        sum_with_min_prev_2 = min_sum + abs(B[i] - 1)
        sum_with_max_prev_2 = max_sum + abs(B[i] - B[i - 1])

        # Determine next values and paths
        if sum_with_min_prev_1 > sum_with_max_prev_1:
            min_next, min_new_path = sum_with_min_prev_1, min_path + [1]
        else:
            min_next, min_new_path = sum_with_max_prev_1, max_path + [1]

        if sum_with_min_prev_2 > sum_with_max_prev_2:
            max_next, max_new_path = sum_with_min_prev_2, min_path + [B[i]]
        else:
            max_next, max_new_path = sum_with_max_prev_2, max_path + [B[i]]

        # Update sums and paths
        min_sum, min_path = min_next, min_new_path
        max_sum, max_path = max_next, max_new_path

    # Determine the optimal cost and path
    if max_sum > min_sum:
        return max_sum, max_path
    else:
        return min_sum, min_path


if __name__ == '__main__':
    B = [69, 19, 15, 81, 93, 100, 35, 18, 81, 16, 65, 20, 4, 45, 81, 83, 90, 14, 82, 85, 43, 7, 64, 76, 33, 47, 95, 12,
         78, 93, 14, 22, 97, 36, 65, 66, 36, 26, 59, 81, 81, 82, 44, 79, 89, 94, 32, 94, 22, 33, 19, 46, 46, 62, 19, 47,
         70, 91, 97, 62, 17, 43, 11, 25, 74, 73, 64, 98, 73, 7, 40, 8, 2, 96, 89, 81, 80, 17, 88, 13, 31, 44, 64]

    # B = [66, 36, 26, 59, 81, 81, 82]
    # B = [3, 15, 4, 12, 10]
    # B = [2, 10, 2, 20]
    # B = [10, 10, 10, 2]

    cost_value, chosen_path = cost(B)

    print(chosen_path)
    sum_verif = 0
    for k in range(1, len(chosen_path)):
        sum_verif += abs(chosen_path[k] - chosen_path[k - 1])
    print(sum_verif)

    print(cost_value)
