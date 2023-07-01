from input_validation import get_players

SIZE = 3

players = get_players()

board_position = [[i + j for j in range(SIZE)] for i in range(1, SIZE * SIZE + 1, 3)]

