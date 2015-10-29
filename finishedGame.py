# This is the full game of Tic Tac Toe : all segements uploaded will be
#  - uploaded to this file to run the full game.

# Game Board - Hannah 

board = [0,1,2,
         3,4,5,
         6,7,8,
        ]
""" The Board Function"""
def grid():
    print (board[0], " | ", board[1], " | ", board[2])
    print ("--------------- ")
    print (board[3], " | ", board[4], " | ", board[5])
    print ("---------------")
    print (board[6], " | ", board[7], " | ", board[8])

grid()
    
#   The program checks if the specified row and column is out of range,
#   once user input is recieved - Nathan

while True:
    playerOne = input("Player 1 pick a box")
    playerOne = int(playerOne)
    
# if the row and column specification is within range of the grid
    if board[playerOne] != "x" and board[playerOne] != "0":
        board[playerOne] = input("X or O? ")
    else:
        print("\nWhoa, sorry dude. Out of range.\n")
    grid()
    
#   Checks if a place in the game grid has already been filled
#   from the last player's turn

    playerTwo = input("Player 2 pick a box")
    playerTwo = int(playerTwo)
    
    if board[playerTwo] != "x" and board[playerTwo] != "0":
        board[playerTwo] = input("x or 0")
    else:
        print("\nPlace is already taken. Try again\n")
    grid()

# runs the input choice again if the user has chosen a spot out of the grid range



