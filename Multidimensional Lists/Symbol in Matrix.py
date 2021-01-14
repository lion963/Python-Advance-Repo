size = int(input())

rows = size
columns = size
matrix = []
found = False
location = []

for i in range(rows):
    matrix.append([])
    for j in list(input()):
        matrix[i].append(j)

symbol = input()

for row in range(rows):
    if found:
        break
    for column in range(columns):
        if matrix[row][column] == symbol:
            location = [row, column]
            found = True

if found:
    print(f'({location[0]}, {location[1]})')
else:
    print(f'{symbol} does not occur in the matrix')
