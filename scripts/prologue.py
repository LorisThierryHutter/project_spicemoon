# Title: prologue.py
# Author:   LorisThierryHuetter | leon-jost
# Date: 18.10.2019 | 14:04
import atexit
from data import prologue_texts
from scripts import general_functions

# dictionary with all saved data
savegame = {}


def start_new_game():
    print(prologue_texts.prologue_introduction)
    savegame["character_name"] = input("Enter the name of your character: ")
    print("Alright, your characters name will be " + savegame["character_name"] + ".")
    input("Press Enter to confirm.")
    prologue_house()


def prologue_house():
    user_input = int(input(prologue_texts.prologue_1))
    if user_input == 1:
        print(prologue_texts.prologue_1_1)
        print(prologue_texts.prologue_2_1)

    elif user_input == 2:
        print(prologue_texts.prologue_1_2)
        user_input = int(input(prologue_texts.prologue_1_2_1))
        if user_input == 1:
            print(prologue_texts.prologue_1_1)
            print(prologue_texts.prologue_2_1)

        elif user_input == 2:
            print(prologue_texts.prologue_2_2)

    general_functions.save_game()
    input()
