def create_matrix(rows, columns):
    matrix = []
    for row in range(rows):
        matrix.append(['^'] * columns)
    return matrix


def print_matrix(matrix):
    [print(*row, sep=' ') for row in matrix]


def put_bombs(matrix, *args):
    for indexes in args:
        row = indexes[0]
        column = indexes[1]
        matrix[row][column] = '*'
    return matrix


def check_bombs_count(matrix, *args):
    row = args[0]
    column = args[1]
    count_bombs = 0
    for k in range(row - 1, row + 2):
        for l in range(column - 1, column + 2):
            try:
                if k >= 0 and l >= 0:
                    if matrix[k][l] == '*':
                        count_bombs += 1
            except:
                IndexError
    return count_bombs


def check_neighbour_bombs_count(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if not matrix[i][j] == '*':
                cell = [i, j]
                matrix[i][j] = check_bombs_count(matrix, *cell)
    return matrix


# create matrix
n = int(input())
rows = n
columns = n
matrix = create_matrix(rows, columns)

# collect bombs indexes
bombs_count = int(input())
bombs_indexes = []
for _ in range(bombs_count):
    indexes = map(int, input()[1:-1].split(', '))
    bombs_indexes.append(tuple(indexes))

# modify and print matrix
put_bombs(matrix, *bombs_indexes)
check_neighbour_bombs_count(matrix)
print_matrix(matrix)
