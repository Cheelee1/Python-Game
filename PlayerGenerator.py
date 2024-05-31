"""
Name: Aurelio Amparo
Date: 2019-10-09
"""
from MyUtilities import*
import random
import time
def GenName():
    FirstSyllable =["Andrew","Jack","Leo","Lele","Jorge","Dwight","Jim","John","Hyde","Lemon"]           # List of syllables to create a random name
    SecondSyllable = "Titanborn Frost Amparo Malone Shrute Halpert Micheal Casto Lime".split()
    postion1 = random.randint(0, len(FirstSyllable)-1)      
    postion2 = random.randint(0, len(SecondSyllable)-1)
    name = FirstSyllable[postion1] +" "+ SecondSyllable[postion2]                                       # takes the random postion of the syllables Lists and creates a name 
    #random.randint(0, len(firstsyllable)-1)
    return name



def GenHistory():
    Background =["Both of my parents died in an accident when i was 12 years old.",            # Same as nameGen just for history
    "I was left in front of an orphanage by my dying mother after a fatal drug deal.",
    "I saw my own mom take her life and I was mentally abused by my strict drunk father.",
    "After losing my whole family i have devoted my life to find out who killed them...",
    "After suffering a life changing accident i dont feel any pain."]
    Job =["Janitor",
    "Drug Dealer",
    "Undercover Cop",
    "Assassin",
    "Unknown"]
    Back1 = random.randint(0, len(Background)-1)
    Back2 = random.randint(0, len(Job)-1)   
    BackStory = ("BackGround: ") +str(Background[Back1])+"\nJob: " +str(Job[Back2])
    return BackStory



def GenPlayer(level):
    player = {}            
    player["ekia"] = []                                       # this function starts off by making a dictionary.
    player["treasures"] = []
    player["row"] = 0
    player["col"] = 0                                         # player["subname"] is defined
    player["name"] = GenName()
    player["History"] = GenHistory()
    player["Attack"] = diceRoll(3,6) + diceRoll(level,4)      # diceRoll function comes in and 
    player["Defense"] = diceRoll(3,6) + diceRoll(level,4)
    player["Health"] = diceRoll(5,6) + diceRoll(level,4)
    return player

    
def PlayerGeneration():  
    while True:
        os.system("cls")
        userInput = input("Enter a level: ")
        while userInput.isdigit() == False:                    # while userInput is a number anything but a number will be "Not Valid"
            print("Not valid")
            userInput = input("Enter a level: ")               #prompts user again
        userInput = int(userInput)
        level = userInput                                      # Genplayer(level) is assigned to userInput
        player = GenPlayer(level)
        ClearScreen()
        
        while True:   
            print("Name: " +player["name"]) 
            print(player["History"])
            print("Attack: " +str(player["Attack"]))
            print("Defense: " +str(player["Defense"]))
            print("Health: " +str(player["Health"]))
            userInput = input("Do you like your Character: (Y)es or (N)o? ").upper()
            if userInput == "Y":
                return player
                ClearScreen()
                break
            elif userInput == "N":
                ClearScreen()
                player = GenPlayer(level)
                continue
            else: 
                print("Not valid")
                time.sleep(1.5)
                ClearScreen()
                continue
            

            