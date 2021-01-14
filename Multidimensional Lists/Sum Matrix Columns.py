rows, columns = [int(x) for x in input().split(', ')]

matrix = []
sum_column = 0

for i in range(rows):
    matrix.append([])
    for j in [int(x) for x in input().split(' ')]:
        matrix[i].append(j)

for j in range(columns):
    sum_column = 0
    for i in range(rows):
        sum_column += matrix[i][j]
    print(sum_column)
