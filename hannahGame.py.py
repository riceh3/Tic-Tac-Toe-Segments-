# Tic Tac Toe

# Welcome and instruction menu

#Take the user name and then is assigned to player 1 for 1 player or 2 players 
print("Welcome to Team Two Tic-Tac-Toe game")
name = input("Please enter your name")
name = str(name)
print ("Hello " + name)
print (name + " Have you played our game before")
confirm = input("Type yes or no")

# Instructions Menu (only shown if user hasnt played the game before ).

if confirm == "no":
    print("Here are the instructions! ")

    print("The Game will ask you to select a box on the grid, where you want to place your 'x' or '0'")
    print("A guide of the grid will appear at the start of the game")

    print("You will then enter your 'x' or '0', and it will place the mark")

    print("The aim of the game, is to get your mark to fill three boxes in a row")
yes = "yes"
for y in yes:
    if confirm == "yes":
        continue
else:
    print("Lets play")
    
# Input takes to 1 player options or 2 player options

players = input("How many players, type 1 or 2")
if players == "1":
    print("you will now play against the computer")
elif players == "2":
    print("Two players")
else:
    print("Sorry that is not an option")
print(name + " is player 1 ")

# Game Board Boxes 
board = [0,1,2,
         3,4,5,
         6,7,8,
        ]
""" This Function is the AI"""
global playerTwo
import random
def computer():
    import random
    playerTwo = random.randint(0,8)

        
"""This function will display the game board, for the players"""

def show():
    print (board[0], " | ", board[1], " | ", board[2])
    print ("-----------------")
    print (board[3], " | ", board[4], " | ", board[5])
    print ("-----------------")
    print (board[6], " | ", board[7], " | ", board[8])
    
show()

# Which player is what mark 
if players == "2":
    print(name + "you are x")
    print("player 2 is 0")
elif players == "1":
    print(name + " you are x ")
    print("the computer is 0")
else:
    print("restart the game")


while True:
    
#2 players against each other
    
    if players == "2":
        print(name + " turn")
        playerOne = input("Pick a box")
        playerOne = int(playerOne)
        if board[playerOne] != "x" and board[playerOne] != "0":
            board[playerOne] = input("Type your letter")
        else:
            print("That box is taken")
        show()
            
    if players == "2":
        print("Player 2 turn")
        playerTwo = input("Pick a box")
        playerTwo = int(playerTwo)
        if board[playerTwo] != "x" and board[playerTwo] != "0":
            board[playerTwo] = input("Type your letter")
        else:
            print("That box is taken")
        show()
        
#One player against the AI function
        
    if players == "1":
        print(name + " turn")
        playerOne = input("Pick a box")
        playerOne = int(playerOne)
        if board[playerOne] != "x" and board[playerOne] != "0":
            board[playerOne] = input("Type your letter")
        else:
            print("That box is taken")
        show()
        
    if players == "1":
        print("The computers turn")
        computer()
        if board[playerTwo] != "x" and board[playerTwo] != "0":
            board[playerTwo] = input("type 0 ")
        else:
            computer()
            
        show()
                   
    else:
        print(" Next go ")
#Win statements 

    oneWins = (name + " WINS!")
    twoWins = ("PLAYER TWO WINS!")
    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        show()
        print(oneWins)
    elif board[0] == "0" and board[1] == "0" and board[2] == "0":
        show()
        print(twoWins)

    if board[0] == "x" and board[3] == "x" and board[6] == "x":
        show()
        print(oneWins)
    elif board[0] == "0" and board[3] == "0" and board[6] == "0":
        show()
        print(twoWins)

    if board[0] == "x" and board[4] == "x" and board[8] == "x":
        show()
        print(oneWins)
    elif board[0] == "0" and board[4] == "0" and board[8] == "0":
        show()
        print(twoWins)

    if board[3] == "x" and board[4] == "x" and board[5] == "x":
        show()
        print(oneWins)
    elif board[3] == "0" and board[4] == "0" and board[5] == "0":
        show()
        print(twoWins)

    if board[6] == "x" and board[7] == "x" and board[8] == "x":
        show()
        print(oneWins)
    elif board[6] == "0" and board[7] == "0" and board[8] == "0":
        show()
        print(twoWins)

    if board[1] == "x" and board[4] == "x" and board[7] == "x":
        show()
        print(oneWins)
    elif board[1] == "0" and board[4] == "0" and board[7] == "0":
        show()
        print(twoWins)

    if board[2] == "x" and board[5] == "x" and board[8] == "x":
        show()
        print(oneWins)
    elif board[2] == "0" and board[5] == "0" and board[8] == "0":
        show()
        print(twoWins)
    else:
        print("Next players turn")


    show()


        
            
            
        
        
    
    
    
