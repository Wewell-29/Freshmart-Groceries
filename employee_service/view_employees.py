from employee_service import fetch_all_employees

fetch_all_employees()
import sqlite3

conn = sqlite3.connect("employee_management.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")
employees = cursor.fetchall()

if not employees:
    print("Database is empty.")
else:
    for emp in employees:
        print(emp)

conn.close()