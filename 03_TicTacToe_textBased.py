
# Using build-in functions.
tictactoe = [[0,0,0],
             [0,0,0],
             [0,0,0]]


def game_board(player=0, row=0, column=0, just_print=False):
    print (" 0 1 2")
    if not just_print:
        tictactoe[row][column] = player
    for count, row in enumerate(tictactoe):
        print(count, row)


game_board(just_print=True)
game_board(player=1, row=2, column=1)
'''
tictactoe[0][1] = 1

game_board()
'''