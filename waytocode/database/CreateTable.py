import sqlite3


conn = sqlite3.connect("company.db")
print("Database Connected")

conn.execute('''CREATE TABLE EMPLOYEES
(ID INT PRIMARY KEY NOT NULL, 
NAME TEXT NOT NULL,
EMAIL TEXT NOT NULL,
SALARY REAL NOT NULL)''')

print("Table Created")

conn.close()
