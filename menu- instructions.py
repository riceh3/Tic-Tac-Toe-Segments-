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

# Then instructions will only show if the user selects that they have not
# - playerd the game before



    
    
