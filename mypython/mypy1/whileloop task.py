# import random
#
# # Snake, water, gun
# all_optn = ["s","w","g"]
#
# while True:
#     auto_plr = random.choice(all_optn)
#     player1 = str(input("Enter code:- "))
#
#     if auto_plr == player1:
#         print("Both Same")
#     elif player1 == "s":
#         if auto_plr == "w":
#             print("Snake drink water, You WIN!")
#         else:
#             print("Gun kill Snake, You loss!")
#         break
#     elif player1 == "w":
#         if auto_plr == "g":
#             print("Gun can't shoot Water , You WIN!")
#         else:
#             print("Snake drink water, You loss!")
#         break
#     elif player1 == "g":
#         if auto_plr == "s":
#             print("Gun kill Snake , You WIN!")
#         else:
#             print("Gun can't shoot water, You loss!")
#         break
#     else:
#         print("Enter valid code")
#
# # create a list of play options
# t = ["Rock", "Paper", "Scissors"]
#
# # assign a random play to the computer
# computer = t[randint(1, 3)]
#
# # set player to False
# player = False
#
# while player == False:
#     # set player to True
#     player = input("Rock, Paper, Scissors?")
#     if player == computer:
#         print("Tie!")
#     elif player == "Rock":
#         if computer == "Paper":
#             print("You lose!", computer, "covers", player)
#         else:
#             print("You win!", player, "smashes", computer)
#     elif player == "Paper":
#         if computer == "Scissors":
#             print("You lose!", computer, "cut", player)
#         else:
#             print("You win!", player, "covers", computer)
#     elif player == "Scissors":
#         if computer == "Rock":
#             print("You lose...", computer, "smashes", player)
#         else:
#             print("You win!", player, "cut", computer)
#     else:
#         print("That's not a valid play. Check your spelling!")
#     # player was set to True, but we want it to be False so the loop continues
#     # player = False
#     # computer = t[randint(1, 3)]

def calc(num):
    val=1
    for i in range(1,num+1):
        print(val,"*",i,"=",val*i)
        val = val * i
    return val
num=5

print(calc(num))