# 1 for snake
# -1 for water
# 0 for gun

import random


computer = random.choice([1,-1,0])
youstr = input("Enter 's' for snake, 'w' for water, 'g' for gun: ")
youDict = {"s": 1, "w": -1, "g": 0}

reverseDict = {1 :"snake", -1:"water", 0:"gun"}
you = youDict[youstr]

print(f"Computer chose {reverseDict[computer]}\nYou chose {reverseDict[you]}")

if(computer == you):
    print("It's a tie!")

else:
    if computer == -1 and you == 1:
        print("You WIN!")

    elif computer == -1 and you == 0:
        print("You lose!")

    elif computer == 1 and you == -1:
        print("You lose!")

    elif computer == 1 and you == 0:
        print("You WIN!")

    elif computer == 0 and you == -1:
        print("You WIN!")

    elif computer == 0 and you == 1:
        print("You lose!")

    else:
        print("Something went wrong!")
 

# if((computer - you) == -1 or (computer - you) == 2):
#     print("You lose!")
# elif (computer - you) == 1 or (computer - you) == -2:
#     print("You WIN!")