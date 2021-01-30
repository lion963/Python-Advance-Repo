size = int(input())
rows = size
clumns = size
matrix = []


for i in range(rows):
    matrix.append([])
    matrix[i] += list(map(int, input().split()))

pairs = [tuple(el.split(',')) for el in input().split()]


