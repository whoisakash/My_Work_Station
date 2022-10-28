import sqlite3

conn = sqlite3.connect("company.db")
print("Database Connected")
# change start
cur_sor = "SELECT * FROM EMPLOYEES"
print("ID, NAME, EMAIL, SALARY")
for rows in conn.execute(cur_sor):
    print(rows)

id = input("Enter Id no.: ")
key = input("Enter key: ")
value = input("Enter Vlue: ")
conn.execute(f"UPDATE EMPLOYEES set {key} = '{value}' where id = {id}")

# conn.execute("UPDATE EMPLOYEES set NAME = 'GOPAL' where id = 3")
print("Total changes : ", conn.total_changes)
conn.commit()

# way 2 to get all data as table
cur_sor = "SELECT * FROM EMPLOYEES"
for rows in conn.execute(cur_sor):
    print(rows)

# cursor = conn.execute("SELECT * FROM EMPLOYEES")
#
# for i in cursor:
#     print("ID : ", i[0])
#     print("Name : ", i[1])
#     print("Email : ", i[2])
#     print("Salary : ", i[3], "\n")

conn.close()