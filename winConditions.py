#Win Conditions

oneWins = (name + " WINS!")
twoWins = ("PLAYER TWO WINS")
if board[0] == "x" and board[1] == "x" and board[2] == "x":
    board()
    print(oneWins)
elif board[0] == "o" and board[1] == "o" and board[2] == "o":
    board()
    print(twoWins)

if board[0] == "x" and board[3] == "x" and board[6] == "x":
    board()
    print(oneWins)
elif board[0] == "o" and board[3] == "o" and board[6] == "o":
    board()
    print(twoWins)

if board[0] == "x" and board[4] == "x" and board[8] == "x":
    board()
    print(oneWins)
elif board[0] == "o" and board[4] == "o" and board[8] == "o":
    board()
    print(twoWins)

if board[3] == "x" and board[4] == "x" and board[5] == "x":
    board()
    print(oneWins)
elif board[3] == "o" and board[4] == "o" and board[5] == "o":
    board()
    print(twoWins)

if board[6] == "x" and board[7] == "x" and board[8] == "x":
    board()
    print(oneWins)
elif board[6] == "o" and board[7] == "o" and board[8] == "o":
    board()
    print(twoWins)

if board[1] == "x" and board[4] == "x" and board[7] == "x":
    board()
    print(oneWins)
elif board[1] == "o" and board[4] == "o" and board[7] == "o":
    board()
    print(twoWins)

if board[2] == "x" and board[5] == "x" and board[8] == "x":
    board()
    print(oneWins)
elif board[2] == "o" and board[5] == "o" and board[8] == "o":
    board()
    print(twoWins)

    board()
    


    


