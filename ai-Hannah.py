# Ai for one player - Hannah
""" This will generate a random number between zero and eight, then be used as player two box"""
global playerTwo
import random
def computer():
    import random
    playerTwo = random.randint(0,8)
    

if players == "1":
    print(name + " turn")
    playerOne = input("Pick a box")
    playerOne = int(playerOne)
    if board[playerOne] != "x" and board[playerOne] != "0":
        board[playerOne] = input("type 0")
    else:
        computer()

    board()

if players == "1":
    print("The computers turn")
    computer()
    if board[playerTwo] != "x" and board[playerTwo] != "0":
        board[playerTwo] = input("type 0 ")
    else:
        computer()

    show()

else:
    print(" Next go")

    
