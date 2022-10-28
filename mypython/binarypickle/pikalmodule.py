import pickle
# creat binary file
# f = open ("student.dat", "wb")
# pickle.dump([23,"John",12],f)
# pickle.dump([24,"Tina",13],f)
# f.close()

# code for add "wb" and append "ab"
# with open("file.dat", "wb") as f:
#     while True:
#         op = int(input("1 for add, 0 for quit:-  "))
#         if (op == 1):
#             name = input("Enter name:- ")
#             rollno = int(input("Enter Roll no.:- "))
#             pickle.dump((name,rollno),f)
#         elif (op == 0):
#             break

# code for read and search
# with open("file.dat", "rb") as f:
#     while True:
#         try:
#             row = pickle.load(f)
#             print(row)
#         except EOFError:
#             break

# read specific coloumn
# with open("new.dat", "rb") as f:
#     while True:
#         try:
#             row = pickle.load(f)
#             print(row)
#         except EOFError:
#             break

'''customer.dat contains city, customer, name, amount search
and print all rows where city is delhi'''
# with open("customer.dat","wb") as f:
#     while True:
#         op = int(input("Enter 1 for add , 0 for quit:- "))
#         if (op == 1):
#             city = input("Enter City:- ")
#             cust_name = input("Enter Cust name:- ")
#             amount = int(input("Enter Amount:- "))
#             pickle.dump((city,cust_name,amount),f)
#         elif (op == 0):
#             break

# sum = 0
# with open("customer.dat", "rb") as f:
#     while True:
#         try:
#             row = pickle.load(f)
#             print(row)
#             if row[0].lower() == "delhi":
#                 sum = sum + row[2]
#         except EOFError:
#             break
#     print("Sales in Delhi",sum)

#way 1. copy teh data from "data.dat" to "new.dat" using pickle module
# data1 = open ("customer.dat","rb")
# row = pickle.load(data1)
# f = open("new.dat","wb")
# pickle.dump((row),f)
# f.close()

# row = pickle.load(open("customer.dat","rb"))
# print(row)

#way 2. copy teh data from "data.dat" to "new.dat" using pickle module
# f1 = open("customer.dat","rb")
# f2 = open("new1.dat","wb")
# while True:
#     try:
#         row = pickle.load(f1)
#         pickle.dump(row,f2)
#     except EOFError:
#         break
# f1.close()
# f2.close()

#read new1.dat file
with open("employee.dat","rb") as f:
    while True:
        try:
            row = pickle.load(f)
            print(row)
        except EOFError:
            break

# update file
'''update salary of person with Emp_code as 
E002 to 50000. in a file "employee.dat has employee data in folloing
formate[Emp_cod,Emp_name,Salary]'''
# f1 = open("employee.dat","wb")
# pickle.dump(["E001","Akash",80000],f1)
# pickle.dump(["E002","Manoj",45000],f1)
# pickle.dump(["E003","Nirav",30000],f1)
# f1.close()
#
# with open("employee.dat","rb+") as f:
#     while True:
#         try:
#             record_pos = f.tell()
#             row = pickle.load(f)
#             if (row[0] == "E002"):
#                 row[2] = 50000
#                 f.seek(record_pos,0)
#                 pickle.dump(row,f)
#         except EOFError:
#             break