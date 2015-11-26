"""This is the full game of Tic Tac Toe: all segements uploaded will be uploaded to this file to run the full game."""

##===========================GAME CODE SETUP===================================
import sys
import random
import winsound
from time import sleep

# Introductory game board with reference numebrs
board_Intro = [0,1,2,
               3,4,5,
               6,7,8]

# Official game Board
board = [" "," "," ",
         " "," "," ",
         " "," "," "]

## The Board (Grid) Function
def grid_Intro():
    """Introductory board displaying reference numbers for each place"""
    print ('\t\t', board_Intro[0], " │ ", board_Intro[1], " │ ", board_Intro[2])
    print ('\t\t', "━━━━━━━━")
    print ('\t\t', board_Intro[3], " │ ", board_Intro[4], " │ ", board_Intro[5])
    print ('\t\t', "━━━━━━━━")
    print ('\t\t', board_Intro[6], " │ ", board_Intro[7], " │ ", board_Intro[8])
    print("")

def grid():
    """Official grid for the live game"""
    print ('\t\t', board[0], " │ ", board[1], " │ ", board[2])
    print ('\t\t', "━━━━━━━━")
    print ('\t\t', board[3], " │ ", board[4], " │ ", board[5])
    print ('\t\t', "━━━━━━━━")
    print ('\t\t', board[6], " │ ", board[7], " │ ", board[8])
    print("")

# Ai for one player 
""" This will generate a random number between zero and eight, then be used as player two box"""
global playerTwo
global aiPlayer

def computer():
    global aiPlayer
    ai = [0,1,2,3,4,5,6,7,8]
    aiPlayer = ()
    aiPlayer = random.choice(ai)

##===========================GAME CODE BODY===================================

# Game Introduction

print("Tic Tac Toe")
name = input("Hey whats your name? ")

print("Hi there, " + name + " have you played this game before", end="")
confirm = input(" (type Y or N): ")

# If selection is yes (Y) then the instruction will not be shown, whereas if selection is no (N) then the instructions will be shown

if confirm == "N" or confirm == "n": # <-------- Nathan's mod 4
    #Instruction menu
    print ("\nNot to worry here are the instructions:")
    print(" The Game will ask you to select a box on the grid, where you want to place your 'x' or '0'")
    print(" A guid of the grid will appear at the start of the game")
    print(" You will then enter your 'x' or '0', and it will place the mark")
    print(" The aim of the game, is to get your mark to fill three boxes in a row")

elif confirm == "Y" or confirm == "y": # <-------- Nathan's mod 5
    print("Lets Play")

# Selction of number of players for menu - Hannah
# Leads to 2 player or one player mode
players = input("\nHow many players, type 1 or 2 ") # <-------- Nathan's mod 6
if players == "1":
    print("you will now play against the computer")
elif players == "2":
    print("Two players")
if players != "1" and players != "2":
    print("Sorry that is not an option ")
    winsound.PlaySound("*", winsound.SND_ALIAS)
else:
    print("Lets Play")
    
    
print(name + " is player one")

grid_Intro() #calls function to display introductory board before game starts

# Assigns players their mark 
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

##  execution of the game in TWO PLAYER mode
    if players == "2":
        print(name + "'s turn", end=" - ")
        playerOne = input("Pick a box: ")
        playerOne = int(playerOne)
        if board[playerOne] != "X" and board[playerOne] != "0": # Checks if place is taken
            board[playerOne] = ex
        else:
            print("\nWhoa, sorry dude. Out of range.\n")
            winsound.PlaySound("*", winsound.SND_ALIAS)
        grid()
        
        print("Player 2 turn", end=" - ")
        playerTwo = input("Pick a box: ")
        playerTwo = int(playerTwo)
        if board[playerTwo] != "X" and board[playerTwo] != "0":
            board[playerTwo] = zero
        else:
            print("\nPlace is already taken. Try again\n")
            winsound.PlaySound("*", winsound.SND_ALIAS)
        grid()

##  execution of the game in PLAYER VS COMPUTER mode
    elif players == "1":
        print(name + "'s turn", end=" - ")
        playerOne = input("Pick a box: ")
        playerOne = int(playerOne)
        if board[playerOne] != "X" and board[playerOne] != "0":
            board[playerOne] = ex
            winsound.Beep(32767, 500)
        else:
            print("That box is taken")
            winsound.PlaySound("*", winsound.SND_ALIAS)
            continue
        grid()
        
        print("The computers turn")
        sleep(4) # the delay in seconds before computer takes its turn
        winsound.Beep(32767, 500)
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
        winsound.PlaySound("*", winsound.SND_ALIAS)
        break
    
    else:
        print(" Next go")

##  Win Conditions for "X" inputs
    oneWins = (name + " WINS!")
    twoWins = ("PLAYER TWO WINS")

    if board[0] == "X" and board[1] == "X" and board[2] == "X":     # Horiztonal checks for 'X'
        grid()
        print(oneWins)
        sys.exit()
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        grid()
        print(oneWins)
        sys.exit()
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        grid()
        print(oneWins)
        sys.exit()
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":   # Vertical checks for 'X'
        grid()
        print(oneWins)
        sys.exit()
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        grid()
        print(oneWins)
        sys.exit()
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        grid()
        print(oneWins)
        sys.exit()
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":   # Diagonal checks for 'X'
        grid()
        print(oneWins)
        sys.exit()
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        grid()
        print(oneWins)
        sys.exit()

##  Win Conditions for "0" inputs
    if board[0] == "0" and board[1] == "0" and board[2] == "0":     # Horiztonal checks for 'X'
        grid()
        print(oneWins)
        sys.exit()
    elif board[3] == "0" and board[4] == "0" and board[5] == "0":
        grid()
        print(oneWins)
        sys.exit()
    elif board[6] == "0" and board[7] == "0" and board[8] == "0":
        grid()
        print(oneWins)
        sys.exit()
    elif board[0] == "0" and board[3] == "0" and board[6] == "0":   # Vertical checks for 'X'
        grid()
        print(oneWins)
        sys.exit()
    elif board[1] == "0" and board[4] == "0" and board[7] == "0":
        grid()
        print(oneWins)
        sys.exit()
    elif board[2] == "0" and board[5] == "0" and board[8] == "0":
        grid()
        print(oneWins)
        sys.exit()
    elif board[0] == "0" and board[4] == "0" and board[8] == "0":   # Diagonal checks for 'X'
        grid()
        print(oneWins)
        sys.exit()
    elif board[2] == "0" and board[4] == "0" and board[6] == "0":
        grid()
        print(oneWins)
        sys.exit()

# runs the input choice again if the user has chosen a spot out of the grid range
