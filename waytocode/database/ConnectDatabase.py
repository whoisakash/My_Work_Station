import sqlite3

conn = sqlite3.connect("company.db")
print("Database Connected")

conn.close()
