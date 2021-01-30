rows = int(input())
matrix = []

for i in range(rows):
    matrix.append([])
    matrix[i] += list(map(int, input().split(', ')))

matrix_even = [[num for num in row if num % 2 == 0] for row in matrix]
print(matrix_even)
