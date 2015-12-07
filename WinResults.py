## Module for import congratulatory messages

#Local variables 'asciiArt' in both functions are assigned to lists which
#are prepared for the formatting of the messages as they are displayed in ASCII
#art form

# ASCII text art customised in FIGFont Editor | http://patorjk.com/software/taag/

def WINS():
    """function for displaying message following the name of player 1, if the win conditions are met for player 1"""
    asciiArt = ["██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗      ██╗",
                "██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ███║",
                "██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ╚██║",
                "██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗     ██║",
                "██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║     ██║",
                "╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═╝",
                "                                                         ",
                "        ██╗    ██╗██╗███╗   ██╗███████╗██╗██╗██╗         ",
                "        ██║    ██║██║████╗  ██║██╔════╝██║██║██║         ",
                "        ██║ █╗ ██║██║██╔██╗ ██║███████╗██║██║██║         ",
                "        ██║███╗██║██║██║╚██╗██║╚════██║╚═╝╚═╝╚═╝         ",
                "        ╚███╔███╔╝██║██║ ╚████║███████║██╗██╗██╗         ",
                "         ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝╚═╝╚═╝         "]
    asciiArt[0] = '\n' + asciiArt[0]
    Wins = "\n".join(asciiArt)
    return Wins

def PLAYER2():
    """function for displaying message if the win conditions are met for player 2 or the computer"""
    asciiArt = ["██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗     ██████╗ ",
                "██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██╗",
                "██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝     █████╔╝",
                "██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ██╔═══╝ ",
                "██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║    ███████╗",
                "╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚══════╝",
                "                                                             ",
                "        ██╗    ██╗██╗███╗   ██╗███████╗██╗██╗██╗             ",
                "        ██║    ██║██║████╗  ██║██╔════╝██║██║██║             ",
                "        ██║ █╗ ██║██║██╔██╗ ██║███████╗██║██║██║             ",
                "        ██║███╗██║██║██║╚██╗██║╚════██║╚═╝╚═╝╚═╝             ",
                "        ╚███╔███╔╝██║██║ ╚████║███████║██╗██╗██╗             ",
                "         ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝╚═╝╚═╝             "]
    asciiArt[0] = '\t\t' + asciiArt[0]
    Wins = "\n\t\t".join(asciiArt)
    return Wins
