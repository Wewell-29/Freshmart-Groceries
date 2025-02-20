from employee_service import delete_employee

email = input("Enter Employee Email to delete: ")

delete_employee(email)
print("✅ Employee deleted successfully!")
