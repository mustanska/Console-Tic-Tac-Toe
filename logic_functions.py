# A function for draw the board
def draw_board(board):
    for row in board:
        print("| ", end="")
        print(" | ".join([str(el) for el in row]), end="")
        print(" |")

