"""
Aurelio Amparo
2019-11-11
"""
def CommandPlayer():
    while True:
        buttons = "W,A,S,D,V,T,Q,K".split(",")
        userInput = input("Enter: W, A, S, D, (V)iew Inventory, (T)Check Treasure, (Q)uick Save, (K)ills : ").upper()
        if userInput in buttons:

            break
        else:
            print("Not Valid")
    return userInput


            
