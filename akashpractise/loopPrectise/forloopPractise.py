n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
# c = 6
# for i in range(c):
#     for j in range(c):
#         if (i==0 or i==5) and j in range(0,1):
#             print("  * *  ", end = " ")
#     for j in range(c):
#         if i in range(1,5) and j==0:
#             print("* * * *", end = " ")
#     print()
# print("incrising triangle")
# n=6
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="  ")
#     print()
#
# print("Decreasing triangle")
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*", end="  ")
#     print()
#
#
# # Right side triangle
# n =5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
#
# # dissending 90 degree traiangle
# n=6
# for i in range(n):
#     for j in range(i,n):
#         print("*", end=" ")
#     for j in range(i+1):
#         print(" ",end=" ")
#     print()
#
# print("Diamond box bottom")
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("* ", end=" ")
#     for j in range(i+1):
#         print(" ",end=" ")
#     # for j in range(i+1,n):
#     #     print("+ ",end=" ")
#     # for j in range(i,n):
#     #     print("* ",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print("* ",end=" ")
#     print()

# print("Diamond pattern")
# n = 5
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()

# print(" Peramid")
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
#
# print("Mirror Peramid")
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()
#
# print("sandglass")
# n=7
# for i in range(n-1):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# print("butterfly")
# n=5
# for i in range(n-1):
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
#
#
# n=int(input("Enter the circle length(3<):- "))
# for i in range(n):
#      for j in range(n):
#          if (i==0 or i==(n-1)) and j in range(0,n-(n-1)):
#              print("  *  * ",end=" ")
#      for j in range(n):
#          if i in range(n-(n-1),n-1) and j==0:
#              print(" *    * ",end=" ")
#      print()

# n = int(input("Enter Num : "))
# for i in range(n):
#     for j in range(i+1):
#         # printing stars
#         print(" * ",end=" ")
#     print("\r")

# s = int(input("Enter Square Size: "))
# for i in range(s):
#     print ("*  " * s)

# rec_a = int(input("Enter Length for Rectangle   : "))
# rec_b = int(input("Enter Width for Rectangle   : "))
# for i in range(rec_a):
#     print ("*  " * rec_b)

# n = int(input("Enter Num :-"))
# for i in range(n):
#     for j in range(0, i+1):
#         print("*",end="")
#     print()
# a = 8, 10,
# b = 5, 6 ,
# b = int(input("Enter Num :-"))

# b = 8
# a = 1
# for i in range(0, b):
#     for j in range(0, a):
#         print("* ", end="")
#     a = a + 1
#     for j in range(0, i+1):
#         print(end=" ")
#     print()

# right side 90 degree Triangle [done]
# b_line = int(input("Enter the length Steps Number :- "))
# a_start = int(input("Enter the Start pattern Number :- "))
# for i in range(0, b_line):
#     for j in range(0, a_start):
#         print("* ", end="")
#     a_start = a_start + 1
#     print()

# piramid star pattern [Done]
# b = 7
# a = 12
# for i in range(0, b):
#     for j in range(0, a):
#         print(end=" ")
#     a = a - 2
#     for j in range(0, i+1):
#         print(" * ", end=" ")
#     print()

# lesson of pattern >>>
# square pattern
# n=5
# for i in range(n):
#     for j in range(n):
#         print("* ", end="  ")
#     print()

#

# s=10
# for i in range(s):
#     for j in range(s):
#         print("* ", end=" ")
#     print()

