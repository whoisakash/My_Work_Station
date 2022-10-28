# i = 1
# while i <= 10:
#     print(i, end=' ')
#     i +=1

# i = 1
# user = int(input("Enter your number : "))
# while i<=10:
#     print(i * user, end=" ")
#     i += 1

num = int(input("Enter your number : "))
count = 5

i = 2

while( i<=num //2):
# while(True):
    if (num % i == 0):
        count +=5
        break

    i +=1

if(count == 5 and num != 1):
    print("Number is prime")

else:
    print("Number is not prime")

# stone paper seccisor