# This is the full game of Tic Tac Toe : all segements uploaded will be
#  - uploaded to this file to run the full game.

# Game Menu - Hannah 

print(" Tic Tac Toe")
name = input("Hey whats your name?")

#takes user name and asigns to player one

print("Hi there, " + name + " have you played this game before")
confirm = input("type yes or no")

# Instruction Menu

if confirm == "no":
    print ("Not to worry here are the instruction")

    print(" The Game will ask you to select a box on the grid, where you want to place your 'x' or '0'")
    print(" A guid of the grid will appear at the start of the game")

    print(" You will then enter your 'x' or '0', and it will place the mark")

    print("The aim of the game, is to get your mark to fill three boxes in a row")
yes = "yes"
for y in yes:
    if confirm == "yes":
        continue
else:
    print("Lets Play")

# Then instructions will only show if the user selects that they have not
# - playerd the game before

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



