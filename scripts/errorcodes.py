# Title:    errorcodes.py
# Author:   LorisThierryHuetter | leon-jost
# Date:     2019.10.22 | 09:12


from scripts import mainmenu


def errorcode01():
    print("Wrong Input. Errorcode 01")
    error = input("Press enter to go back to main menu")
    mainmenu.mainmenu()