n=5
# p=1
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    # p+=1
    print()


n=6
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=1
    print()
