from pyfiglet import figlet_format


def print_matrix(matrix):
    for row in matrix:
        print(row)


def create_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        matrix.append([])
        matrix[i] += [0 for j in range(columns)]
    return matrix


def modify_matrix(col, player, matrix):
    for row in range(len(matrix) - 1, -1, -1):
        if matrix[row][col] == 0:
            matrix[row][col] = player
            return matrix
    return matrix


def validate_column(col, matrix):
    if 0 <= col < len(matrix[0]):
        return True


def print_art(msg, player):
    ascii_art = figlet_format(msg) + figlet_format(player)
    print(ascii_art)


def check_horizontal(matrix, k, l, player):
    if matrix[k][l] == player \
            and matrix[k][l + 1] == player \
            and matrix[k][l + 2] == player \
            and matrix[k][l + 3] == player:
        return True
    elif matrix[k + 1][l] == player \
            and matrix[k + 1][l + 1] == player \
            and matrix[k + 1][l + 2] == player \
            and matrix[k + 1][l + 3] == player:
        return True
    elif matrix[k + 2][l] == player \
            and matrix[k + 2][l + 1] == player \
            and matrix[k + 2][l + 2] == player \
            and matrix[k + 2][l + 3] == player:
        return True
    elif matrix[k + 3][l] == player \
            and matrix[k + 3][l + 1] == player \
            and matrix[k + 3][l + 2] == player \
            and matrix[k + 3][l + 3] == player:
        return True
    return False


def check_vertical(matrix, k, l, player):
    if matrix[k][l] == player \
            and matrix[k + 1][l] == player \
            and matrix[k + 2][l] == player \
            and matrix[k + 3][l] == player:
        return True
    elif matrix[k][l + 1] == player \
            and matrix[k + 1][l + 1] == player \
            and matrix[k + 2][l + 1] == player \
            and matrix[k + 3][l + 1] == player:
        return True
    elif matrix[k][l + 2] == player \
            and matrix[k + 1][l + 2] == player \
            and matrix[k + 2][l + 2] == player \
            and matrix[k + 3][l + 2] == player:
        return True
    elif matrix[k][l + 3] == player \
            and matrix[k + 1][l + 3] == player \
            and matrix[k + 2][l + 3] == player \
            and matrix[k + 3][l + 3] == player:
        return True
    return False


def check_diagonal(matrix, k, l, player):
    if matrix[k][l] == player \
            and matrix[k + 1][l + 1] == player \
            and matrix[k + 2][l + 2] == player \
            and matrix[k + 3][l + 3] == player:
        return True
    elif matrix[k][l + 3] == player \
            and matrix[k + 1][l + 2] == player \
            and matrix[k + 2][l + 1] == player \
            and matrix[k + 3][l] == player:
        return True
    return False


def check_winner(matrix, n):
    player = n
    for k in range(len(matrix) - 3):
        for l in range(len(matrix[0]) - 3):
            if check_horizontal(matrix, k, l, player):
                return True
            elif check_vertical(matrix, k, l, player):
                return True
            elif check_diagonal(matrix, k, l, player):
                return True
    return False


def setup(players, matrix):
    loop = True
    is_winner = False
    while True:
        if is_winner:
            break
        for i in range(1, players + 1):
            while True:
                column = int(input(f'Player {i}, please choose a column:\n'))
                if validate_column(column - 1, matrix):
                    matrix = modify_matrix(column - 1, i, matrix)
                    print_matrix(matrix)
                    break
                else:
                    print(f'Please enter a valid column!')

            if check_winner(matrix, i):
                print(print_art('The winner is palyer: ', str(i)))
                loop = False
                is_winner = True
                break


def main():
    is_winner = False
    matrix = create_matrix(int(input('Please input rows:\n')), int(input('Please input columns:\n')))
    print_matrix(matrix)
    players = int(input('Please enter the number of players\n'))
    loop = True

    while loop:
        loop=setup(players, matrix)

main()