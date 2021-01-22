rows = 8
columns = 8
matrix = []
queens = []

for i in range(rows):
    matrix.append([])
    matrix[i] += list(input().split())

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 'K':
            r_index = i
            c_index = j

# UP/V
try:
    for row in range(r_index - 1, -1, -1):
        if matrix[row][c_index] == 'Q' and row >= 0:
            queens.append([row, c_index])
            break
except:
    IndexError
# DOWN/V
try:
    for row in range(r_index + 1, rows):
        if matrix[row][c_index] == 'Q' and row >= 0:
            queens.append([row, c_index])
            break
except:
    IndexError
# RIGHT/H
try:
    for col in range(c_index + 1, columns):
        if matrix[r_index][col] == 'Q' and col >= 0:
            queens.append([r_index, col])
            break
except:
    IndexError
# LEFT/H
try:
    for col in range(c_index - 1, -1, -1):
        if matrix[r_index][col] == 'Q' and col >= 0:
            queens.append([r_index, col])
            break
except:
    IndexError
# UP/RIGTH
try:
    col = c_index
    for row in range(r_index - 1, -1, -1):
        col += 1
        if matrix[row][col] == 'Q' and col >= 0 and row >= 0:
            queens.append([row, col])
            break
except:
    IndexError
# DOWN/RIGHT
try:
    col = c_index
    for row in range(r_index + 1, rows):
        col += 1
        if matrix[row][col] == 'Q' and col >= 0 and row >= 0:
            queens.append([row, col])
            break
except:
    IndexError
# UP/LEFT
try:
    col = c_index
    for row in range(r_index - 1, -1, -1):
        col -= 1
        if matrix[row][col] == 'Q' and col >= 0 and row >= 0:
            queens.append([row, col])
            break
except:
    IndexError
# DOWN/LEFT
try:
    col = c_index
    for row in range(r_index + 1, rows):
        col -= 1
        if matrix[row][col] == 'Q' and col >= 0 and row >= 0:
            queens.append([row, col])
            break
except:
    IndexError

if queens:
    print(*queens, sep='\n')
else:
    print(f'The king is safe!')
