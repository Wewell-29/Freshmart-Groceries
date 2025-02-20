from employee_service import update_employee_contact

email = input("Enter employee email to update: ")
new_phone = input("Enter new phone number: ")
new_address = input("Enter new address: ")

update_employee_contact(email, new_phone, new_address)

print(f"✅ Employee with email {email} updated successfully!")