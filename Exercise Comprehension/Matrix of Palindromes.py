alphabet = 'abcdefghijklmnopqrstuvwxyz'
rows, columns = [int(num) for num in input().split()]
matrix = [[alphabet[i] + alphabet[i + j] + alphabet[i] for j in range(columns)] for i in range(rows)]
[print(*row, sep=' ') for row in matrix]
