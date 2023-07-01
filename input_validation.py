from colorama import Fore
from validation_functions import is_valid_input, is_valid_symbol, is_unique_value


def get_players():
    players = {}
    symbols = ["X", "O"]

    first_player = input("Player 1, what is your name? ")
    while not is_valid_input(first_player):
        first_player = input("Player 1, what is your name? ")

    first_player_symbol = input(f"{first_player} choose X or O: ").upper()
    while not is_valid_symbol(first_player_symbol, symbols):
        print(Fore.RED + "You should write X or O only!" + Fore.RESET)
        first_player_symbol = input("Choose X or O: ").upper()

    symbols.remove(first_player_symbol)
    players[first_player] = first_player_symbol

    second_player = input("Player 2, what is your name? ")
    while True:
        if not is_unique_value(second_player, players):
            print(Fore.RED + "The name is already taken. Please write it again." + Fore.RESET)
        else:
            if is_valid_input(second_player):
                break

        second_player = input("Player 2, what is your name? ")

    players[second_player] = symbols[0]

    return players
