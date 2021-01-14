rows, columns = map(int, input().split())

matrix = []
max_sum_square = 0
square_matrix = []
row = None
column = None

for i in range(rows):
    matrix.append([])
    matrix[i] += list(map(int, input().split()))

for i in range(rows - 2):
    for j in range(columns - 2):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] \
                      + matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] \
                      + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if current_sum > max_sum_square:
            max_sum_square = current_sum
            row = i
            column = j

square_matrix = [[matrix[row][column], matrix[row][column + 1], matrix[row][column + 2]],
                 [matrix[row + 1][column], matrix[row + 1][column + 1], matrix[row + 1][column + 2]],
                 [matrix[row + 2][column], matrix[row + 2][column + 1], matrix[row + 2][column + 2]]]

print(f'Sum = {max_sum_square}')
[print(*row, sep=' ') for row in square_matrix]
