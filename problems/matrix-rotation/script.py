#!/bin/python3
from os import error


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def rotate_ring(matrix, i_first, i_last, j_first, j_last, rotations):
    ring = []
    # Collect the elements in the ring to 1D array
    # Traverse right
    ring.extend(matrix[i_first][j_first:j_last])
    # Traverse down
    ring.extend(matrix[i][j_last] for i in range(i_first, i_last))
    # Traverse left
    ring.extend(matrix[i_last][j_last:j_first:-1])
    # Traverse up
    ring.extend(matrix[i][j_first] for i in range(i_last, i_first, -1))

    ring_rotations = rotations % len(ring)
    # Rotate left for ring_rotations rotations
    rotated_line = ring[ring_rotations:] + ring[:ring_rotations]

    pos = 0

    # Update elements in the input matrix
    # Traverse right
    for j in range(j_first, j_last):
        matrix[i_first][j] = rotated_line[pos]
        pos += 1
    # Traverse down
    for i in range(i_first, i_last):
        matrix[i][j_last] = rotated_line[pos]
        pos += 1
    # Traverse left
    for j in range(j_last, j_first, -1):
        matrix[i_last][j] = rotated_line[pos]
        pos += 1
    # Traverse up
    for i in range(i_last, i_first, -1):
        matrix[i][j_first] = rotated_line[pos]
        pos += 1


def matrix_rotation(matrix, rotations):
    rows, cols = len(matrix), len(matrix[0])
    max_offset = min(rows, cols) // 2

    for offset in range(max_offset):
        rows_offset_start, cols_offset_start = (offset, offset)
        rows_offset_end = rows - 1 - rows_offset_start
        cols_offset_end = cols - 1 - cols_offset_start
        rotate_ring(matrix, rows_offset_start, rows_offset_end, cols_offset_start, cols_offset_end, rotations)

    print_matrix(matrix)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    input_matrix = []

    for _ in range(m):
        input_matrix.append(list(map(int, input().rstrip().split())))

    matrix_rotation(input_matrix, r)
