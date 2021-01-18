n = int(input())

rows = n
columns = n
matrix = []
coal = 0
count_coal = 0
flag = True

commands = [el for el in input().split()]

for i in range(rows):
    matrix.append([])
    matrix[i] += list(input().split())

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 'c':
            coal += 1
        elif matrix[i][j] == 's':
            row = i
            column = j

for el in commands:
    if el == 'right':
        try:
            if matrix[row][column + 1]:
                column += 1
        except:
            IndexError
    elif el == 'left':
        try:
            if matrix[row][column - 1]:
                column -= 1
        except:
            IndexError
    elif el == 'up':
        try:
            if matrix[row - 1][column]:
                row -= 1
        except:
            IndexError
    elif el == 'down':
        try:
            if matrix[row + 1][column]:
                row += 1
        except:
            IndexError

    if matrix[row][column] == 'c':
        count_coal += 1
        matrix[row][column] = '*'
        if count_coal == coal:
            print(f'You collected all coals! ({row}, {column})')
            flag = False
            break
    elif matrix[row][column] == 'e':
        print(f'Game over! ({row}, {column})')
        flag = False
        break

if flag:
    print(f'{coal - count_coal} coals left. ({row}, {column})')
