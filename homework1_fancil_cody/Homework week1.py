def create_contact():
    print("Creating a new contact...")
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    contact_data = {"name": name, "email": email, "phone": phone}
    return contact_data

create_contact()