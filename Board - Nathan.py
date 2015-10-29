r1 = ["_", "_", "_"]
r2 = ["_", "_", "_"]
r3 = ["_", "_", "_"]
.
.
.
.
.
.
.
#   Prints the tic-tac-toe grid
    print('')
    print('\t\t', '\t'.join(r1), '\n')  |
    print('\t\t', '\t'.join(r2), '\n')  |----- each list is joined into a one string but each seperation made by '\t' (tab space)
    print('\t\t', '\t'.join(r3), '\n')  |
