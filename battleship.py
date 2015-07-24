battleship_board = {}

user_input = raw_input('What square would you like to shoot at?')

def battleship(square):
    if battleship_board[square] == 0:
        battleship_board[square] = 1
        return "You've hit a battleship"
    else:
        "You've missed!"

print battleship()
