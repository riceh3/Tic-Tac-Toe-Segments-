"""This is the full game of Tic Tac Toe: all segements uploaded will be uploaded to this file to run the full game."""

##===========================G A M E   C O D E   S E T U P===================================
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

## Board (Grid) Functions
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
    print("") # leaves a gap between game board and next written instruction

# AI for one player

""" This will generate a random number between zero and eight, then be used as player two box"""
global playerTwo
global aiPlayer

def computer():
    global aiPlayer
    ai = [0,1,2,3,4,5,6,7,8]
    aiPlayer = ()
    aiPlayer = random.choice(ai)

##  Win Conditions

def wincheck():
    import winResults as win
    
    oneWins = (name.upper() + win.WINS())
    twoWins = (win.PLAYER2)

    # for "X" inputs
    if board[0] == "X" and board[1] == "X" and board[2] == "X":     # Horiztonal checks for 'X'
        print(oneWins)
        sys.exit()
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        print(oneWins)
        sys.exit()
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        print(oneWins)
        sys.exit()
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":   # Vertical checks for 'X'
        print(oneWins)
        sys.exit()
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        print(oneWins)
        sys.exit()
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        print(oneWins)
        sys.exit()
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":   # Diagonal checks for 'X'
        print(oneWins)
        sys.exit()
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        print(oneWins)
        sys.exit()

##  Win Conditions for "O" inputs
    if board[0] == "O" and board[1] == "O" and board[2] == "O":     # Horiztonal checks for 'O'
        print(twoWins)
        sys.exit()
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        print(twoWins)
        sys.exit()
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        print(twoWins)
        sys.exit()
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":   # Vertical checks for 'O'
        print(twoWins)
        sys.exit()
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        print(twoWins)
        sys.exit()
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        print(twoWins)
        sys.exit()
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":   # Diagonal checks for 'O'
        print(twoWins)
        sys.exit()
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        print(twoWins)
        sys.exit()

##===========================G A M E   C O D E   B O D Y===================================

# Game Introduction
Title = [" ______   __     ______        ",
         "/\__  _\ /\ \   /\  ___\       ",
         "\/_/\ \/ \ \ \  \ \ \____      ",
         "   \ \_\  \ \_\  \ \_____\     ",
         "    \/_/   \/_/   \/_____/     ",
         " ______   ______     ______    ",
         "/\__  _\ /\  __ \   /\  ___\   ",
         "\/_/\ \/ \ \  __ \  \ \ \____  ",
         "   \ \_\  \ \_\ \_\  \ \_____\ ",
         "    \/_/   \/_/\/_/   \/_____/ ",
         " ______   ______     ______    ",
         "/\__  _\ /\  __ \   /\  ___\   ",
         "\/_/\ \/ \ \ \/\ \  \ \  __\   ",
         "   \ \_\  \ \_____\  \ \_____\ ",
         "    \/_/   \/_____/   \/_____/"]

print("\n".join(Title), end="\t")
name = input("Hey whats your name? ")
print("Hi there, " + name + " have you played this game before", end="")
confirm = input(" (type Y or N): ")

# If selection is no (N) the game instructions are shown, otherwise the game begins

if confirm == "N" or confirm == "n": # <-------- Nathan's mod 4
    #Instruction menu
    print ("\nNot to worry here are the instructions:")
    print(" The Game will ask you to select a box on the grid, where you want to place your 'x' or '0'")
    print(" A guid of the grid will appear at the start of the game")
    print(" You will then enter your 'x' or '0', and it will place the mark")
    print(" The aim of the game, is to get your mark to fill three boxes in a row")

elif confirm == "Y" or confirm == "y":
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

grid_Intro() #calls the function to display board with ref. numbers before game starts

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
while True: # to enable repetition of turn-taking between players and reversion for certain stages during the game

    ex = ("X")
    zero = ("O")

##  execution of the game in TWO PLAYER mode
    if players == "2":
        playerOne = int(input(name + "'s turn, pick a box: "))
        if board[playerOne] == "X" or board[playerOne] == "O": # Checks if a spot in the grid is taken
            print("\nPlace is already taken. Try again\n")
            continue                                           # runs the input choice again if the user has chosen a spot already
        elif playerOne > len(board)-1:                         # check if input is our of grid range
            print("\nWhoa, sorry dude. Out of range.\n")
            winsound.PlaySound("*", winsound.SND_ALIAS)            
            continue                                           # runs the input choice again if the user has chosen a spot out of the grid range
        else:
            board[playerOne] = ex
        grid()
        wincheck()
        
        playerTwo = int(input("Player 2 turn, pick a box: "))
        if board[playerTwo] == "X" or board[playerTwo] == "O": # Checks if a spot in the grid is taken
            print("\nPlace is already taken. Try again\n")
            winsound.PlaySound("*", winsound.SND_ALIAS)
            continue                                           # runs the input choice again if the user has chosen a spot already
        elif playerTwo > len(board)-1:                         # check if input is our of grid range
            print("\nWhoa, sorry dude. Out of range.\n")            
            continue                                           # runs the input choice again if the user has chosen a spot out of the grid range
        else:
            board[playerTwo] = zero
        grid()
        wincheck()

##  execution of the game in PLAYER VS COMPUTER mode
    elif players == "1":
        playerOne = int(input(name + "'s turn, pick a box: "))
        try:
            if board[playerOne] == "X" or board[playerOne] == "O":
                print("That box is taken")
                winsound.PlaySound("*", winsound.SND_ALIAS)
                continue
            else:
                board[playerOne] = ex
                winsound.Beep(32767, 500)
        except IndexError:
            print("\nWhoa, sorry dude. Out of range.\n")            
            continue
        grid()
        wincheck()
        
        print("The computers turn")
        sleep(3) # the delay in seconds before computer takes its turn
        winsound.Beep(32767, 500)
        computer()
        compTwo = int(aiPlayer)
        if board[compTwo] != "X" and board[compTwo] != "O":
            board[compTwo] = zero
            grid()
        else:
            computer()
            grid()
        wincheck()

    if players != "1" and players != "2":
        print("Sorry that is not an option")
        winsound.PlaySound("*", winsound.SND_ALIAS)
        break
    else:
        print(" Next go")
