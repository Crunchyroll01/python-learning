contact_data = {}
def create_contact():
    print("Creating a new contact...")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    contact_data = {"first name": first_name, "last name": last_name, "email": email, "phone": phone}
    return contact_data

contact_data = create_contact()

print(contact_data)