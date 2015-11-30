import sys
import random
import socket, select, pickle
from time import sleep
import logging
global a
global b


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
def grid():  
    print ("")
    print ("")
    print ('\t\t', board[0], " │ ", board[1], " │ ", board[2])
    print ('\t\t', "━━━━━━━━")
    print ('\t\t', board[3], " │ ", board[4], " │ ", board[5])
    print ('\t\t', "━━━━━━━━")
    print ('\t\t', board[6], " │ ", board[7], " │ ", board[8])
    print("")



class Connect:
    global secondGo
    global a 

    def __init__(self):
        global a 
        self.playerOneConnect = socket.socket()
        port = 12345
        self.playerOneConnect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.playerOneConnect.bind(('', port))
        self.playerOneConnect.listen(5)

class Connect2:
    global secondGo
    global b

    def __init__(self):
        global b
        self.playerTwoConnect = socket.socket()
        port = 23456
        self.playerTwoConnect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.playerTwoConnect.bind(('', port))
        self.playerTwoConnect.listen(5)


        

                
class FirstGo(Connect):
    global b 
    global a
    global secondGo
    global secondGo2
    global winFirstGo
    global winFirstGo2

    def winFirstGo(self):
        oneWins = ("Player One Wins")
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            grid()
            print(oneWins)
            print("Disconnected")
            sys.exit()
        elif board[3] == "X" and board[4] == "X" and board[5] == "X":
            grid()
            print(oneWins)
            print("Disconnected")
            sys.exit()
        elif board[6] == "X" and board[7] == "X" and board[8] == "X":
            grid()
            print(oneWins)
            print("Disconnected")
            sys.exit()
        elif board[0] == "X" and board[3] == "X" and board[6] == "X":
            grid()
            print(oneWins)
            print("Disconnected")
            sys.exit()
        elif board[1] == "X" and board[4] == "X" and board[7] == "X":
            grid()
            print(oneWins)
            print("Disconnected")
            sys.exit()
        elif board[2] == "X" and board[5] == "X" and board[8] == "X":
            grid()
            print(oneWins)
            print("Disconnected")
            sys.exit()
        elif board[0] == "X" and board[4] == "X" and board[8] == "X":
            grid()
            print(oneWins)
            print("Disconnected")
            sys.exit()
        elif board[2] == "X" and board[4] == "X" and board[6] == "X":
            grid()
            print(oneWins)
            print("Disconnected")
            sys.exit()
            
            
        secondGo2(self)

    def winFirstGo2(self):
        twoWins = ("Player Two Wins")
        if board[0] == "0" and board[1] == "0" and board[2] == "0":
            grid()
            print(twoWins)
            print("Disconnected")
            sys.exit()
        elif board[3] == "0" and board[4] == "0" and board[5] == "0":
            grid()
            print(twoWins)
            print("Disconnected")
            sys.exit()
        elif board[6] == "0" and board[7] == "0" and board[8] == "0":
            grid()
            print(twoWins)
            print("Disconnected")
            sys.exit()
        elif board[0] == "0" and board[3] == "0" and board[6] == "0":
            grid()
            print(twoWins)
            print("Disconnected")
            sys.exit()
        elif board[1] == "0" and board[4] == "0" and board[7] == "0":
            grid()
            print(twoWins)
            print("Disconnected")
            sys.exit()
        elif board[2] == "0" and board[5] == "0" and board[8] == "0":
            grid()
            print(twoWins)
            print("Disconnected")
            sys.exit()
        elif board[0] == "0" and board[4] == "0" and board[8] == "0":
            grid()
            print(twoWins)
            print("Disconnected")
            sys.exit()
        elif board[2] == "0" and board[4] == "0" and board[6] == "0":
            grid()
            print(twoWins)
            print("Disconnected")
            sys.exit()

        secondGo(self)
            
            
            
        

    def secondGo(self):
        global a
        global secondGo2
        global winFirstGo
        global winFirstGo2
        print("Player One Turn", end="-")
        a.send(b'Pick a Box')
        try:
            ex = ("X")
            
            playerOne = a.recv(1024)
            playerOne = playerOne.decode("utf-8").rstrip('\r\n')
            playerOne = int(playerOne)

            if board[playerOne] != "X" and board[playerOne] != "0":
                board[playerOne] = ex
                grid()
                secondGo2(self)
           
            else:
                print("Sorry that box is taken")
        except ValueError:
            ex = ("X")
   
            playerOne = a.recv(1024)
            playerOne = playerOne.decode("utf-8").rstrip('\r\n')
            playerOne = int(playerOne)

            if board[playerOne] != "X" and board[playerOne] != "0":
                board[playerOne] = ex
                grid()
                winFirstGo(self)

           
            else:
                print("Sorry that box is taken")
                
        except KeyboardInterrupt:
            print("Shutdown")
            self.playerOneConnect.shutdown(1)
            self.playerOneConnect.close()
                
    def secondGo2(self):
        global winFirstGo2
        global winFirstGo
        global secondGo
        global b
        print("Player Two Turn")
        b.send(b'Pick a box')
        try:
            zero = ("0")
     
            playerTwo = b.recv(1024)
            playerTwo = playerTwo.decode("utf-8").rstrip('\r\n')
            playerTwo = int(playerTwo)

            if board[playerTwo] != "X" and board[playerTwo] != "0":
                board[playerTwo] = zero
                grid()
                secondGo(self)
            else:
                print("Sorry thats not an option")
                
        except ValueError:
            zero = ("0")

            playerTwo = b.recv(1024)
            playerTwo = playerTwo.decode("utf-8").rstrip('\r\n')
            playerTwo = int(playerTwo)

            if board[playerTwo] != "X" and board[playerTwo] != "0":
                board[playerTwo] = zero
                grid()
                winFirstGo2(self)
            else:
                print("Sorry thats not an option")
                
        except KeyboardInterrupt:
            print("Shutdown")
            self.playerTwoConnect.shutdown(1)
            self.playerTwoConnect.close()
                
            
                
    def __init__(self):
        global winFirstGo2
        global winFirstGo
        global b
        global a
        global secondGo
        global secondGo2
        Connect.__init__(self)
   
        a, addr = self.playerOneConnect.accept()
        print("Connecting")

        a.send(b'Thankyou for connecting')
        print("Player One has Connected")
        print("Connecting")
        
        Connect2.__init__(self)
        b, addr = self.playerTwoConnect.accept()
        
        try:
            ex = ("X")
            print("Player One Turn", end = "-")
            a.send(b'pick a box')

            playerOne = a.recv(1024)
            playerOne = playerOne.decode("utf-8").rstrip('\r\n')
            playerOne = int(playerOne)

            if board[playerOne] != "X" and board[playerOne] != "0":
                board[playerOne] = ex
                grid()
                secondGo2(self)
           
            else:
                print("Sorry that box is taken")
                
        except ValueError:
            ex = ("X")
            print("Player One Turn", end = "-")
            a.send(b'pick a box')

            playerOne = a.recv(1024)
            playerOne = playerOne.decode("utf-8").rstrip('\r\n')
            playerOne = int(playerOne)

            if board[playerOne] != "X" and board[playerOne] != "0":
                board[playerOne] = ex
                grid()
                secondGo2(self)
           
            else:
                print("Sorry that box is taken")
                
        except KeyboardInterrupt:
            print("Shutdown")
            self.playerOneConnect.shutdown(1)
            self.playerOneConnect.close()
            

                
    
  

FirstGo()
                


            
            
        
