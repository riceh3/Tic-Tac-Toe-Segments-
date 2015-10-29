#   The program checks if the specified row and column is out of range,
#   once user input is recieved
    r = int(input("Row: "))
    c = int(input("Coloumn: "))
    if r <= 3 and c <= 3:
        place = input("X or O? ")
    else:
        print("\nWhoa, sorry dude. Out of range.\n")
        continue

#   Checks if a place in the game grid has already been filled
#   from the last player's turn
    if r == 1:
        if r1[c-1] == "X" or r1[c-1] == "0":
            print("\nPlace is already taken. Try again\n")
            continue
    elif r == 2:
        if r2[c-1] == "X" or r2[c-1] == "0":
            print("\nPlace is already taken. Try again\n")
            continue
    elif r == 3:
        if r3[c-1] == "X" or r3[c-1] == "0":
            print("\nPlace is already taken. Try again\n")
            continue
