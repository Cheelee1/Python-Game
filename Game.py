"""
Aurelio Amparo
20
Program: Game
"""

import pickle
import sys
import random
from MyUtilities import*
from PlayerGenerator import*
import os
from BoardGenerator import*
from CommandPlayer import*
from TreasureGenerator import*
from Combat import*
import time



def Main():
    print("Welcome to King of the Forest!!!")
    time.sleep(2)
    print("Loading content...")
    time.sleep(3)
    ClearScreen()
    while True:
        gameChoice = input("(N)ew Game or (L)oad game?").upper()     
        if gameChoice == "N":                       
            player, board, treasure = NewGame()                     
            break
        elif gameChoice == "L":
            player, board, treasure = LoadGame()
            ShowBoard(board, player)
            break
        else:
            print("Not valid")



    while True:
        userInput = CommandPlayer()
        if userInput == "Q":
            SaveGame(player, board, treasure)
            input("thank you for playing! Game Saved! Press Enter to continue. ")
            sys.exit(0)

        elif userInput == "W":
            board[player["row"]][player["col"]] = "."
            if player["row"] == 0:
                player["row"] = len(board)-1
            else:
                player["row"] -= 1
        
        elif userInput == "A":
            board[player["row"]][player["col"]] = "."
            if player["col"] == 0:
                player["col"] = len(board[0])-1
            else:
                player["col"] -= 1

        elif userInput == "S":
            board[player["row"]][player["col"]] = "."
            if player["row"] == len(board)-1:
                player["row"] = 0
            else:
                player["row"] += 1

        elif userInput == "D":
            board[player["row"]][player["col"]] = "."
            if player["col"] == len(board[0])-1:
                player["col"] = 0
            else:
                player["col"] += 1
        elif userInput == "T":
            if CheckTreasure(player,treasure):
                print("You have found " + treasure["name"] + "!" )
                input("Press Enter to continue your journey.")
                player["treasures"].append(treasure["name"])  # keeps track of treasure names
                treasure = GenTreasure(board)
            ClearScreen()
            ShowBoard(board, player)
            continue                 
            
        elif userInput == "V":
            for i in range(len(player["treasures"])): 
                print(player["treasures"][i])               #  every item in your treasures gets printed
            input("Press Enter to continue: ")
            ClearScreen()
            ShowBoard(board, player)
            continue          
        elif userInput == "K":
            for i in range(len(player["ekia"])):
                print(player["ekia"][i])
            input("Press Enter to continue: ")
            ClearScreen()
            ShowBoard(board, player)
            continue          

        board[player["row"]][player["col"]] = "@"
        chance = diceRoll(1,6)
        if chance == 1:
            enemy = (GenPlayer(1))              # this generates an enemy and changes player["subname"] to enemy["subname"]
            player = CommenceCombat(player, enemy)
        elif chance == 6:
            player = MinorTreasure(player)      #overwrite player stats with new stats
            input("Press Enter to continue your journey.")
        
        ShowBoard(board, player)


Main()