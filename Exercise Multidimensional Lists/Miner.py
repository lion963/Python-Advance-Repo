n = int(input())

rows = n
columns = n
matrix = []
coal = 0
count_coal = 0
flag = True

commands = [el for el in input().split()]

for i in range(rows):
    matrix.append([])
    matrix[i] += list(input().split())

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 'c':
            coal += 1
        elif matrix[i][j] == 's':
            index_r = i
            index_c = j

for el in commands:
    if el == 'right':
        try:
            if matrix[index_r][index_c + 1]:
                index_c += 1
        except:
            IndexError
    elif el == 'left':
        try:
            if matrix[index_r][index_c - 1]:
                index_c -= 1
        except:
            IndexError
    elif el == 'up':
        try:
            if matrix[index_r - 1][index_c]:
                index_r -= 1
        except:
            IndexError
    elif el == 'down':
        try:
            if matrix[index_r + 1][index_c]:
                index_r += 1
        except:
            IndexError

    if matrix[index_r][index_c] == 'c':
        count_coal += 1
        matrix[index_r][index_c] = '*'
        if count_coal == coal:
            print(f'You collected all coals! ({index_r}, {index_c})')
            flag = False
            break
    elif matrix[index_r][index_c] == 'e':
        print(f'Game over! ({index_r}, {index_c})')
        flag = False
        break

if flag:
    print(f'{coal - count_coal} coals left. ({index_r}, {index_c})')
