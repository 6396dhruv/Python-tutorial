# snake water gun game
import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
you = input("Enter your choice: ")

yourdict = {"snake": 1, "water": -1, "gun":0}
reversedict = {1:"snake", -1: "water", 0: "gun"}

yourchoice = yourdict[you]

print(f"You choose {reversedict[yourchoice]}\n Computer choose {reversedict[computer]}")

if(computer == yourchoice):
    print("its a draw")
else:
    if(computer == -1 and yourchoice == 1):
        print("you win")
    elif(computer == -1 and yourchoice == 0):
        print("you loose")
    elif(computer == 1 and yourchoice == -1):
        print("you loose")
    elif(computer == 1 and yourchoice == 0):
        print("you win")
    elif(computer == 0 and yourchoice == 1):
        print("you loose")
    elif(computer == 0 and yourchoice == -1):
        print("you win")
    else:
        print("something went wrong")





