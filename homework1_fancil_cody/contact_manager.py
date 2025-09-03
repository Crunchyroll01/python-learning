import datetime , sys
x = datetime.datetime.now()
# Global database - this is where ALL contacts are stored
contact_data = {}
def create_contact():
    print("\nCreating a new contact...\n")
    
    # Input and validation for each field
    while True:
        first_name = input("Enter first name: ").strip().capitalize()
        if first_name == "":
            print("First name cannot be empty.")
            continue
        elif first_name.isdigit():
            print("First name cannot be number.")
            continue
        break
    while True:
        last_name = input("Enter last name: ").strip().capitalize()
        if last_name == "":
            print("Last name cannot be empty.")
            continue
        elif last_name.isdigit():
            print("Last name cannot be number.")
            continue
        break
    while True:
        email = input("Enter email: ").strip().capitalize()
        if email == "":
            print("Email cannot be empty.")
            continue
        elif email.isdigit():
            print("Email cannot be only numbers.")
            continue
        break
    while True:
        phone = input("Enter phone number: ")
        if phone == "":
            print("Phone number cannot be empty.")
            continue
        elif phone.isalpha():
            print("Phone number cannot be letters.")
            continue
        break
    while True:
        street = input("Enter street: ").strip().capitalize()
        if street == "":
            print("Street cannot be empty.")
            continue
        elif street.isdigit():
            print("Street cannot be only numbers.")
            continue
        break
    while True:
        city = input("Enter city: ").strip().capitalize()
        if city == "":
            print("City cannot be empty.")
            return create_contact()
        elif city.isdigit():
            print("City cannot be only numbers.")
            return create_contact()
        break
    while True:
        state = input("Enter state: ").strip().capitalize()
        if state == "":
            print("State cannot be empty.")
            return create_contact()
        elif state.isdigit():
            print("State cannot be only numbers.")
            return create_contact()
        break
    while True:
        zip_code = input("Enter zip code: ").strip()
        if zip_code == "":
            print("Zip code cannot be empty.")
            return create_contact()
        elif zip_code.isalpha():
            print("Zip code cannot be letters.")
            return create_contact()
        break
    contact_id = f"contact_{len(contacts_database) + 1}"
    
    # Creating the contact dictionary then returning it
    
    address = {"street": street, 
               "city": city, 
               "state": state, 
               "zip code": zip_code}
    
    contact_data = {"first name": first_name, 
                    "last name": last_name, 
                    "email": email, 
                    "phone": phone, 
                    "address": address,
                    "Timestamp": print(f"Contact created on {x}")
                    }
    return contact_data

# Create a new contact and print the details

contact_data = create_contact()
print(contact_data)

contacts_database = {
    "contact_001": {contact_data},
    "contact_002": {contact_data},
}

def show_contacts():
    print("\n--- All Contacts ---")
    for contact_id, info in contacts_database.items():
        print(f"{contact_id}: {info['first name']} , {info["last name"]} , {info['email']} , {info['phone']} , {info['address']}")
def delete_contact():
    print("\nDeleting a contact...\n")
    contact_id = input("Enter the contact ID to delete (e.g., contact_001): ").strip()
    if contact_id in contacts_database:
        del contacts_database[contact_id]
        print(f"Contact {contact_id} has been deleted.")
    else:
        print(f"Contact ID {contact_id} not found.")

def main_menu():
    
    # Main menu loop
    while True:
        print("\Contact Manager:\n")
        print("1. Add new Contact")
        print("2. Search contacts")
        print("3. List all contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Generate statistics")
        print("7. Find duplicates")
        print("8. Export by category")
        print("9. Exit")
        
        # Get user choice
        choice = int(input("Choose an option (1-4): "))
        
        # Handle user choice
        if choice == 1:
            create_contact()
        elif choice == 2:
            # search_contacts()
            pass
        elif choice == 3:
            show_contacts()
        elif choice == 4:
            # update_contact()
            pass
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            # generate_statistics()
            pass
        elif choice == 7:
            # find_duplicates()
            pass
        elif choice == 8:
            # export_by_category()
            pass
        elif choice == 9:
            print("Exiting the program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.")