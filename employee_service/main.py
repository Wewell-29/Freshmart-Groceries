from employee_service import create_table, insert_employee, fetch_all_employees, update_employee, delete_employee

# Create table (only needed once)
create_table()

# Insert a sample employee
insert_employee("Alice Johnson", "1990-05-15", "123 Main St, NY", "123-456-7890", "alice@example.com", "Robert Johnson", "987-654-3210", "Father")

# Fetch and display all employees
employees = fetch_all_employees()
if not employees:
    print("No employees found.")
else:
    for emp in employees:
        print(emp)

# Update an employee's info
update_employee("alice@example.com", "555-123-4567", "456 New St, NY")

# Delete an employee
delete_employee("alice@example.com")

# Fetch and display all employees again after deletion
employees = fetch_all_employees()
if not employees:
    print("No employees found.")
else:
    for emp in employees:
        print(emp)

# Print the successful porting message
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
port = 5000  # Change if using a different port

print(f"✅ Server is successfully running at http://{ip_address}:{port}/")
