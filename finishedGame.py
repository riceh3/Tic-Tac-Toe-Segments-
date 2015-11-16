# This is the full game of Tic Tac Toe : all segements uploaded will be
#  This is the full Game of Tic Tac Toe: all segments  uploaded will be
# - uploaded to this file to run the full game.

# Game Introduction

print(" Tic Tac Toe") # <------- Nathan's mod 1
name = input("Hey whats your name?")# < -------- Nathan's mod 2 

print("Hi there, " + name + " have you played this game before", end = "")
confirm = input("type Y or N")# <------- Nathan's mod 3

# If selection is yes then the instruction will not be shown, whereas if selection is no then the instructions will be shown


# Instruction Menu

if confirm == "N" or confirm == "n":  # <------ Nathan's mod 4
    print ("\nNot to worry here are the instruction:")
    print(" The Game will ask you to select a box on the grid, where you want to place your 'x' or '0'")
    print(" A guid of the grid will appear at the start of the game")
    print(" You will then enter your 'x' or '0', and it will place the mark")
    print("The aim of the game, is to get your mark to fill three boxes in a row")

elif confirm == "Y" or confirm == "y": # <------ Nathan's mod 5 
    print ("Lets Play")

# Selction of number of players for menu - Hannah
# Leads to 2 player or one player code

players = input("\nHow many players, type 1 or 2")# <----- Nathan's mod 6

if players == "1":
    print("you will now play against the computer")
elif players == "2":
    print("Two players")
if players != "1" and players != "2":
    print("Sorry that is not an option ")
else:
    print("Lets Play")
    
    
print(name + " is player one")


# Game Board 
board = [0,1,2,
         3,4,5,
         6,7,8,
        ]

# Ai for one player 
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

    
        
""" ~~~~~~~~~~The Board Function ~~~~~~~~~~~~~ """ # <----- Nathan's mod 
def grid(): # board displays reference numbers for each place
    print ('\t\t', board[0], " | ", board[1], " | ", board[2])
    print ('\t\t', "---------------")
    print ('\t\t', board[3], " | ", board[4], " | ", board[5])
    print ('\t\t', "---------------")
    print ('\t\t', board[6], " | ", board[7], " | ", board[8])

# Assigns players there mark 


if players == "2":
    print(name + " you are x")
    print("player 2 is 0")
elif players == "1":
    print(name + " you are x")
    print("the computer is o")
else:
    print("restart the game")
    

grid()



    

# Turn input and selction ...
while True:

    ex = ("x")
    zero = ("o")

    
    if players == "2": # evaluates if the game mode is between two live players is carried out
        print(name + "'s turn")
        playerOne = input("pick a box")
        playerOne = int(playerOne)
        if board[playerOne] != "x" and board[playerOne] != "0":
            board[playerOne] = ex
        else:
            print("\nWhoa, sorry dude. Out of range.\n")
        grid()
        
        print("Player 2 turn")
        playerTwo = input("Pick a box")
        playerTwo = int(playerTwo)
        if board[playerTwo] != "x" and board[playerTwo] != "0":
            board[playerTwo] = zero
        else:
            print("\nPlace is already taken. Try again\n")
        grid()

    elif players == "1": # evaluates if the game mode is between one player and the computer
        print(name + "'s turn")
        playerOne = input(" Pick a box")
        playerOne = int(playerOne)
        if board[playerOne] != "x" and board[playerOne] != "0":
            board[playerOne] = ex
        else:
            print("That box is taken")
        grid()
        
        print("The computers turn")
        computer()
        compTwo = aiPlayer
        compTwo = int(compTwo)
        if board[compTwo] != "x" and board[compTwo] != "0":
            board[compTwo] = zero
            grid()
        else:
            computer()
            grid()

    if players != "1" and players != "2":
        print("Sorry that is not an option")
        break 
    
    else:
        print(" Next go")

#Win Conditions

    oneWins = (name + " WINS!")
    twoWins = ("PLAYER TWO WINS")

    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        grid()
        print(oneWins)
    elif board[0] == "o" and board[1] == "o" and board[2] == "o":
        grid()
        print(twoWins)
    if board[0] == "x" and board[3] == "x" and board[6] == "x":
        grid()
        print(oneWins)
    elif board[0] == "o" and board[3] == "o" and board[6] == "o":
        grid()
        print(twoWins)
    if board[0] == "x" and board[4] == "x" and board[8] == "x":
        grid()
        print(oneWins)
    elif board[0] == "o" and board[4] == "o" and board[8] == "o":
        grid()
        print(twoWins)
    if board[3] == "x" and board[4] == "x" and board[5] == "x":
        grid()
        print(oneWins)
    elif board[3] == "o" and board[4] == "o" and board[5] == "o":
        grid()
        print(twoWins)
    if board[6] == "x" and board[7] == "x" and board[8] == "x":
        grid()
        print(oneWins)
    elif board[6] == "o" and board[7] == "o" and board[8] == "o":
        grid()
        print(twoWins)
    if board[1] == "x" and board[4] == "x" and board[7] == "x":
        grid()
        print(oneWins)
    elif board[1] == "o" and board[4] == "o" and board[7] == "o":
        grid()
        print(twoWins)
    if board[2] == "x" and board[5] == "x" and board[8] == "x":
        grid()
        print(oneWins)
    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        grid()
        print(twoWins)


    grid()


    



# runs the input choice again if the user has chosen a spot out of the grid range



