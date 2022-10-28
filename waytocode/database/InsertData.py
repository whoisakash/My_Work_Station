import sqlite3

conn = sqlite3.connect("company.db")
print("Database Connected")

conn.execute("INSERT INTO EMPLOYEES (ID,NAME,EMAIL,SALARY) \
             VALUES(1,'Akash','akash@test.com',30000)")

conn.execute("INSERT INTO EMPLOYEES (ID,NAME,EMAIL,SALARY) \
             VALUES(2,'Abhishek','abhi@test.com',30000)")

conn.execute("INSERT INTO EMPLOYEES (ID,NAME,EMAIL,SALARY) \
             VALUES(3,'Gautam','gautam@test.com',30000)")

conn.commit()

print("Data Inserted")
conn.close()