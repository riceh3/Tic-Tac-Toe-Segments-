"""This is the full game of Tic Tac Toe: all segements uploaded will be uploaded to this file to run the full game."""

##====================================== G A M E   C O D E   S E T U P ===============================================

import sys                               # Allows use to close the system at the end of the game.
import random                            # Used for the AI box selection. 
import socket, select, pickle            # Used for Server. 
from time import sleep                   # Allows time gap between players turns.
global a                                 # Can reference variable a within all functions.
global b                                 # Can reference variable b within all functions.
import winsound                          # Can use built in sounds throughout the game.
global playerTwo                         # Can reference variable playerTwo in all functions
global aiPlayer                          # Can reference variable aiPlayer in all functions
import winResults as win                 # imports module with congratulatory messages



                     # Introductory game board with reference numbers, so the player knows the board layout.
                  

board_Intro = [0,1,2,
               3,4,5,
               6,7,8]

def grid_Intro():                                                                                         # Introductory game board, with reference numbers.
    
    """Introductory board displaying reference numbers for each place"""
    
    print ("")                                                                                            # Allows a gap before the board.
    print ("")    
    print ("")
    print ('\t\t',"              ", board_Intro[0], " │ ", board_Intro[1], " │ ", board_Intro[2])         # Each Line is centered in the middle of the window.
    print ('\t\t',"              ", "━━━━━━━━")
    print ('\t\t',"              ", board_Intro[3], " │ ", board_Intro[4], " │ ", board_Intro[5])
    print ('\t\t',"              ", "━━━━━━━━")
    print ('\t\t',"              ", board_Intro[6], " │ ", board_Intro[7], " │ ", board_Intro[8])
    print("")                                                                                             # Allows a gap at the end of the board.


                                                      # Official game board.

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def grid():
    
    """Official game board, for player input"""
    
    print ("")                                                                                           # Allows a gap before the board.
    print ("")
    print ('\t\t',"              ", board[0], " │ ", board[1], " │ ", board[2])                          # Each line is centered in the middle of the window.
    print ('\t\t',"              ", "━━━━━━━━")
    print ('\t\t',"              ", board[3], " │ ", board[4], " │ ", board[5])
    print ('\t\t',"              ", "━━━━━━━━")
    print ('\t\t',"              ", board[6], " │ ", board[7], " │ ", board[8])                          # Allows a gap at the end of the board.
    print("")                                                                                        



class Connect:

    """Client connection for playerOne"""
        
    
    global secondGo                      # Can reference method secondGo within the class.                      
    global a                             # Can reference variable a in all methods.

    def __init__(self):                  # Initialization that runs each time the class is called.
        
        global a                         # Can reference variable a in all methods.
        
        
        
        self.playerOneConnect = socket.socket()                                                          #  Create Socket for Connection.
        port = 12345                                                                                     #  Port for player one to connect to. 
        self.playerOneConnect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                        #  Address family's for socket, defines the socket type.
        self.playerOneConnect.bind(('', port))                                                           #  Bind the socket to the port. 
        self.playerOneConnect.listen(5)                                                                  #  Wait 5 Seconds for connection response.

class Connect2:

    """Client connection for playerTwo"""
            
        
    global secondGo                      # Can reference method secondGo within the class.
    global b                             # Can reference variable b in all methods.

    def __init__(self):                  # Initialization that runs each time the class is called.
        
        global b                         # Can reference variable b in all methods.
        
        
        self.playerTwoConnect = socket.socket()                                                          # Create socket for Connection.
        port = 23456                                                                                     # Port for player two to connect to.
        self.playerTwoConnect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                        # Address family's for the socket, defines the socket type.
        self.playerTwoConnect.bind(('', port))                                                           # Bind the socket to the port.
        self.playerTwoConnect.listen(5)                                                                  # Wait 5 seconds for the connection response.



class FirstGo(Connect):

    """Two players online, allows connection and turns"""

          
    global b                            # Can reference variable b within the class, (allows messages to be sent and recieved to client)
    global a                            # Can reference variable a within the class, (allows messages to be sent and recieved to client)
    
    global secondGo                     # Can reference method within the class.
    global secondGo2                    # Can reference method within the class.
    
    global winFirstGo                   # Can reference the  player one win conditons method, from all methods within the class.
    global winFirstGo2                  # Can reference the player two win conditions method, from all methods within the class.
    

    def winFirstGo(self):

        """Win conditions for player one online"""
          
        oneWins = win.WINS()                                                        # Display win message for player 1, from imported module.
        
        if board[0] == "X" and board[1] == "X" and board[2] == "X":                 # Row one check.
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player One Wins")
            print(oneWins)                                                          # Win Display.
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.
            
            
        elif board[3] == "X" and board[4] == "X" and board[5] == "X":               # Row two check.
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player One Wins")
            print(oneWins)                                                          # Win Display.
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.
            
            
        elif board[6] == "X" and board[7] == "X" and board[8] == "X":               # Row three check.
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player One Wins")
            print(oneWins)                                                          # Win Display
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.

            
        elif board[0] == "X" and board[3] == "X" and board[6] == "X":               # column one check.
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player One Wins")
            print(oneWins)                                                          # Win Display
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.

            
        elif board[1] == "X" and board[4] == "X" and board[7] == "X":               # column two check.
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player One Wins")
            print(oneWins)                                                          # Win Display
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.
            
            
        elif board[2] == "X" and board[5] == "X" and board[8] == "X":               # column three check.        
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player One Wins")
            print(oneWins)                                                          # Win Display
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.

            
        elif board[0] == "X" and board[4] == "X" and board[8] == "X":               # Diagonal check.
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player One Wins")
            print(oneWins)                                                          # Win Display
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.
            
            
        elif board[2] == "X" and board[4] == "X" and board[6] == "X":               # Diagonal check (other diagonal posibility)
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player One Wins")
            print(oneWins)                                                          # Win Display
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.
            
            
        secondGo2(self)                                                             # If player one hasn't won then player two turn is called.

    def winFirstGo2(self):

        """Win Conditions for player two online"""
        
        twoWins = win.PLAYER2()                                                     # Display win message for player 2, from imported module.
        
        if board[0] == "0" and board[1] == "0" and board[2] == "0":                 # Row one check.
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player Two wins")
            print(twoWins)                                                          # Win Display
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.

            
        elif board[3] == "0" and board[4] == "0" and board[5] == "0":               # Row two check.
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player Two wins")
            print(twoWins)                                                          # Win Display
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.

            
        elif board[6] == "0" and board[7] == "0" and board[8] == "0":               # Row three check.
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player Two wins")
            print(twoWins)                                                          # Win Display.
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.

            
        elif board[0] == "0" and board[3] == "0" and board[6] == "0":               # column one check.
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player Two wins")
            print(twoWins)                                                          # Win Display.
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.
            
            
        elif board[1] == "0" and board[4] == "0" and board[7] == "0":               # column two check.
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player Two wins")
            print(twoWins)                                                          # Win Display.
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.

            
        elif board[2] == "0" and board[5] == "0" and board[8] == "0":               # column three check.
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player Two wins")
            print(twoWins)                                                          # Win Display.
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.
            
        elif board[0] == "0" and board[4] == "0" and board[8] == "0":               # Diagonal check.
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player Two wins")
            print(twoWins)                                                          # Win Display.
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.

            
        elif board[2] == "0" and board[4] == "0" and board[6] == "0":               # Diagonal check (other posibility)
            grid()                                                                  # Displays the grid, to show that the player has won.
            print("\n" + '\t\t' + "              Player Two wins")
            print(twoWins)                                                          # Win Display.
            print("\n" + '\t\t' + "             Disconnected")                      # Tells the players that they are now disconnected.
            sys.exit()                                                              # Exits the game, after they have won.

        secondGo(self)                                                              # If player two hasn't won, it will call player ones turn.
            
            
            
    def secondGo(self):
        
        """Player one turn online"""

        
        global a                                                                   # Variable a can be referenced from Connect class.
        global secondGo2                                                           # Method can be referenced within class.
        global winFirstGo                                                          # Method can be referenced within class.
        global winFirstGo2                                                         # Method can be referenced within class.
        
        print('\t\t' + "               Player One Turn")                           # Each time the method is called, will state player one turn for users.
        a.send(b'Pick a Box')                                                      # Sends a message to player one through client, requesting input.
        
        try:                                                                       # Will attempt to execute code.
            
            ex = ("X")                                                             # Automatically inputs string 'x' when called.
            
            playerOne = a.recv(1024)                                               # Recieves '1024' number of bytes from the connected player.
            playerOne = playerOne.decode("utf-8").rstrip('\r\n')                   # Decodes the input received via the client and erases the start of the string.
            playerOne = int(playerOne)                                             # Change input to int, so can determine which box the player has chosen.
            

            if board[playerOne] != "X" and board[playerOne] != "0":                # Checks that the box chosen is not already taken by either player.
                board[playerOne] = ex                                              # Automatically inputs 'X' without further user input.
                winsound.PlaySound("*", winsound.SND_ALIAS)
                grid()                                                             # Displays the grid, now showing player mark in the box they chose.
                secondGo2(self)                                                    # Will then go to player two turn.
           
            else:                                                                  # If the player cannot pick that box.
                print('\t\t' + "           Sorry that box is taken")               # Tells the user that box is already taken.
                
                
        except ValueError:                                                         # If Value Error occurs, which every turn after the first turn will.
                                                                                   
            ex = ("X")                                                             # Automatically inputs string 'x' when called.
   
            playerOne = a.recv(1024)                                               # Recieves '1024' number of bytes from the connected player.
            playerOne = playerOne.decode("utf-8").rstrip('\r\n')                   # Decodes the input recieved via the client and erases the start of the string.
            playerOne = int(playerOne)                                             # Change input to int, so can determine which box the player has chose.
            

            if board[playerOne] != "X" and board[playerOne] != "0":                # Checks that the box chosen is not already taken by either player.
                board[playerOne] = ex                                              # Automatically inputs 'X' without further user input.
                winsound.PlaySound("*", winsound.SND_ALIAS)
                grid()                                                             # Displays the grid, now showing player mark in the box they chose.
                winFirstGo(self)                                                   # Will then check if the player has won. Calls win conditions for player one.

           
            else:                                                                  # If the player cannot pick that box.
                print('\t\t' + "            Sorry that box is taken")              # Tells the user that box is already taken.
                secondGo2(self)
                
        except KeyboardInterrupt:                                                  # Unless user presses 'ctrl - c' or 'delete'
            print('\t\t' + "            Shutdown")                                 # Tells the user that they have stopped the game.
            
            self.playerOneConnect.shutdown(1)                                      # Will shutdown the connection.
            self.playerOneConnect.close()                                          # Will close the the connection.
            sys.exit()                                                             # Ends the game.
            
                
    def secondGo2(self):
        
        """Player two turn online"""

        
        global winFirstGo2                                                         # Method win confditions for player two can be referenced.
        global winFirstGo                                                          # Method win conditions can be referenced. 
        global secondGo                                                            # Method can be referenced. 
        global b                                                                   # Variable b can be referenced. Used to send messages to player two.

        
        print('\t\t' + "               Player Two Turn")                           # Will show the users that it is player two turn.
        b.send(b'Pick a box')                                                      # Sends a message to player two asking for input, via the client.
        
        try:                                                                       # Will attempt to execute code.  
            
            zero = ("0")                                                           # Variable to automatically enter '0' for player two, when called.
     
            playerTwo = b.recv(1024)                                               # Recieves '1024' bytes from player two input.
            playerTwo = playerTwo.decode("utf-8").rstrip('\r\n')                   # Decode the message from the user.
            playerTwo = int(playerTwo)                                             # Change input to int, so can determine which place on the baord that they chose.
            

            if board[playerTwo] != "X" and board[playerTwo] != "0":                # Checks if box is already taken by either player.
                board[playerTwo] = zero                                            # If the box is free, '0' will be entered in the chosen box.
                winsound.PlaySound("*", winsound.SND_ALIAS)
                grid()                                                             # Display the board, now showing where the player chose. 
                secondGo(self)                                                     # Calls player one turn.
                
                
            else:                                                                  # If the box is taken, or input is wrong, lets the user know.
                print('\t\t' + "         Sorry thats not an option")               # Centered to show under the grid.
                secondGo(self)
                
        except ValueError:                                                         # If Value Error, which will be after players first turn, execute following code.                           
            zero = ("0")                                                           # Variable to automatically enter '0' for player two, when called.    

            playerTwo = b.recv(1024)                                               # Recieves '1024' bytes from player two input.
            playerTwo = playerTwo.decode("utf-8").rstrip('\r\n')                   # Decode the message from the user.
            playerTwo = int(playerTwo)                                             # Change the input to int, so can determine which place on the board that they chose
            

            if board[playerTwo] != "X" and board[playerTwo] != "0":                # Checks if the box is already taken by either place.
                board[playerTwo] = zero                                            # If the box is free, '0' will be entered in the chosen box.
                winsound.PlaySound("*", winsound.SND_ALIAS)
                grid()                                                             # Display the board, now showing where the player chose.
                winFirstGo2(self)                                                  # Checks if player two has won.

                
            else:                                                                  # If the box is taken, or input is wrong, lets the user know.
                print('\t\t' + "         Sorry thats not an option")               # Centered to show under the grid.
                
                
        except KeyboardInterrupt:                                                  # Unless user presses 'ctrl - c' or 'delete'.
            print('\t\t' + "           Shutdown")                                  # Tells the user that game will shutdown.
            
            self.playerTwoConnect.shutdown(1)                                      # Will shutdown the connection.
            self.playerTwoConnect.close()                                          # Will close the connection.
            sys.close()                                                            # The programme will end.               
            
                
    def __init__(self):                                                            # Initialisation, happens when the class is called.

    
        global winFirstGo2                                                         # Method can be referenced.
        global winFirstGo                                                          # Method can be referenced.
        global b                                                                   # Global can be referenced.
        global a                                                                   # Global can be referenced.
        global secondGo                                                            # Method can be referenced.
        global secondGo2                                                           # Method cna be referenced.
        
        Connect.__init__(self)                                                     # Inherit from Connection class, to establish connection to player one.
        
        print('\t\t' + "                 Connecting")                              # Waiting for connection message.
        a, addr = self.playerOneConnect.accept()                                   # Accept the connection from player one and declare variable a.
                                     

        a.send(b'Thankyou for connecting')                                         # Send message via client to player one, confirm connection.
        print('\t\t' + "           Player One has Connected")                      # Shows other user that player one has connected.
        print('\t\t' + "                 Connecting")                              # Waiting for connection from other player message.
        
        Connect2.__init__(self)                                                    # Inherit from Connect2 class, to establish connection to player two.
        b, addr = self.playerTwoConnect.accept()                                   # Accept the connection from player two and declare variable b.
        
        
        try:                                                                       # Attempt to execute code.
            ex = ("X")                                                             # Variable to automatically enter "X", for player one.
            
            print('\t\t' + "               Player One Turn")                       # Shows that it is player one turn.
            a.send(b'pick a box')                                                  # Send message via client to player one, requesting input.

            playerOne = a.recv(1024)                                               # Recieve '1024' bytes of data from player one.
            playerOne = playerOne.decode("utf-8").rstrip('\r\n')                   # Decode the message from the user.
            
            playerOne = int(playerOne)                                             # Convert input to int, can determine which box the player chose.

            if board[playerOne] != "X" and board[playerOne] != "0":                # Checks if box is already taken, by either player.
                board[playerOne] = ex                                              # If box is free, will automatically enter 'X' for player one.
                winsound.PlaySound("*", winsound.SND_ALIAS)
                grid()                                                             # Displays the grid, now showing player one turn, to all users.
                secondGo2(self)                                                    # Calls player two turn.
                
           
            else:                                                                  # If box chosen is taken, by either player, execute following. 
                print('\t\t' + "    Sorry that box is taken")                      # Announces that the box is taken.
                
                
        except ValueError:                                                         # Except Value Error, which will occur after player first go.
            ex = ("X")                                                             # Automatically enters 'X' for player one, when called.
            
            print('\t\t' + "               Player One Turn")                       # Shows that it is player one turn.
            a.send(b'pick a box')                                                  # Send messge to player one via client, requesting input.

            playerOne = a.recv(1024)                                               # Recieve '1024' bytes of data from player one.
            playerOne = playerOne.decode("utf-8").rstrip('\r\n')                   # Decode the message. 
            playerOne = int(playerOne)                                             # Convert input to int, can determine which box the player chose.
            

            if board[playerOne] != "X" and board[playerOne] != "0":                # Checks that box chosen is free.
                board[playerOne] = ex                                              # If box is free, will automatically enter 'X' in chosen box.
                winsound.PlaySound("*", winsound.SND_ALIAS)
                grid()                                                             # Displays the grid, showing where the player chose.
                secondGo2(self)                                                    # Player two turn.
                
           
            else:                                                                  # If box not free, then can't go there.  
                print('\t\t' + "    Sorry that box is taken")                      # Tells the player they can't choose that box.
                
                
        except KeyboardInterrupt:                                                  # Unless user presses 'ctrl - c' or 'delete'.
            
            print('\t\t' + "       Shutdown")                                      # Announces that the programme will now shutdown.
            
            self.playerOneConnect.shutdown(1)                                      # Connection will shutdown.
            self.playerOneConnect.close()                                          # Connection will be closed.
            sys.exit()                                                             # The programme will end.


def onePlayerWin1():
    
    """Win conditions for player one - One-player mode"""
    
    oneWins = win.WINS()                                                           # When called, this will call function from imported module, (win display).
    
    
    if board[0] == "X" and board[1] == "X" and board[2] == "X":                    # Check row one.
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":                  # Check row two.
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":                  # Check row three.
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":                  # Check column one.
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":                  # Check column two.
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":                  # Check column three.
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.  
        sys.exit()                                                                 # The programme ends.
        
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":                  # Diagonal check
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":                  # Diagonal check (other posibility).
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.
        sys.exit()                                                                 # The programme ends.
        
    computerTurn()                                                                 # If player one does not win, the Computers turn is called.
    

def onePlayerWin2():

    """Win conditions for player two - One-player mode"""
    
    twoWins = win.PLAYER2()                                                        # When called function from imported module is shown, (win display).
    
            
    if board[0] == "0" and board[1] == "0" and board[2] == "0":                    # Check row one.
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display.       
        sys.exit()                                                                 # The programme ends.
        
    elif board[3] == "0" and board[4] == "0" and board[5] == "0":                  # Check row two.
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display. 
        sys.exit()                                                                 # The programme ends.
        
    elif board[6] == "0" and board[7] == "0" and board[8] == "0":                  # Check row three.
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[0] == "0" and board[3] == "0" and board[6] == "0":                  # Check column one.
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display. 
        sys.exit()                                                                 # The programme ends.
        
    elif board[1] == "0" and board[4] == "0" and board[7] == "0":                  # Check column two.
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[2] == "0" and board[5] == "0" and board[8] == "0":                  # Check column three.
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[0] == "0" and board[4] == "0" and board[8] == "0":                  # Check diagonal
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[2] == "0" and board[4] == "0" and board[6] == "0":                  # Check diagonal (other posibility).
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display.
        sys.exit()                                                                 # The programme ends.
        
    onePlayer()                                                                    # If player two hasn't won, player one turn.
    

def twoPlayerWin1():

    """Win conditions player one - One player"""
    
    oneWins = win.WINS()                                                           # Win display, from imported module.
    
    if board[0] == "X" and board[1] == "X" and board[2] == "X":                    # Check row one.
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":                  # Check row two.
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":                  # Check row three.
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display. 
        sys.exit()                                                                 # The programme ends.
        
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":                  # Check column one.
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":                  # Check column two.
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display. 
        sys.exit()                                                                 # The programme ends.
        
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":                  # Check column three.
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":                  # Check diagonal.
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.   
        sys.exit()                                                                 # The programme ends.
        
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":                  # Check diagonal (other posibility).
        print("\n" + '\t\t' + "              Player One Wins")
        print(oneWins)                                                             # Shows win display.
        sys.exit()                                                                 # The programme ends.
        
    twoPlayer2()                                                                   # If player one hasn't won, then player two turn.
    

def twoPlayerWin2():

    """Win conditions player two - two players"""
    
    twoWins = win.PLAYER2()                                                        # Win display for player two, from imported module.
            
    if board[0] == "0" and board[1] == "0" and board[2] == "0":                    # Check row one.
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display.  
        sys.exit()                                                                 # The programme ends.
        
    elif board[3] == "0" and board[4] == "0" and board[5] == "0":                  # Check row two.
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[6] == "0" and board[7] == "0" and board[8] == "0":                  # Check row three.
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display. 
        sys.exit()                                                                 # The programme ends.
        
    elif board[0] == "0" and board[3] == "0" and board[6] == "0":                  # Check column one.
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[1] == "0" and board[4] == "0" and board[7] == "0":                  # Check column two.
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[2] == "0" and board[5] == "0" and board[8] == "0":                  # Check column three.
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display. 
        sys.exit()                                                                 # The programme ends.
        
    elif board[0] == "0" and board[4] == "0" and board[8] == "0":                  # Check diagonal.
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display.
        sys.exit()                                                                 # The programme ends.
        
    elif board[2] == "0" and board[4] == "0" and board[6] == "0":                  # Check diagonal (other option).
        print("\n" + '\t\t' + "              Player Two wins")
        print(twoWins)                                                             # Show win display.
        sys.exit()                                                                 # The programme ends.
        
    twoPlayer1()                                                                   # If player two hasn't won, player two turn.
    


    
def title():

    """Displays game time"""
    
    Title = ["                         ______   __     ______        ",
             "                        /\__  _\ /\ \   /\  ___\       ",
             "                        \/_/\ \/ \ \ \  \ \ \____      ",
             "                           \ \_\  \ \_\  \ \_____\     ",
             "                            \/_/   \/_/   \/_____/     ",
             "                         ______   ______     ______    ",
             "                        /\__  _\ /\  __ \   /\  ___\   ",
             "                        \/_/\ \/ \ \  __ \  \ \ \____  ",
             "                           \ \_\  \ \_\ \_\  \ \_____\ ",
             "                            \/_/   \/_/\/_/   \/_____/ ",
             "                         ______   ______     ______    ",
             "                        /\__  _\ /\  __ \   /\  ___\   ",
             "                        \/_/\ \/ \ \ \/\ \  \ \  ___\  ",
             "                           \ \_\  \ \_____\  \ \_____\ ",
             "                            \/_/   \/_____/   \/_____/ ",
             "                                                       ",
             "                                                       ",
             "                                                       "]

    
    print("\n".join(Title), end="\t")                                              # Shows the Title in the centre of the window.

##===========================G A M E   C O D E   B O D Y=============================================================

def start():
    
    """Game Menu"""
    
    title()                                                                                             # Show the title.

    print("\n" + '\t\t' + "       Have you played this game before?", end="")                           # If the user has played this game before, then they can skip- 
    confirm = input("\n" + '\t\t' + "              (type Yes or No)")                                   # - the intructions.

    if confirm == "No" or confirm == "no" or confirm == "n" or confirm == "NO" or confirm == "N":       # Various ways the user can say no.
        
        print("")                                                                                       
        print("INSTRUCTIONS:".center(80))                                       
        print("The Game will ask you to select a box on the grid,".center(80))
        print("where you want to place your 'x' or '0'".center(80))                                     # Game Intructions, centered and space left so title can be- 
        print("A guid of the grid will appear at the start of the game".center(80))                     # - shown.
        print("You will then enter your mark, and it will place the mark".center(80))
        print("The aim of the game, is to get your mark to fill three ".center(80))
        print("boxes in a row".center(80))
        print(" ")
        print(" ")
        print(" ")
        
        playerSelection()                                                                               # After the instructions are read the player can select players
        
    elif confirm == "Yes" or confirm == "yes" or confirm == "y" or confirm == "YES" or confirm == "Y":  # Various ways the user can say yes.
        
        print("\n" + '\t\t' +"                     LETS PLAY")                                          # The user can skip the instructions. 
        print(" ")
        print(" ")
        
        playerSelection()                                                                               # The user can move on to select the number of players.
        
    else:
        
        print("\n" + '\t\t' + "              Sorry that's not an option")                               # Unexpected input - the game continues.
        playerSelection()
        


def playerSelection():

    """The user selects how many player (to set game mode), and starts the game"""
    
    players = input('\t\t' + "  How many players, type 1 or 2, (Type '1' or '2')")                      # Requests user input for number of players.
    
    if players == "1":
        
        print("\n" + '\t\t' + "    You will now play against the computer")
        grid_Intro()                                                                                    # Displays the introduction grid, as a layout.
        
        print("\n" + '\t\t' + "         You are X, the computer is 0")                                  # Assigns the player 'X'.
        onePlayer()                                                                                     # Starts the game.
        
    elif players == "2":
        
        print("\n" + '\t\t' + "       Do you want to play online or offline")                           # Online and Offline option for two players.
        lan = input('\t\t'+ "            (type 'online' or 'offline')")
        
        if lan == "offline" or lan == "Offline" or lan == "OFFLINE" or lan == "off":                    # Various ways the user could input 'offline'.
            grid_Intro()                                                                                # Displays the introduction grid, as a layout.
            
            print("\n" + '\t\t' + "   Decide who is player One and who is player Two")                  # Both players on same computer so they can decide.
            print("\n" + '\t\t' + "              Player One is X")
            print("\n" + '\t\t' + "              Player Two is 0")
            
            twoPlayer1()                                                                                # Starts Game.
            
        elif lan == "online" or lan == "Online" or lan == "on" or lan == "ONLINE":                      # Various ways the user can input 'online'.
            
            print("\n" + '\t\t' + "           The Players will now connect")                            # Connection required to start the game. 
            grid_Intro()                                                                                # Displays the introduction grid, as a layout.
            
            FirstGo()                                                                                   # Starts Game.
            
        else:
            
            print("\n" + '\t\t' + "           Sorry that is not an option")                             # Unexpected Input, will start the function again.
            playerSelection()
            
    elif players != "1" and players != "2":                                                             # Unexpected number of players, will start the function again.
        print("\n" + '\t\t' + "               Sorry that is not an option")
        
        winsound.PlaySound("*", winsound.SND_ALIAS)                                                     # Plays sound before player selection starts again.
        playerSelection()

def twoPlayer1():
    
    """Player One Turn - Two-player mode offline"""
    
    ex = ("X")                                                                                         # Automatically inputs 'X' for player one.
 
    while True:
        
        try:                                                                                           # Attempt to execute code.
            playerOne = int(input("\n" + '\t\t' +"       Player One turn, pick a box: "))              # Requests user input.
            
            if board[playerOne] == "X" or board[playerOne] == "0":                                     # If box is already taken, input is not allowed. 
                print("\n" + '\t\t' + "         Box is already taken.Try again")
                winsound.PlaySound("*", winsound.SND_ALIAS)                                            # Play sound.
                continue
            
            else:                                                                                      # If box is free, then the user input is accepted. 
                board[playerOne] = ex                                                                  # Automatically input 'X' in chosen box.
                
            grid()                                                                                     # Displays grid, showing where the player chose.  
            twoPlayerWin1()                                                                            # Check if player one has won.
            
        except IndexError:                                                                             # If box chosen is out of range, input is not accepted.
            
            print("\n" + '\t\t' + "         Whoa, sorry dude. Out of range")
            winsound.PlaySound("*", winsound.SND_ALIAS)                                                # Plays sound.
            continue

def twoPlayer2():

    """Player two turn - Two-player mode offline"""
    
    zero = ("0")                                                                                       # Automatically enters '0' when called.
    
    while True:
        try:                                                                                           # Attempt to execute the following code.
            
            playerTwo = int(input("\n" + '\t\t' +"       Player 2 turn, pick a box: "))                # Requests user input.
            
            if board[playerTwo] == "X" or board[playerTwo] == "0":                                     # If box is already taken, input not allowed.
                print("\n" + '\t\t' + "     Place is already taken. Try again")
                winsound.PlaySound("*", winsound.SND_ALIAS)                                            # Play sound.
                continue
            
            else:
                board[playerTwo] = zero                                                                # Automatically enter '0' in chosen box.
                
            grid()                                                                                     # Displays grid, showing where the player chose.
            twoPlayerWin2()                                                                            # Checks if player two has won.
            
        except IndexError:                                                                             # If chosen box is out of range, input is not accepted.
            print("\n" + '\t\t' + "        Whoa, sorry dude. Out of range")
            winsound.PlaySound("*", winsound.SND_ALIAS)                                                # Plays sound. 
            continue

def onePlayer():

    """Users One turn - One-player mode"""
    
    ex = ("X")                                                                                         # Automatically enters 'X' when called.
    
    while True:
        try:                                                                                           # Attempt to execute code.
            
            playerOne = int(input("\n" + '\t\t' + "           Your turn, pick a box"))                 # Request user input.
            
            if board[playerOne] == "X" or board[playerOne] == "0":                                     # If box is already taken, input is not allowed.
                print("\n" + "              That box is taken")
                winsound.PlaySound("*", winsound.SND_ALIAS)                                            # Play sound.
                continue
            
            else:
                board[playerOne] = ex                                                                  # Automatically enter 'X' in chosen box.
                winsound.Beep(1767, 500)                                                               # Play sound.
                
        except IndexError:                                                                             # If user is out of range.
            print("\n" + '\t\t' + "          Whoa, sorry dude. Out of range")                  
            continue
        
        grid()                                                                                         # Displays the grid, showing where the player chose.
        onePlayerWin1()                                                                                # Checks if player one has won.            
        
def computerTurn():

    """Computer's turn - One-player mode"""
    
    global aiPlayer                                                       # Allows variable to be reference.
    
    zero = ("0")                                                          # Automatically enters '0', when called.
    ai = [0,1,2,3,4,5,6,7,8]                                              # Range of numbers that the computer can chose between.
    
    aiPlayer = ()            
    aiPlayer = random.choice(ai)                                          # Computer chooses random number from the given list.
    
    while True:
        print("\n" + '\t\t' + "             The Computer's Turn")         # Tells the user that it is the computers turn. 
        sleep(3)                                                          # Allows 3 second gap for the computers turn.
        
        winsound.Beep(1767, 500)                                          # Plays sound.
        compTwo = int(aiPlayer)                                           # Chosen listen element is converted to int, so can be used to pick a box on board.
        
        if board[compTwo] != "X" and board[compTwo] != "0":               # Checks that the box is free.
            board[compTwo] = zero                                         # Automatically enters '0' in the randomly picked box.
            
        grid()                                                            # Show the grid to the user, showing where the computer entered '0'.                                       
        onePlayerWin2()                                                   # Checks if the computer has won.



start()                                                                  # Starts the program, by calling the start menu.  





