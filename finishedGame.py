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

# Selction of number of players for menu - Hannah
# Leads to 2 player or one player code

players = input("How many players, type 1 or 2")

if players == "1":
    print("you will now play against the computer")
elif players == "2":
    print("Two players")
else:
    print("Sorry that is not an option ")
    
print(name + " is player one")

# Then instructions will only show if the user selects that they have not
# - playerd the game before

# Game Board - Hannah
board = [0,1,2,
         3,4,5,
         6,7,8,
        ]

# Ai for one player - Hannah
""" This will generate a random number between zero and eight, then be used as player two box"""

global playerTwo
global aiPlayer
import random

def computer():
    global aiPlayer
    import random
    ai = [0,1,2,3,4,5,6,7,8]
    aiPlayer = ()
    aiPlayer = random.choice(ai)

    
        
""" The Board Function"""
def grid():
    print (board[0], " | ", board[1], " | ", board[2])
    print ("--------------- ")
    print (board[3], " | ", board[4], " | ", board[5])
    print ("---------------")
    print (board[6], " | ", board[7], " | ", board[8])

grid()


if players == "2":
    print(name + " you are x")
    print("player 2 is 0")
elif players == "1":
    print(name + " you are x")
    print("the computer is o")
else:
    print("restart the game")

# Ai for one player - Hannah

    
#   The program checks if the specified row and column is out of range,
#   once user input is recieved - Nathan


while True:
    if players == 2:
        print(name + "turn")
        playerOne = input("pick a box")
        playerOne = int(playerOne)
        if board[playerOne] != "x" and board[playerOne] != "0":
            board[playerOne] = input("X or O? ")
        else:
            print("\nWhoa, sorry dude. Out of range.\n")
        grid()
        
        print("Player 2 turn")
        playerTwo = input("Pick a box")
        playerTwo = int(playerTwo)
        if board[playerTwo] != "x" and board[playerTwo] != "0":
            board[playerTwo] = input("x or 0")
        else:
            print("\nPlace is already taken. Try again\n")
        grid()

    elif players == "1":
        print(name + " turn")
        playerOne = input(" Pick a box")
        playerOne = int(playerOne)
        if board[playerOne] != "x" and board[playerOne] != "0":
            board[playerOne] = input(" type your mark")
        else:
            print("That box is taken")
        grid()
        
        print("The computers turn")
        computer()
        compTwo = aiPlayer
        compTwo = int(compTwo)
        if board[compTwo] != "x" and board[compTwo] != "0":
            board[compTwo] = input("type 0")
            grid()
        else:
            computer()
            grid()
    else:
        print(" Next go")
        
#Checks if a place in the game grid has already been filled
#from the last player's turn



# runs the input choice again if the user has chosen a spot out of the grid range



