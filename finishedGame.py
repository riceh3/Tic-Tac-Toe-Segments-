# This is the full game of Tic Tac Toe : all segements uploaded will be
#  - uploaded to this file to run the full game.

# Game Introduction

print("Tic Tac Toe") # <-------- Nathan's mod 1
name = input("Hey whats your name? ") # <-------- Nathan's mod 2

print("Hi there, " + name + " have you played this game before", end="")
confirm = input(" (type Y or N): ") # <-------- Nathan's mod 2

# If selection is yes then the instruction will not be shown, whereas if selection is no then the instructions will be shown


# Instruction Menu

if confirm == "N" or confirm == "n": # <-------- Nathan's mod 4
    print ("\nNot to worry here are the instructions:")
    print(" The Game will ask you to select a box on the grid, where you want to place your 'x' or '0'")
    print(" A guid of the grid will appear at the start of the game")
    print(" You will then enter your 'x' or '0', and it will place the mark")
    print(" The aim of the game, is to get your mark to fill three boxes in a row")

elif confirm == "Y" or confirm == "y": # <-------- Nathan's mod 5
    print("Lets Play")

# Selction of number of players for menu - Hannah
# Leads to 2 player or one player code

players = input("\nHow many players, type 1 or 2 ") # <-------- Nathan's mod 6

if players == "1":
    print("you will now play against the computer")
elif players == "2":
    print("Two players")
if players != "1" and players != "2":
    print("Sorry that is not an option ")
else:
    print("Lets Play")
    
    
print(name + " is player one")

# Game board with reference numebrs
board_Intro = [0,1,2,
         3,4,5,
         6,7,8,
        ]

# Game Board # <-------- Nathan's mod 7
board = [" "," "," ",
         " "," "," ",
         " "," "," ",
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

    

"""~~~~~~~~~~~~~ The Board Function ~~~~~~~~~~~~~""" # <-------- Nathan's mod 8
def grid_Intro(): # board displays reference numbers for each place
    print ('\t\t', board_Intro[0], " │ ", board_Intro[1], " │ ", board_Intro[2])
    print ('\t\t', "━━━━━━━━")
    print ('\t\t', board_Intro[3], " │ ", board_Intro[4], " │ ", board_Intro[5])
    print ('\t\t', "━━━━━━━━")
    print ('\t\t', board_Intro[6], " │ ", board_Intro[7], " │ ", board_Intro[8])

def grid(): # official grid for live game
    print ('\t\t', board[0], " │ ", board[1], " │ ", board[2])
    print ('\t\t', "━━━━━━━━")
    print ('\t\t', board[3], " │ ", board[4], " │ ", board[5])
    print ('\t\t', "━━━━━━━━")
    print ('\t\t', board[6], " │ ", board[7], " │ ", board[8])
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Assigns players there mark 


grid_Intro()

if players == "2":
    print(name + " you are X")
    print("player 2 is O")
elif players == "1":
    print(name + " you are X")
    print("the computer is O")
else:
    print("restart the game")
    

# Turn input and selction ...
while True:

    ex = ("X")
    zero = ("O")

    
    if players == "2": # Nathan: evaluates if the game mode is between two live players, then the following statements are carried out
        print(name + "'s turn")
        playerOne = input("pick a box")
        playerOne = int(playerOne)
        if board[playerOne] != "X" and board[playerOne] != "0":
            board[playerOne] = ex
        else:
            print("\nWhoa, sorry dude. Out of range.\n")
        grid()
        
        print("Player 2 turn")
        playerTwo = input("Pick a box")
        playerTwo = int(playerTwo)
        if board[playerTwo] != "X" and board[playerTwo] != "0":
            board[playerTwo] = zero
        else:
            print("\nPlace is already taken. Try again\n")
        grid()

    elif players == "1": # Nathan: evaluates if the game mode is between one player and the computer, then the following statements are carried out
        print(name + "'s turn")
        playerOne = input(" Pick a box")
        playerOne = int(playerOne)
        if board[playerOne] != "X" and board[playerOne] != "0":
            board[playerOne] = ex
        else:
            print("That box is taken")
        grid()
        
        print("The computers turn")
        computer()
        compTwo = aiPlayer
        compTwo = int(compTwo)
        if board[compTwo] != "X" and board[compTwo] != "0":
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

    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        grid()
        print(oneWins)
    elif board[0] == "O" and board[1] == "O" and board[2] == "O":
        grid()
        print(twoWins)
    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        grid()
        print(oneWins)
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        grid()
        print(twoWins)
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        grid()
        print(oneWins)
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        grid()
        print(twoWins)
    if board[3] == "X" and board[4] == "X" and board[5] == "X":
        grid()
        print(oneWins)
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        grid()
        print(twoWins)
    if board[6] == "X" and board[7] == "X" and board[8] == "X":
        grid()
        print(oneWins)
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        grid()
        print(twoWins)
    if board[1] == "X" and board[4] == "X" and board[7] == "X":
        grid()
        print(oneWins)
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        grid()
        print(twoWins)
    if board[2] == "X" and board[5] == "X" and board[8] == "X":
        grid()
        print(oneWins)
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        grid()
        print(twoWins)


# runs the input choice again if the user has chosen a spot out of the grid range
