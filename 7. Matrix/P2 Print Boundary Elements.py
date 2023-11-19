# Q. Given a matrix print it's boundary elements .i.e. alternate rows from left to
# right and right to left.
#
# I/P: [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
#   ]

# Output: 1 2 3 4 8 12 16 15 14 13 9 5


def print_boundary_elements(matrix, rows, cols):
    if rows == 1:
        for j in range(cols):
            print(matrix[0][j], end=' ')
    elif cols == 1:
        for i in range(rows):
            print(matrix[i][0], end=' ')
    else:
        for j in range(cols):
            print(matrix[0][j], end=' ')
        for i in range(1, rows):
            print(matrix[i][cols-1], end=' ')
        for j in range(cols-2, -1, -1):
            print(matrix[rows-1][j], end=' ')
        for i in range(rows-2, 0, -1):
            print(matrix[i][0], end=' ')

    print()

if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    rows = len(matrix)
    cols = len(matrix[0])
    print_boundary_elements(matrix, rows, cols)