

def transpose_matrix(matrix, rows, cols):
    # need to swap between diagonal element
    for i in range(rows):
        for j in range(i+1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def print_matrix(str, matrix, rows, cols):
    if str:
        print(str, end=' ')
    print("[")
    for i in range(rows):
        print(f"\t {matrix[i]}")
    print("]")


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    rows = len(matrix)
    cols = len(matrix[0])
    print_matrix("original matrix: ", matrix, rows, cols)
    transpose_matrix(matrix, rows, cols)
    print_matrix("transpose matrix:", matrix, rows, cols)
