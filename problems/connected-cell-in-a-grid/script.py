#!/bin/python3

# https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    max_region_size = 0
    visited = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (row, col) in visited:
                continue
            if matrix[row][col] == 1:
                # explore the region
                region_size = 0
                stack = [(row, col)]
                while stack:
                    (node_row, node_col) = stack.pop()
                    if (node_row, node_col) in visited:
                        continue
                    visited.add((node_row, node_col))
                    region_size += 1
                    if node_row > 0 and matrix[node_row - 1][node_col] == 1:
                        stack.append((node_row - 1, node_col))

                    if node_row < len(matrix) - 1 and matrix[node_row + 1][node_col] == 1:
                        stack.append((node_row + 1, node_col))

                    if node_col > 0 and matrix[node_row][node_col - 1] == 1:
                        stack.append((node_row, node_col - 1))

                    if node_col < len(matrix[row]) - 1 and matrix[node_row][node_col + 1] == 1:
                        stack.append((node_row, node_col + 1))

                if region_size > max_region_size:
                    max_region_size = region_size

    return max_region_size


if __name__ == '__main__':
    # matrix = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
    matrix = [[1, 1, 1, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    result = connectedCell(matrix)

    print(result)
