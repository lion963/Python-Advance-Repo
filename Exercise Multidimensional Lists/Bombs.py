n = int(input())

rows = n
columns = n
matrix = []
active_cell = 0
sum_cells = 0

for i in range(rows):
    matrix.append([])
    matrix[i] += list(map(int, input().split()))

bombs = [tuple(map(int, el.split(','))) for el in input().split()]

for el in bombs:
    row = el[0]
    column = el[1]
    if matrix[row][column] > 0:
        try:
            k = row - 1
            l = column - 1
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= matrix[row][column]
        except:
            IndexError
        try:
            k = row - 1
            l = column
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= matrix[row][column]
        except:
            IndexError
        try:
            k = row - 1
            l = column + 1
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= matrix[row][column]
        except:
            IndexError
        try:
            k = row
            l = column - 1
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= matrix[row][column]
        except:
            IndexError
        try:
            k = row
            l = column + 1
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= matrix[row][column]
        except:
            IndexError
        try:
            k = row + 1
            l = column - 1
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= matrix[row][column]
        except:
            IndexError
        try:
            k = row + 1
            l = column
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= matrix[row][column]
        except:
            IndexError
        try:
            k = row + 1
            l = column + 1
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= matrix[row][column]
        except:
            IndexError

        matrix[row][column] = 0

for el in matrix:
    for ele in el:
        if ele > 0:
            active_cell += 1
            sum_cells += ele

print(f'Alive cells: {active_cell}')
print(f'Sum: {sum_cells}')
[print(*row, sep=' ') for row in matrix]
