rows, columns = map(int, input().split(', '))
# rows, cols = [int(x) for x in input().split(", ")]

matrix = []
sum_matrix = 0

for i in range(rows):
    matrix.append([])
    matrix[i] += list(map(int, input().split(', ')))
    # [int(x) for x in input().split(", ")]

for el in matrix:
    sum_matrix += (sum(el))
print(sum_matrix)
print(matrix)
