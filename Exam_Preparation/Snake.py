n = int(input())

rows = n
columns = n
matrix = []
row_index = ''
col_index = ''
b_index = []
eaten_food = 0

for i in range(rows):
    matrix.append([])
    matrix[i] = list(input())

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 'S':
            row_index = i
            col_index = j
        if matrix[i][j] == 'B':
            b_index.append([i, j])

while True:
    command = input()
    if command:
        if command == 'up':
            matrix[row_index][col_index] = '.'
            row_index -= 1
            if rows - 1 < row_index or row_index < 0:
                print(f'Game over!')
                break
            elif matrix[row_index][col_index] == '*':
                matrix[row_index][col_index] = 'S'
                eaten_food += 1
                if eaten_food == 10:
                    print(f'You won! You fed the snake.')
                    break
            elif matrix[row_index][col_index] == 'B':
                if row_index == b_index[0][0] and col_index == b_index[0][1]:
                    matrix[row_index][col_index] = '.'
                    row_index = b_index[1][0]
                    col_index = b_index[1][1]
                else:
                    matrix[row_index][col_index] = '.'
                    row_index = b_index[0][0]
                    col_index = b_index[0][1]
                matrix[row_index][col_index] = 'S'
        elif command == 'down':
            matrix[row_index][col_index] = '.'
            row_index += 1
            if rows - 1 < row_index or row_index < 0:
                print(f'Game over!')
                break
            elif matrix[row_index][col_index] == '*':
                matrix[row_index][col_index] = 'S'
                eaten_food += 1
                if eaten_food == 10:
                    print(f'You won! You fed the snake.')
                    break
            elif matrix[row_index][col_index] == 'B':
                if row_index == b_index[0][0] and col_index == b_index[0][1]:
                    matrix[row_index][col_index] = '.'
                    row_index = b_index[1][0]
                    col_index = b_index[1][1]
                else:
                    matrix[row_index][col_index] = '.'
                    row_index = b_index[0][0]
                    col_index = b_index[0][1]
                matrix[row_index][col_index] = 'S'
        elif command == 'left':
            matrix[row_index][col_index] = '.'
            col_index -= 1
            if columns - 1 < col_index or col_index < 0:
                print(f'Game over!')
                break
            elif matrix[row_index][col_index] == '*':
                matrix[row_index][col_index] = 'S'
                eaten_food += 1
                if eaten_food == 10:
                    print(f'You won! You fed the snake.')
                    break
            elif matrix[row_index][col_index] == 'B':
                if row_index == b_index[0][0] and col_index == b_index[0][1]:
                    matrix[row_index][col_index] = '.'
                    row_index = b_index[1][0]
                    col_index = b_index[1][1]
                else:
                    matrix[row_index][col_index] = '.'
                    row_index = b_index[0][0]
                    col_index = b_index[0][1]
                matrix[row_index][col_index] = 'S'
        elif command == 'right':
            matrix[row_index][col_index] = '.'
            col_index += 1
            if columns - 1 < col_index or col_index < 0:
                print(f'Game over!')
                break
            elif matrix[row_index][col_index] == '*':
                matrix[row_index][col_index] = 'S'
                eaten_food += 1
                if eaten_food == 10:
                    print(f'You won! You fed the snake.')
                    break
            elif matrix[row_index][col_index] == 'B':
                if row_index == b_index[0][0] and col_index == b_index[0][1]:
                    matrix[row_index][col_index] = '.'
                    row_index = b_index[1][0]
                    col_index = b_index[1][1]
                else:
                    matrix[row_index][col_index] = '.'
                    row_index = b_index[0][0]
                    col_index = b_index[0][1]
                matrix[row_index][col_index] = 'S'

    else:
        break

print(f'Food eaten: {eaten_food}')
for row in matrix:
    print(*row, sep='')
