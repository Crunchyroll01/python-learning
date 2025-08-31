import datetime
x = datetime.datetime.now()
contact_data = {}
def create_contact():
    print("\nCreating a new contact...\n")
    # Input and validation for each field
    first_name = input("Enter first name: ").strip().capitalize()
    if first_name == "":
        print("First name cannot be empty.")
    elif first_name.isdigit():
        print("First name cannot be number.")
        return create_contact()
    
    last_name = input("Enter last name: ").strip().capitalize()
    if last_name == "":
        print("Last name cannot be empty.")
    elif last_name.isdigit():
        print("Last name cannot be number.")
        return create_contact()
    
    email = input("Enter email: ").strip().capitalize()
    if email == "":
        print("Email cannot be empty.")
    elif email.isdigit():
        print("Email cannot be only numbers.")
        return create_contact()
    
    phone = input("Enter phone number: ")
    if phone == "":
        print("Phone number cannot be empty.")
    elif phone.isalpha():
        print("Phone number cannot be letters.")
        return create_contact()

    street = input("Enter street: ").strip().capitalize()
    if street == "":
        print("Street cannot be empty.")
        return create_contact()
    elif street.isdigit():
        print("Street cannot be only numbers.")
        return create_contact()
    
    city = input("Enter city: ").strip().capitalize()
    if city == "":
        print("City cannot be empty.")
        return create_contact()
    elif city.isdigit():
        print("City cannot be only numbers.")
        return create_contact()

    state = input("Enter state: ").strip().capitalize()
    if state == "":
        print("State cannot be empty.")
        return create_contact()
    elif state.isdigit():
        print("State cannot be only numbers.")
        return create_contact()
        
    zip_code = input("Enter zip code: ").strip()
    if zip_code == "":
        print("Zip code cannot be empty.")
        return create_contact()
    elif zip_code.isalpha():
        print("Zip code cannot be letters.")
        return create_contact()
    # Creating the contact dictionary then returning it
    address = {"street": street, "city": city, "state": state, "zip code": zip_code}
    print(f"\nContact created successfully on\n\n{x}")
    contact_data = {"first name": first_name, "last name": last_name, "email": email, "phone": phone, "address": address}
    return contact_data
# Create a new contact and print the details
contact_data = create_contact()
print(contact_data)
"""
def main_menu():
    print("\nMenu:\n")
    print("1. View Contact")
    print("2. New Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Choose an option (1-4): ")
    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please select a valid option.")
        return main_menu()
    elif choice == '1':
        
    return choice
"""