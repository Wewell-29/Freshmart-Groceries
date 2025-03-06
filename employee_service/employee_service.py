from flask import Flask, request, jsonify
from db_connection import connect_db

app = Flask(__name__)

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

@app.route('/employees', methods=['GET'])
def fetch_all_employees():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    conn.close()
    return jsonify(employees)

@app.route('/employee', methods=['POST'])
def insert_employee():
    data = request.json
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO employees (full_name, date_of_birth, address, phone_number, email, emergency_contact_name, emergency_contact_phone, emergency_contact_relationship) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (data['full_name'], data['date_of_birth'], data['address'], data['phone_number'], 
              data['email'], data['emergency_contact_name'], data['emergency_contact_phone'], 
              data['emergency_contact_relationship']))
        conn.commit()
        conn.close()
        return jsonify({"message": "Employee added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/employee/<email>', methods=['DELETE'])
def delete_employee(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE email = ?", (email,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Employee deleted successfully!"})

if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', port=5000, debug=True)
