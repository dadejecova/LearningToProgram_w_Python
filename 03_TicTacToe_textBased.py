# Using build-in functions.
tictactoe = [[0,0,0],
             [0,0,0],
             [0,0,0]]


def game_board():
    print (" 0 1 2")
    for count, row in enumerate(tictactoe):
        print(count, row)


game_board()

tictactoe[0][1] = 1

game_board()