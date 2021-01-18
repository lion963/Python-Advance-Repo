rows = int(input())
matrix = []

for i in range(rows):
    matrix.append([])
    matrix[i] += list(map(int, input().split(', ')))

flat_matrix = [num for row in matrix for num in row]
print(flat_matrix)
