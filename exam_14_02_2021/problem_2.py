import math


def create_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        matrix.append([])
        matrix[i] += [int(symbol) if symbol.isdigit() else symbol for symbol in input().split()]
    return matrix


def player_position(matrix):
    position_p = None
    for i in range(len(matrix)):
        if 'P' in matrix[i]:
            position_p = [i, matrix[i].index('P')]
            break
    return position_p


def up(matrix, position, coins, is_wall, is_out):
    row_index = position[0] - 1
    col_index = position[1]
    if 0 <= row_index < len(matrix) and 0 <= col_index < len(matrix):
        if not matrix[row_index][col_index] == 'X':
            coins += matrix[row_index][col_index]
            position = [row_index, col_index]
            matrix[position[0]][position[1]] = 0
            matrix[row_index][col_index] = 'P'
        else:
            is_wall = True
    else:
        is_out = True
    return matrix, position, coins, is_wall, is_out


def right(matrix, position, coins, is_wall, is_out):
    row_index = position[0]
    col_index = position[1] + 1
    if 0 <= row_index < len(matrix) and 0 <= col_index < len(matrix):
        if not matrix[row_index][col_index] == 'X':
            coins += matrix[row_index][col_index]
            position = [row_index, col_index]
            matrix[position[0]][position[1]] = 0
            matrix[row_index][col_index] = 'P'
        else:
            is_wall = True
    else:
        is_out = True
    return matrix, position, coins, is_wall, is_out


def down(matrix, position, coins, is_wall, is_out):
    row_index = position[0] + 1
    col_index = position[1]
    if 0 <= row_index < len(matrix) and 0 <= col_index < len(matrix):
        if not matrix[row_index][col_index] == 'X':
            coins += matrix[row_index][col_index]
            position = [row_index, col_index]
            matrix[position[0]][position[1]] = 0
            matrix[row_index][col_index] = 'P'
        else:
            is_wall = True
    else:
        is_out = True
    return matrix, position, coins, is_wall, is_out


def left(matrix, position, coins, is_wall, is_out):
    row_index = position[0]
    col_index = position[1] - 1
    if 0 <= row_index < len(matrix) and 0 <= col_index < len(matrix):
        if not matrix[row_index][col_index] == 'X':
            coins += matrix[row_index][col_index]
            position = [row_index, col_index]
            matrix[position[0]][position[1]] = 0
            matrix[row_index][col_index] = 'P'
        else:
            is_wall = True
    else:
        is_out = True
    return matrix, position, coins, is_wall, is_out


n = int(input())
rows = n
columns = n

board = create_matrix(rows, columns)
position_player = player_position(board)
is_wall = False
is_out = False
path = []
coins = 0


while True:
    command = input()
    if not command:
        break
    if command == 'up':
        board, position_player, coins, is_wall, is_out = up(board, position_player, coins, is_wall, is_out)
    elif command == 'right':
        board, position_player, coins, is_wall, is_out = right(board, position_player, coins, is_wall, is_out)
    elif command == 'down':
        board, position_player, coins, is_wall, is_out = down(board, position_player, coins, is_wall, is_out)
    elif command == 'left':
        board, position_player, coins, is_wall, is_out = left(board, position_player, coins, is_wall, is_out)

    if is_wall or is_out:
        break
    path.append(position_player)
    if coins >= 100:
        break

if is_wall or is_out:
    coins = math.floor(coins / 2)
    print(f"Game over! You've collected {coins} coins.")
    print(f"Your path:")
    [print(pos) for pos in path]
else:
    print(f"You won! You've collected {coins} coins.")
    print(f"Your path:")
    [print(pos) for pos in path]
