import random
import string
LETTERS = string.ascii_letters
NUMS = "01234568789"
SPE = "-+*%&$!"
SYMBOLS = LETTERS + NUMS + SPE
Len = int(input("ENTEER PASS. LENGTH: "))

i= 0
while i<5:
    password = "".join(random.sample(SYMBOLS, Len))
    print(password)
    i += 1
print()
