from random import choice

print("GAME CODE\n s for Scissors//\tr for Rock//\tp for Paper")
all_option = ["s","r","p"]
chance = 5
s="Scissors"
r="Rock"
p="Paper"
while (True):
    # for i in range(0,chance):
        auto_player = choice(all_option)
        player = str(input("Enter Code:- "))

        if auto_player == player:
            print("Game Tei!")
        elif player == "s":
            if auto_player == "p":
                print("You Win")
            else:
                print(f"You loss", r, "breaks", s)
            break
        elif player == "r":
            if auto_player == "s":
                print("You Win")
            else:
                print(f"You loss", p, "cover","your", r)
            break
        elif player == "p":
            if auto_player == "r":
                print("You Win")
            else:
                print(f"You loss", s, "cut","your", p)
            break
        else:
            print("Enter vadil code")


