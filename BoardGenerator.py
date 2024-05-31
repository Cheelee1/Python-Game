""" 
Aurelio Amparo 
2019-10-30
Game 3
"""
import random
from PlayerGenerator import*

def CreateBoard(row,col):
    board = []                        # board is an empty list
    for i in range(row):                # for i in range of row Input
        board.append([])                    # create a list in board
        for j in range(col):                     # for j in range of col input take board[i] and put a "." in every postion
            board[i].append(".")
    return board



def ShowBoard(board, player):
    ClearScreen()
    for i in board:                     # for every list inside board =[]
        print(" ".join(i))              # prints each list on a seperate line.
    print("Health: " + str(player["Health"]))
    print("Attack: " + str(player["Attack"]))
    print("Defense: " + str(player["Defense"]))
    


def PlacePlayer(board,player): 
    player["row"] = random.randint(0,len(board)-1)      
    player["col"] = random.randint(0,len(board[0])-1)
    board[player["row"]][player["col"]] = "@"
    return board,player

