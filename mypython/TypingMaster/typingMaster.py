import random
word = ("a", "s", "d", "f", "_", "j", "k", "l", ":")
# word = ("asdf","sadf","dasf","fads")
# word = (1,2,3,4,5)
# word1= random.choice(word)
# print(word1)
length = 0
a=50
while (length<251):
    word1 = random.choice(word)
    print(word1,end="")
    if (length % a ==0):
        print("\n")
    length +=1

print()
