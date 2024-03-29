# Title: general_functions.py
# Author:   LorisThierryHuetter | leon-jost
# Date: 21.10.2019 | 11:15

from scripts import prologue
import json
import os


def cls():
    os.system('cls')  # to clear screen


def save_game():
    with open("../saves/savegame.json", "w") as savegame_json:
        json.dump(prologue.savegame, savegame_json)


def load_game():
    with open("../saves/savegame.json") as savegame_json:
        prologue.savegame = json.load(savegame_json)
    print("Your characters name is " + prologue.savegame["character_name"])
    pause = input("Paused")
