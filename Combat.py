"""
Aurelio Amparo
2019-12-03
 Combat
 """
from MyUtilities import*
from PlayerGenerator import*
import time
import sys
def CommenceCombat(player, enemy):
   print("You have encountered a " +enemy["name"]+ "!")
   print("\n")
   while True:   
      playerAttack = random.randint(1,20)
      enemyAttack = random.randint(1,20)
      playerAttackbonus = (player["Attack"])//5
      enemyAttackbonus = (enemy["Attack"])//5
      playerDefensebonus = (player["Defense"])//5
      enemyDefensebonus = (enemy["Defense"])//5

      while True:
         time.sleep(1.5)
         print(enemy["name"] + " stat:")
         print(" Attack: " +str(enemy["Attack"]))
         print(" Defense: " +str(enemy["Defense"]))
         print(" Health: " +str(enemy["Health"]))
         print("\n")
         print(player["name"] + " stat:")
         print(" Attack: " +str(player["Attack"]))
         print(" Defense: " +str(player["Defense"]))
         print(" Health: " +str(player["Health"]))
         userInput = input("What Attack would you like to use? (P)ower Attack, (Q)Quick Attack, (C)ounter Attack, (N)ormal Attack.").upper()
         if userInput == "P":
            (playerAttackbonus)*=2
            (enemyAttackbonus)*=1.5
            ClearScreen()
            break
         elif userInput == "Q":
            (playerAttackbonus)*=2
            (enemyDefensebonus)*=1.5
            ClearScreen()
            break
         elif userInput == "C":
            (playerDefensebonus)*=2.5
            (playerAttackbonus)*=0
            ClearScreen()
            break
         elif userInput == "N":
            (playerAttackbonus)*=1
            (enemyAttackbonus)*=1
            ClearScreen()
            break
         else:
            print("NOPE Try again!")
            time.sleep(1.5)
            ClearScreen()
      playerDamage = playerAttack + playerAttackbonus - enemyDefensebonus - 10
      if playerDamage <= 0:
         time.sleep(1.5)
         print("YOU MISSED NOOB!")
      else:
         time.sleep(1.5)
         print("You have done " +str(playerDamage)+ " damage!")
         enemy["Health"] -= playerDamage
      if enemy["Health"] <= 0:
         break
      enemyDamage = enemyAttack + enemyAttackbonus - playerDefensebonus - 10
      if enemyDamage <= 0:
         time.sleep(1.5)
         print("Enemy is a NOOB! He missed!")
      else:
         time.sleep(1.5)
         print("The enemy F**ked you up and did " +(str(enemyDamage))+ " damage!")
         player["Health"] -= enemyDamage

      if player["Health"] <= 0:
         break
   if player["Health"] <= 0:
      input("Game Over!")
      input("Press Enter to contin...... End your journey.")
      sys.exit(0)
   elif enemy["Health"]<= 0:
      print("You just killed a " +enemy["name"]+ "!")
      player["ekia"].append(enemy["name"])
      input("Press Enter to continue your journey.")
      return player
      

      



         








