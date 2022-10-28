import csv
# with open("schooldata.csv", "w") as csvfile:
filename_csv = input("Enter File")
data = open(filename_csv, "w")
w1 = csv.writer(data)
w1.writerow(["Roll No", "Name", "Marks"])
while True:
    op = int(input("Enter 1 to add, 0 to exit: "))
    if (op == 1):
        rollno = int(input("Enter Roll No:- "))
        name = input("Enter Name:- ")
        marks = int(input("Enter Marks:- "))
        w1.writerow([rollno, name, marks])

    elif (op == 0):
        break

