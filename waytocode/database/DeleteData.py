import sqlite3

conn = sqlite3.connect("company.db")
print("Database Connected")

conn.execute("DELETE from EMPLOYEES where id = 3")
print("Total changes : ", conn.total_changes)
conn.commit()

cursor = conn.execute("SELECT * FROM EMPLOYEES")

for i in cursor:
    print("ID : ", i[0])
    print("Name : ", i[1])
    print("Email : ", i[2])
    print("Salary : ", i[3], "\n")

conn.close()