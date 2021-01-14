rows, columns = map(int, input().split())

matrix = []

for i in range(rows):
    matrix.append([])
    matrix[i] += input().split()

while True:
    line = input()
    if line == 'END':
        break

    command_list = line.split()

    if command_list[0] == 'swap' and len(command_list) == 5:
        row1 = int(command_list[1])
        col1 = int(command_list[2])
        row2 = int(command_list[3])
        col2 = int(command_list[4])
        if (row1 and row2) in range(rows) and (col1 and col2) in range(columns):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*row, sep=' ') for row in matrix]
        else:
            print(f'Invalid input!')
    else:
        print(f'Invalid input!')
