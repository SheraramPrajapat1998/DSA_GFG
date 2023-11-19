# Q. Given a matrix print it in snake pattern

# I/P: [
#       [1, 2, 3, 4],
#       [5, 6, 7, 8],
#       [9, 10, 11, 12],
#       [13, 14, 15, 16]
#       ]
# O/P: 1 2 3 4 5 8 7 6 5 9 10 11 12 16 15 14 13


def print_snake_pattern(matrix, rows, cols):
    for i in range(rows):
        if(i & 1 == 0):
            for j in range(cols):
                print(matrix[i][j], end=' ')
        else:
            for j in range(cols-1, -1, -1):
                print(matrix[i][j], end=' ')
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
    print_snake_pattern(matrix, rows, cols)
