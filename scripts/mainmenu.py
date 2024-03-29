# Title:    mainmenu.py
# Author:   LorisThierryHuetter | leon-jost
# Date:     2019.10.18 | 14:00


import sys
import os

sys.path.append(os.getcwd())
from scripts import general_functions
from scripts import prologue
from scripts import errorcodes

# sys.path.insert(0, "\Users\loris.huetter\PycharmProjects\project_spicemoon")


os.system('color 84')  # to change color of background and font (for dramatic effect)


def errorcode01():
    print("Wrong Input. Errorcode 01")
    error = input("Press enter to go back to main menu")
    mainmenu()


def mainmenu():
    general_functions.cls()
    # """
    #   text
    # """
    # this makes a string for multiple lines
    print("""
                                         _____       _           ___  ___                  
                                        /  ___|     (_)          |  \/  |                  
                                        \ `--. _ __  _  ___ ___  | .  . | ___   ___  _ __ 
                                         `--. \ '_ \| |/ __/ _ \ | |\/| |/ _ \ / _ \| '_ \ 
                                        /\__/ / |_) | | (_|  __/ | |  | | (_) | (_) | | | |
                                        \____/| .__/|_|\___\___| \_|  |_/\___/ \___/|_| |_|
                                              | |                                          
                                              |_|                        
                                                
    """)
    print("1)   Start New Game")
    print("2)   Continue Game")
    print("3)   Options")
    print("4)   Credits")
    print("5)   Exit")
    print("")
    x = input("Press number and enter to choose: ")
    x = int(x)

    if x == 1:
        print("Starting game...")
        prologue.start_new_game()
    elif x == 2:
        general_functions.load_game()
    elif x == 3:
        z = input("Starting Options:")
        mainmenu()
    elif x == 4:
        z = input("Made by Loris Thierry Hütter and Leon Jost")
        mainmenu()
    elif x == 5:
        print("Closing Game")
    else:
        errorcodes.errorcode01()


mainmenu()
