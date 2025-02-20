from employee_service import *

create_table()

# Insert an employee
insert_employee("Alice Johnson", "1990-05-15", "123 Main St, NY", "123-456-7890", "alice@example.com", "Robert Johnson", "987-654-3210", "Father")

# Fetch all employees
fetch_all_employees()

# Update employee contact details
update_employee_contact("alice@example.com", "555-123-4567", "456 New Ave, LA")

# Delete an employee
delete_employee("alice@example.com")
