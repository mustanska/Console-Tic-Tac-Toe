from copy import deepcopy

from variables import board_positions, empty_board
from logic_functions import draw_board, start_game

print("These are the board position numbers you can choose from:")
draw_board(board_positions)

start = input('For start press "Y", For leave press anything else: ').lower()

while start == "y":
    board = deepcopy(empty_board)
    start_game(board)

    start = input('Do you want to RESTART the game (press "Y" for restart or anything else to leave)? ').lower()
else:
    print("Goodbye!")

