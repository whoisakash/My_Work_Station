import sqlite3

conn = sqlite3.connect("company.db")
print("Database Connected")

# * stands for all
# cursor = conn.execute("SELECT * FROM EMPLOYEES")

cur_sor = "SELECT * FROM EMPLOYEES"
for rows in conn.execute(cur_sor):
    print(rows)

# for i in cursor:
#     print("ID : ", i[0])
#     print("Name : ", i[1])
#     print("Email : ", i[2])
#     print("Salary : ", i[3], "\n")


print("Got Data")
conn.close()
