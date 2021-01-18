n, m = map(int, input().split())

rows = n
columns = n
matrix = []

for i in range(rows):
    matrix.append([])
    matrix[i] += list(input().split())

commands = [el for el in input().split()]

