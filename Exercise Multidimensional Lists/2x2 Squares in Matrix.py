rows, columns = [int(x) for x in input().split(' ')]

matrix = []
count = 0

for i in range(rows):
    matrix.append([])
    for j in [x for x in input().split(' ')]:
        matrix[i].append(j)

for i in range(rows - 1):
    for j in range(columns - 1):
        if matrix[i][j] == matrix[i + 1][j] == matrix[i][j + 1] == matrix[i + 1][j + 1]:
            count += 1

print(count)
