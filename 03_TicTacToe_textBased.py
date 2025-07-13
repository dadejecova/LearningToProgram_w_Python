# Using build-in functions.
tictactoe = [[0,0,0],
             [0,0,0],
             [0,0,0]]

# This code initializes a 3x3 Tic Tac Toe board represented as a list of lists.
for row in tictactoe:
    print(row)  # This will print each row of the Tic Tac Toe board.


print(" " * 3)  # This will print a separator line for better readability.

for count, row in enumerate(tictactoe):
    print(count, row)
    for item in row:
        print(item)  # This will print each item in the row of the Tic Tac Toe board.

    
