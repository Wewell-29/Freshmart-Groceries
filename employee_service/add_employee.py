if __name__ == "__main__":
    full_name = input("Enter Full Name: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    address = input("Enter Address: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    emergency_name = input("Enter Emergency Contact Name: ")
    emergency_phone = input("Enter Emergency Contact Phone: ")
    emergency_relationship = input("Enter Relationship to Employee: ")

    from employee_service import insert_employee
    insert_employee(full_name, dob, address, phone, email, emergency_name, emergency_phone, emergency_relationship)
