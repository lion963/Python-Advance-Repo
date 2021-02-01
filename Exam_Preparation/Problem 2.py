def create_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        matrix.append([])
        matrix[i] += list(input())
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


def player_position(matrix):
    for k in range(len(matrix)):
        for l in range(len(matrix[k])):
            if matrix[k][l] == 'P':
                return k, l


def validate_position(row, column):
    if 0 <= row < rows and 0 <= column < columns:
        return True
    return False


def up(matrix, row, column, text):
    if validate_position(row - 1, column):
        if matrix[row - 1][column] == '-':
            matrix[row][column] = '-'
            matrix[row - 1][column] = 'P'
        else:
            text += matrix[row - 1][column]
            matrix[row][column] = '-'
            matrix[row - 1][column] = 'P'
    else:
        if text:
            text = text[:-1]
        row = row
        column = column
        return matrix, text, row, column
    row = row - 1
    column = column
    return matrix, text, row, column


def down(matrix, row, column, text):
    if validate_position(row + 1, column):
        if matrix[row + 1][column] == '-':
            matrix[row][column] = '-'
            matrix[row + 1][column] = 'P'
        else:
            text += matrix[row + 1][column]
            matrix[row][column] = '-'
            matrix[row + 1][column] = 'P'
    else:
        if text:
            text = text[:-1]
        row = row
        column = column
        return matrix, text, row, column
    row = row + 1
    column = column
    return matrix, text, row, column


def left(matrix, row, column, text):
    if validate_position(row, column - 1):
        if matrix[row][column - 1] == '-':
            matrix[row][column] = '-'
            matrix[row][column - 1] = 'P'
        else:
            text += matrix[row][column - 1]
            matrix[row][column] = '-'
            matrix[row][column - 1] = 'P'
    else:
        if text:
            text = text[:-1]
        row = row
        column = column
        return matrix, text, row, column
    row = row
    column = column - 1
    return matrix, text, row, column


def right(matrix, row, column, text):
    if validate_position(row, column + 1):
        if matrix[row][column + 1] == '-':
            matrix[row][column] = '-'
            matrix[row][column + 1] = 'P'
        else:
            text += matrix[row][column + 1]
            matrix[row][column] = '-'
            matrix[row][column + 1] = 'P'
    else:
        if text:
            text = text[:-1]
        row = row
        column = column
        return matrix, text, row, column
    row = row
    column = column + 1
    return matrix, text, row, column


mapper = {
    'up': up,
    'down': down,
    'left': left,
    'right': right
}

text = input()
n = int(input())
rows = n
columns = n
matrix = create_matrix(rows, columns)
row, column = player_position(matrix)

for i in range(int(input())):
    command = input()
    matrix, text, row, column = mapper[command](matrix, row, column, text)

print(text)
print_matrix(matrix)
