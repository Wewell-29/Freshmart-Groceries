from db_connection import connect_db

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            address TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            emergency_contact_name TEXT NOT NULL,
            emergency_contact_phone TEXT NOT NULL,
            emergency_contact_relationship TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_employee(full_name, dob, address, phone, email, emergency_name, emergency_phone, emergency_relationship):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO employees (full_name, date_of_birth, address, phone_number, email, emergency_contact_name, emergency_contact_phone, emergency_contact_relationship) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (full_name, dob, address, phone, email, emergency_name, emergency_phone, emergency_relationship))
        conn.commit()
        print("✅ Employee added successfully!")
    except sqlite3.IntegrityError:
        print("❌ Error: Email already exists!")
    conn.close()

def fetch_all_employees():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    conn.close()
    return employees  # Ensure this returns data

from employee_service import fetch_all_employees

employees = fetch_all_employees()

if not employees:
    print("No employees found.")
else:
    for emp in employees:
        print(emp)  # Ensure output is printed


def update_employee(email, new_phone, new_address):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM employees WHERE email = ?", (email,))
    employee = cursor.fetchone()

    if employee:  # If employee exists, update the info
        cursor.execute("""
            UPDATE employees 
            SET phone_number = ?, address = ? 
            WHERE email = ?
        """, (new_phone, new_address, email))
        
        conn.commit()
        print("✅ Update successful!")
    else:
        print("❌ Error: Employee not found!")

    conn.close()


def delete_employee(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE email = ?", (email,))
    conn.commit()
    conn.close()