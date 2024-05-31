"""
Aurelio Amparo
2019-11-13
game 5
"""
import random
from MyUtilities import*
from PlayerGenerator import*
import os
from BoardGenerator import*
from CommandPlayer import*

def GenTreasure(board):
    treasure = {}
    treasureName1 = ["flunky","Smelly","Small","Big","Dirty","Shiny","Old","Golden","Dark","Light"]
    treasureName2 = ["Apple","Shield","Sword","Bow","banana","health potion","Pear","Dagger","Spear"]
    postion1 = random.randint(0, len(treasureName1)-1)
    postion2 = random.randint(0, len(treasureName2)-1)
    treasure["name"] = treasureName1[postion1] + " " + treasureName2[postion2]
    treasure["row"] = random.randint(0,len(board)-1)
    treasure["col"] = random.randint(0,len(board[0])-1)
    return treasure

def CheckTreasure(player, treasure):
    if treasure["row"] == player["row"] and treasure["col"] == player["col"]:
        return True
    else:
        return False

def MinorTreasure(player):
    genEvent = ["You have encountered a Wizard.",
    "You have found Magical Mushrooms.",
    "Bowl of RICE!!!",
    "There is a Monk.",
    "You Found the Fountain of Gundam.",
    "There is a Leo...Wait that is your reflection.",
    "Wow! You have found Magical herbs!"]
    event = genEvent[random.randint(0,len(genEvent)-1)]
    upgradeStat = random.randint(1,3)
    if upgradeStat == 1:
       upgrader = diceRoll(2,4)
       statName = "Health"
       player["Health"] += upgrader


    elif upgradeStat == 2:
       upgrader  = diceRoll(1,4)
       statName = "Attack"
       player["Attack"] += upgrader


    elif upgradeStat == 3:
        upgrader = diceRoll(1,4)
        statName = "Defense"
        player["Defense"] += upgrader

    print(event + "Your " + statName + " was increased by "+ str(upgrader) + "!")
    return player

