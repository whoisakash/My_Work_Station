import random
chance=3

lower_case = "abcdefghijklmnopqrstuvwxyz"
uper_case = lower_case.upper()
numbers = "0123456789"
symbols = "@#$%&*/\?"

User_for = lower_case + uper_case + numbers + symbols
length_for_pass = 8

print("a = new password, 0 = exit")
while True:
# for i in range(chance):
    # if i < chance:
    #     print("Your free chance over")
    #     break
    inp = input("Enter code:-")
    if inp =="a":
        password = "".join(random.sample(User_for, length_for_pass))
        print("You Password is - ", password)
    elif inp == "0":
        break
    else:
        print("Invalide code")

