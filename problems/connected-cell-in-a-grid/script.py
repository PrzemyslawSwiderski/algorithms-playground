#!/bin/python3

# https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

# All 8 directions a neighbor can be in, as (row_offset, column_offset).
# Rows go down as the index increases, columns go right.
NEIGHBOR_OFFSETS = [
    (-1, -1), (-1, 0), (-1, 1),  # up-left,   up,    up-right
    (0, -1), (0, 1),  # left,             right
    (1, -1), (1, 0), (1, 1),  # down-left, down,  down-right
]


def is_inside_grid(row_index, column_index, total_rows, total_columns):
    """Return True if (row_index, column_index) is a valid cell in the grid."""
    return 0 <= row_index < total_rows and 0 <= column_index < total_columns


def connectedCell(matrix):
    total_rows = len(matrix)
    total_columns = len(matrix[0]) if total_rows > 0 else 0

    largest_region_size = 0

    # Remembers every filled cell we have already counted, so that no cell
    # is ever counted in more than one region (or counted twice).
    visited_cells = set()

    # Scan the grid cell by cell, looking for the start of a new region.
    for start_row in range(total_rows):
        for start_column in range(total_columns):

            cell_is_empty = matrix[start_row][start_column] == 0
            cell_already_counted = (start_row, start_column) in visited_cells

            if cell_is_empty or cell_already_counted:
                continue

            # We found a filled cell that belongs to a region we haven't
            # seen yet. Explore the whole region with a depth-first search.
            current_region_size = 0

            # The stack holds cells that still need to be processed.
            cells_to_explore = [(start_row, start_column)]

            # Mark as visited right when the cell is added to the stack,
            # so the same cell can never be added twice.
            visited_cells.add((start_row, start_column))

            while cells_to_explore:
                current_row, current_column = cells_to_explore.pop()
                current_region_size += 1

                # Look at all 8 surrounding cells.
                for row_offset, column_offset in NEIGHBOR_OFFSETS:
                    neighbor_row = current_row + row_offset
                    neighbor_column = current_column + column_offset

                    if not is_inside_grid(neighbor_row, neighbor_column,
                                          total_rows, total_columns):
                        continue

                    neighbor_is_filled = matrix[neighbor_row][neighbor_column] == 1
                    neighbor_already_seen = (neighbor_row, neighbor_column) in visited_cells

                    if neighbor_is_filled and not neighbor_already_seen:
                        visited_cells.add((neighbor_row, neighbor_column))
                        cells_to_explore.append((neighbor_row, neighbor_column))

            # The region is fully explored; keep it if it's the biggest so far.
            if current_region_size > largest_region_size:
                largest_region_size = current_region_size

    return largest_region_size


if __name__ == '__main__':
    # matrix = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
    # diagonal should be supported as well (result: 5 expected) :
    matrix = [
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1]
    ]

    result = connectedCell(matrix)

    print(result)
