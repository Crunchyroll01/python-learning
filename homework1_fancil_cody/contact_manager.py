import datetime , sys, os
# Global database - this is where ALL contacts are stored
contact_data = {}
#Initializing variables
address = {}
first_name = ""
last_name = ""
email = ""
phone = ""
# clear screen helps me to keep program clean by clearing previous outputs
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def create_contact():
    print("\nCreating a new contact...\n")
    
    # Input and validation for each field
    while True:
        first_name = input("Enter first name: ").strip().capitalize()
        if first_name == "":
            print("First name cannot be empty.")
            continue
        elif first_name.isdigit():
            #checks if input is only numbers
            print("First name cannot be number.")
            continue
        break
    clear_screen()
    while True:
        last_name = input("Enter last name: ").strip().capitalize()
        if last_name == "":
            print("Last name cannot be empty.")
            continue
        elif last_name.isdigit():
            print("Last name cannot be number.")
            continue
        break
    clear_screen()
    while True:
        # Strip and capitalize trims whitespace and capitalizes first letter
        email = input("Enter email: ").strip().capitalize()
        if email == "":
            print("Email cannot be empty.")
            continue
        elif "@" not in email or "." not in email:
            print("Email must contain '@' and '.'")
            continue
        elif email.isdigit():
            print("Email cannot be only numbers.")
            continue
        break
    clear_screen()
    while True:
        phone = input("Enter phone number: ")
        if phone == "":
            print("Phone number cannot be empty.")
            continue
        elif phone.isalpha():
            #checks if input is only letters
            print("Phone number cannot be letters.")
            continue
        break
    clear_screen()
    while True:
        street = input("Enter street: ").strip().capitalize()
        if street == "":
            print("Street cannot be empty.")
            continue
        elif street.isdigit():
            print("Street cannot be only numbers.")
            continue
        break
    clear_screen()
    while True:
        city = input("Enter city: ").strip().capitalize()
        if city == "":
            print("City cannot be empty.")
            continue
        elif city.isdigit():
            print("City cannot be only numbers.")
            continue
        break
    clear_screen()
    while True:
        state = input("Enter state: ").strip().capitalize()
        if state == "":
            print("State cannot be empty.")
            continue
        elif state.isdigit():
            print("State cannot be only numbers.")
            continue
        break
    clear_screen()
    while True:
        zip_code = input("Enter zip code: ").strip()
        if zip_code == "":
            print("Zip code cannot be empty.")
            continue
        elif zip_code.isalpha():
            print("Zip code cannot be letters.")
            continue
        break
    clear_screen()
    
    # Creating the contact dictionary then returning it
    
    address = {"street": street, 
               "city": city, 
               "state": state, 
               "zip code": zip_code}
    
    x = datetime.datetime.now()
    contact_data = {"first_name": first_name, 
                    "last_name": last_name, 
                    "email": email, 
                    "phone": phone, 
                    "address": address,
                    "Timestamp": f"Contact created on {x}"
                    }
    
    # Generating a unique contact ID
    contact_id = f"contact_{len(contacts_database) + 1}"
    
    contacts_database[contact_id] = contact_data
    
    print(f"\nYou created : {contact_id} successfully!\n")
    
    return contact_data

# Create a new contact and print the details

contacts_database = {}

def show_contacts():
    print("\n--- All Contacts ---")
    
    for contact_id, info in contacts_database.items():
        print(f"{contact_id}: {info['first_name']} , {info['last_name']} , {info['email']} , {info['phone']} , {info['address']} , {info['Timestamp']}")
        
def delete_contact():
    print("\nDeleting a contact...\n")
    
    contact_id = input("Enter the contact ID to delete (e.g., contact_1, etc.): ").strip()
    
    if contact_id in contacts_database:
        del contacts_database[contact_id]
        print(f"Contact {contact_id} has been deleted.")
    elif not contacts_database:
        print("\nNo contacts are stored currently.\n")
    else:
        print(f"Contact ID {contact_id} not found.")

def main_menu():
    clear_screen()
    # Main menu loop
    while True:
        print("\nContact Manager:\n")
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
        choice = int(input("\nChoose an option (1-9): "))
        
        # Handle user choice
        if choice == 1:
            clear_screen()
            create_contact()
        elif choice == 2:
            clear_screen()
            # search_contacts()
            pass
        elif choice == 3:
            clear_screen()
            while True:
                if not contacts_database:
                    print("\nNo contacts are stored currently.\n")
                    break
                else:
                    show_contacts()
                    break
        elif choice == 4:
            clear_screen()
            # update_contact()
            pass
        elif choice == 5:
            clear_screen()
            delete_contact()
        elif choice == 6:
            clear_screen()
            # generate_statistics()
            pass
        elif choice == 7:
            clear_screen()
            # find_duplicates()
            pass
        elif choice == 8:
            clear_screen()
            # export_by_category()
            pass
        elif choice == 9:
            clear_screen()
            print("\nExiting the program. Goodbye!\n")
            sys.exit()
        else:  
            clear_screen()
            print("\nInvalid choice. Please select a valid option.\n")
            
main_menu()