# find hotel near hirabag, nana varachha for brother
'''make marksheet Grade
Grade : make
A : 85 to 100
B : 70 to 84
C : 55 to 69
F : 0 to 54
if enter mark out of  0 to 100 then  Invalid marks '''

print("'''YOUR GRADE'''")

your_marks = int(input("\nEnter Your Marks :-"))


if your_marks<=100 and your_marks>=85 :
    print("Your Grade:- [A}/Pass")
if your_marks<=84 and your_marks>=70 :
    print("Your Grade:- [B}/Pass")
if your_marks<=69 and your_marks>=55 :
    print("Your Grade:- [C}/Pass")
if your_marks<=54 and your_marks>=0 :
    print("Your Grade:- [F}/Fail")
else:
    print("Enter valid Marks from 0 to 100")