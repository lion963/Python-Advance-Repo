import math


def create_matrix(rows, columns):
    matrix = []
    player_position = None
    for i in range(rows):
        matrix.append([])
        matrix[i] += [int(symbol) if symbol.isdigit() else symbol for symbol in input().split()]
        if 'P' in matrix[i]:
            player_position = [i, matrix[i].index('P')]
    return matrix, player_position


def validate(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def check_wall_out(wall, out):
    return wall or out


def check_coins(coins):
    if coins >= 100:
        return True
    return False


def moves(matrix, command, position, coins, is_wall, is_out):
    deltas = {"up": (-1, 0),
              "right": (0, +1),
              "down": (+1, 0),
              "left": (0, -1)}
    row_index = position[0] + deltas[command][0]
    col_index = position[1] + deltas[command][1]
    if validate(row_index, col_index, matrix):
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


def print_result(wall, out, path, coins):
    if wall or out:
        coins = math.floor(coins / 2)
        print(f"Game over! You've collected {coins} coins.")
        print(f"Your path:")
        [print(pos) for pos in path]
    else:
        print(f"You won! You've collected {coins} coins.")
        print(f"Your path:")
        [print(pos) for pos in path]


n = int(input())
rows = n
columns = n

board, position_player = create_matrix(rows, columns)
is_wall = False
is_out = False
path = []
coins = 0

while True:
    command = input()
    board, position_player, coins, is_wall, is_out = moves(board, command, position_player, coins, is_wall, is_out)

    if check_wall_out(is_wall, is_out):
        break

    path.append(position_player)

    if check_coins(coins):
        break

print_result(is_wall, is_out, path, coins)
