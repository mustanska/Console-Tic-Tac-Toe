from operator import itemgetter

from colorama import Fore

from validation_functions import is_empty_spaces, is_valid_position
from variables import players, board_positions, SIZE


# A function for draw the board
def draw_board(field):
    for row in field:
        print("| ", end="")
        print(" | ".join([str(el) for el in row]), end="")
        print(" |")


# A function for find the position on board
def position_on_board(position, field):
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == position:
                return row, col


# A function that checks for the winner
def winner_checking(field, current_row, current_col, current_symbol):
    result = list()

    result.append(check_row(field, current_row, current_symbol))
    result.append(check_column(field, current_col, current_symbol))
    result.append(check_primary_diagonal(field, current_symbol))
    result.append(check_secondary_diagonal(field, current_symbol))

    return any(result)


# A function that checks positions (row, column, first and second diagonal
def check_positions(field, row, col, symbol, is_r=False, is_c=False, is_pd=False, is_sd=False):
    count = 0
    indices = []

    while True:
        if field[row][col] == symbol:
            count += 1
            indices.append([row, col])

        if count == 3:
            for r, c in indices:
                field[r][c] = Fore.GREEN + symbol + Fore.RESET
            return True

        if is_r and 0 <= col + 1 < SIZE:
            col += 1

        elif is_c and 0 <= row + 1 < SIZE:
            row += 1

        elif is_pd and (0 <= row + 1 < SIZE and 0 <= col + 1 < SIZE):
            row += 1
            col += 1

        elif is_sd and (0 <= row + 1 < SIZE and 0 <= col - 1 < SIZE):
            row += 1
            col -= 1

        else:
            return False

        if field[row][col] != symbol:
            count = 0
            indices = []


# A function that checks if winner is at the given row
def check_row(field, row, symbol):
    col = 0
    return check_positions(field, row, col, symbol, is_r=True)


# A function that checks if winner is at the given column
def check_column(field, col, symbol):
    row = 0
    return check_positions(field, row, col, symbol, is_c=True)


# A function that checks if winner is at the primary diagonal
def check_primary_diagonal(field, symbol):
    row = 0
    col = 0

    return check_positions(field, row, col, symbol, is_pd=True)


# A function that checks if winner is at the secondary diagonal
def check_secondary_diagonal(field, symbol):
    row = 0
    col = SIZE - 1

    return check_positions(field, row, col, symbol, is_sd=True)


# A function for start the game
def start_game(field):
    is_winner = False

    while is_empty_spaces(field) and not is_winner:
        for name, symbol in players.items():
            position_number = input(f"{name} choose a free position [1-9]: ")

            if not is_valid_position(position_number, board_positions):
                continue

            row, col = position_on_board(position_number, board_positions)
            if field[row][col] != " ":
                print(Fore.RED + "The position is already taken. You missed your turn..." + Fore.RESET)
                continue

            field[row][col] = symbol

            is_winner = winner_checking(field, row, col, symbol)

            draw_board(field)

            if is_winner:
                print(Fore.GREEN + f"The winner is {name}. Congratulation!" + Fore.RESET)
                break

            if not is_empty_spaces(field):
                print(Fore.BLUE + "There is no more empty spaces. The game is over!" + Fore.RESET)
                break
