from colorama import Fore


# A function that check if the input is valid
def is_valid_input(current_input):
    if current_input and not current_input == " ":
        return True

    print(Fore.RED + "The input is not valid. Try again..." + Fore.RESET)
    return False


# A function that check if the symbol is X or O
def is_valid_symbol(current_input, symbols):
    return current_input in symbols


# A function that check if position is valid
def is_valid_position(current_position, positions):
    for row in range(len(positions)):
        if current_position in positions[row]:
            return True

    print(Fore.RED + "The position is not valid. You missed your turn..." + Fore.RESET)
    return False


# A function that checks for empty space in field
def is_empty_spaces(field):
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == " ":
                return True
    return False


# A function that checks for a unique player name and sign
def is_unique_value(current_value, current_list):
    return current_value not in current_list

