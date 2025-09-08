import datetime , sys, os

# Global database - this is where ALL contacts are stored
contacts_database = {}
# Contact data storage
contact_data = {}
# Initializing variables
address = {}
first_name = ""
last_name = ""
email = ""
phone = ""

def clear_screen():
    """
    Clears the terminal screen for better readability.
    Uses 'cls' for Windows and 'clear' for Unix-based systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
def create_contact():
    """
    Prompts the user to input and validate all fields for a new contact.
    Adds the new contact to the global contacts_database dictionary.
    Returns:
        dict: The newly created contact's data.
    """
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
        state = input("Enter state abbreviation: ").strip().capitalize()
        if state == "":
            print("State cannot be empty.")
            continue
        elif state.isdigit():
            print("State cannot be only numbers.")
            continue
        elif len(state) != 2:
            print("State must be a 2-letter abbreviation.")
            continue
        break
    clear_screen()
    
    while True:
        zip_code = input("Enter zip code: ").strip().capitalize()
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
    
    contact_id = f"contact_{len(contacts_database) + 1}"
    x = datetime.datetime.now()
    
    contact_data = {"contact_id": f"contact_{len(contacts_database) + 1}",
                    "first_name": first_name, 
                    "last_name": last_name, 
                    "email": email, 
                    "phone": phone, 
                    "address": address,
                    "Timestamp": f"Contact created on {x}"
                    }
    
    contacts_database[contact_id] = contact_data
    
    print(f"\nYou created : {contact_id} successfully!\n")
    
    return contact_data

def show_contacts():
    """
    Displays all contacts currently stored in the contacts_database.
    Prints each contact's details in a readable format.
    """
    print("\n--- All Contacts ---")
    for contact_id, info in contacts_database.items():
        print(f"{contact_id}: {info['first_name']} , {info['last_name']} , {info['email']} , {info['phone']} , {info['address']} , {info['Timestamp']}, {info.get('Timestamp_updated', 'Never updated')}")

def delete_contact():
    """
    Prompts the user for a contact ID and deletes the corresponding contact from contacts_database.
    Handles cases where the contact does not exist or the database is empty.
    """
    print("\nDeleting a contact...\n")
    if not contacts_database:
        print("\nNo contacts are stored currently.\n")
        return
    
    contact_id = input("Enter the contact ID to delete (e.g., contact_1, etc.): ").strip().lower()
    
    if contact_id in contacts_database:
        del contacts_database[contact_id]
        print(f"Contact {contact_id} has been deleted.")
    elif not contacts_database:
        print("\nNo contacts are stored currently.\n")
    else:
        print(f"Contact ID {contact_id} not found.")

def search_contacts(contacts_database):
    """
    Allows the user to search for contacts by first or last name.
    Prints the contact details if found, otherwise notifies the user.
    Args:
        contacts_database (dict): The dictionary containing all contacts.
    Returns:
        dict or None: The found contact's data, or None if not found.
    """
    while True:
        print("\nSearching contacts by name...\n")
        if not contacts_database: 
            print("\nNo contacts are stored currently.\n")
            break
        name_query = input("Enter the first or last name to search: ").strip().lower()
        for contact_id, contact in contacts_database.items():
            if name_query in (contact['first_name'].lower()) or (name_query in contact['last_name'].lower()):
                print(f"\nContact has been found!\n {contact_id}: {contact['first_name']} , {contact['last_name']} , {contact['email']} , {contact['phone']} , {contact['address']} , \n {contact['Timestamp']}")
                return contact
            else:
                print(f"\nNo contact found with the name: {name_query}\n")
                return None

def update_contact():
    """
    Allows the user to update a specific field of a contact found by first or last name.
    Prompts for the field to update and validates the new value.
    Updates the contact and adds a 'Timestamp_updated' field.
    Returns:
        dict or None: The updated contact's data, or None if not found.
    """
    while True:
        print(f"\nWhich contact? Search by First/Last name.\n")
        if not contacts_database: 
            print(f"\nNo contacts are stored currently.\n")
            break
        name_query = input("Enter the first or last name to search: ").strip().lower()
        print(f"\nSearching contacts by name...\n")
        for contact_id, contact in contacts_database.items():
            if name_query in (contact['first_name'].lower()) or (name_query in contact['last_name'].lower()):
                print(f"\nContact has been found!\n\n {contact_id}: {contact['first_name']} , {contact['last_name']} , {contact['email']} , {contact['phone']} , {contact['address']} , \n {contact['Timestamp']} , \n {contact.get('Timestamp_updated', 'Never updated')},\n")
                print(f"1. First Name\n2. Last Name\n3. Email\n4. Phone\n5. Street\n6. City\n7. State\n8. Zip Code\n")
                choice=(input(f"\nWhat would you like to update?: \n"))
                if choice == "1":
                    new_first_name = input("Enter new first name: ").strip().capitalize()
                    if new_first_name == "":
                        print("First name cannot be empty.")
                        continue
                    elif new_first_name.isdigit():
                        print("First name cannot be number.")
                        continue
                    elif new_first_name == contact['first_name']:
                        print("New first name cannot be the same as the current first name.")
                        continue
                    elif new_first_name.isalpha() == False:
                        print("First name must contain only letters.")
                        continue
                    contact['first_name'] = new_first_name
                    print(f"\nFirst name updated to {new_first_name}.\n")
                    contact['Timestamp_updated'] = f"Contact updated on {datetime.datetime.now()}"
                    return contact
                elif choice == "2":
                    new_last_name = input("Enter new last name: ").strip().capitalize()
                    if new_last_name == "":
                        print("Last name cannot be empty.")
                        continue
                    elif new_last_name.isdigit():
                        print("Last name cannot be number.")
                        continue
                    elif new_last_name == contact['last_name']:
                        print("New last name cannot be the same as the current last name.")
                        continue
                    elif new_last_name.isalpha() == False:
                        print("Last name must contain only letters.")
                        continue
                    contact['last_name'] = new_last_name
                    print(f"\nLast name updated to {new_last_name}.\n")
                    contact['Timestamp_updated'] = f"Contact updated on {datetime.datetime.now()}"
                    return contact
                elif choice == "3":
                    new_email = input("Enter new email: ").strip().capitalize()
                    if new_email == "":
                        print("Email cannot be empty.")
                        continue
                    elif "@" not in new_email or "." not in new_email:
                        print("Email must contain '@' and '.'")
                        continue
                    elif new_email.isdigit():
                        print("Email cannot be only numbers.")
                        continue
                    elif new_email == contact['email']:
                        print("New email cannot be the same as the current email.")
                        continue
                    contact['email'] = new_email
                    print(f"\nEmail updated to {new_email}.\n")
                    contact['Timestamp_updated'] = f"Contact updated on {datetime.datetime.now()}"
                    return contact
                elif choice == "4":
                    new_phone = input("Enter new phone number: ").strip()
                    if new_phone == "":
                        print("Phone number cannot be empty.")
                        continue
                    elif new_phone.isalpha():
                        print("Phone number cannot be letters.")
                        continue
                    elif new_phone == contact['phone']:
                        print("New phone number cannot be the same as the current phone number.")
                        continue
                    contact['phone'] = new_phone
                    print(f"\nPhone number updated to {new_phone}.\n")
                    contact['Timestamp_updated'] = f"Contact updated on {datetime.datetime.now()}"
                    return contact
                elif choice == "5":
                    new_street = input("Enter new street: ").strip().capitalize()
                    if new_street == "":
                        print("Street cannot be empty.")
                        continue
                    elif new_street.isdigit():
                        print("Street cannot be only numbers.")
                        continue
                    elif new_street == contact['address']['street']:
                        print("New street cannot be the same as the current street.")
                        continue
                    contact['address']['street'] = new_street
                    print(f"\nStreet updated to {new_street}.\n")
                    contact['Timestamp_updated'] = f"Contact updated on {datetime.datetime.now()}"
                    return contact
                elif choice == "6":
                    new_city = input("Enter new city: ").strip().capitalize()
                    if new_city == "":
                        print("City cannot be empty.")
                        continue
                    elif new_city.isdigit():
                        print("City cannot be only numbers.")
                        continue
                    elif new_city == contact['address']['city']:
                        print("New city cannot be the same as the current city.")
                        continue
                    elif new_city.isalpha() == False:
                        print("City must contain only letters.")
                        continue
                    contact['address']['city'] = new_city
                    print(f"\nCity updated to {new_city}.\n")
                    contact['Timestamp_updated'] = f"Contact updated on {datetime.datetime.now()}"
                    return contact
                elif choice == "7":
                    new_state = input("Enter new state: ").strip().capitalize()
                    if new_state == "":
                        print("State cannot be empty.")
                        continue
                    elif new_state.isdigit():
                        print("State cannot be only numbers.")
                        continue
                    elif new_state == contact['address']['state']:
                        print("New state cannot be the same as the current state.")
                        continue
                    elif new_state.isalpha() == False:
                        print("State must contain only letters.")
                        continue
                    contact['address']['state'] = new_state
                    print(f"\nState updated to {new_state}.\n")
                    contact['Timestamp_updated'] = f"Contact updated on {datetime.datetime.now()}"
                    return contact
                elif choice == "8":
                    new_zip_code = input("Enter new zip code: ").strip().capitalize()
                    if new_zip_code == "":
                        print("Zip code cannot be empty.")
                        continue
                    elif new_zip_code.isalpha():
                        print("Zip code cannot be letters.")
                        continue
                    elif new_zip_code == contact['address']['zip code']:
                        print("New zip code cannot be the same as the current zip code.")
                        continue
                    contact['address']['zip code'] = new_zip_code
                    print(f"\nZip code updated to {new_zip_code}.\n")
                    contact['Timestamp_updated'] = f"Contact updated on {datetime.datetime.now()}"
                    return contact
            else:
                print(f"\nNo contact found with the name: {name_query}, cannot update.\n")
                return None
"""
def contact_statistics():
    
    Generates and displays statistics about the contacts in the contacts_database.
    Statistics include total number of contacts, number of unique cities, and number of unique states.
    
    if not contacts_database:
        print("\nNo contacts are stored currently.\n")
        return
    
    total_contacts = len(contacts_database)
    unique_cities = set()
    unique_states = set()
    
    for contact in contacts_database.values():
        unique_cities.add(contact['address']['city'])
        unique_states.add(contact['address']['state'])
    
    print("\n--- Contact Statistics ---")
    print(f"Total number of contacts: {total_contacts}")
    print(f"Number of unique cities: {len(unique_cities)}")
    print(f"Number of unique states: {len(unique_states)}")
"""
def find_duplicates():
    """
    Identifies and displays duplicate contacts based on email or phone number.
    Prints the details of duplicate contacts if found, otherwise notifies the user.
    """
    if not contacts_database:
        print("\nNo contacts are stored currently.\n")
        return
    
    seen_emails = {}
    seen_phones = {}
    seen_first_names = {}
    seen_last_names = {}
    duplicates = []
    
    for contact_id, contact in contacts_database.items():
        first_name = contact['first_name']
        last_name = contact['last_name']
        email = contact['email']
        phone = contact['phone']
        timestamp = contact['Timestamp']
        
        if email in seen_emails:
            duplicates.append((seen_emails[email], contact_id))
        else:
            seen_emails[email] = contact_id
        
        if phone in seen_phones:
            duplicates.append((seen_phones[phone], contact_id))
        else:
            seen_phones[phone] = contact_id
        if first_name in seen_first_names:
            duplicates.append((seen_first_names[first_name], contact_id))
        else:
            seen_first_names[first_name] = contact_id
        if last_name in seen_last_names:
            duplicates.append((seen_last_names[last_name], contact_id))
'''
    if len(duplicates) > 0:
        print("\n--- Duplicate Contacts Found ---")
        for dup in duplicates:
            print(f"Duplicate pair: {dup[0]} and {dup[1]}\n")
            print(f"{dup[0]}: {contacts_database[dup[0]]}\n")
            print(f"{dup[1]}: {contacts_database[dup[1]]}\n")
    else:
        print("\nNo duplicate contacts found.\n")
        
    if len(duplicates) > 0:
        choice=input("Do you want to merge contacts? (y/n): ").strip().lower()
        if choice == 'y' or 'Y':
            for dup in duplicates:
        else:
            print("No contacts were merged.")
'''
def generate_statistics():
    """
    Generates and displays statistics about the contacts in the contacts_database.
    """
    if not contacts_database:
        print("\nNo contacts are stored currently.\n")
        return
    
    total_contacts = len(contacts_database)
    unique_cities = set()
    unique_states = set()
    
    for contact in contacts_database.values():
        unique_cities.add(contact['address']['city']['zip code'])
        unique_states.add(contact['address']['state']['zip code'])
    
    print("\n--- Contact Statistics ---")
    print(f"Total number of contacts: {total_contacts}")
    print(f"Number of unique cities: {len(unique_cities)}")
    print(f"Number of unique states: {len(unique_states)}")
    for state in unique_states:
        print (f"State: {state}, Number of contacts: {sum(1 for contact in contacts_database.values() if contact['state'] == state)}")
    print("\n")
    for zip in unique_cities:
        print (f"Zip Code: {zip}, Number of contacts: {sum(1 for contact in contacts_database.values() if contact['zip code'] == zip)}")
    print("\n")
    
    # No input info is allowed to be empty, all contacts have all fields filled. 
    # Therefore, no need to check for empty fields when generating statistics or floats for averages per category, each will be 100%.
def main_menu():
    """
    Displays the main menu and handles user navigation through the contact manager.
    Calls the appropriate function based on user input.
    Loops until the user chooses to exit.
    """
    clear_screen()
    # Main menu loop
    while True:
        print("\nContact Manager:\n")
        print("1. Add new Contact")
        print("2. Search contacts by first/last name")
        print("3. List contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Generate statistics")
        print("7. Find duplicates")
        print("8. Exit")
        # Get user choice
        while True:
            choice = (input("\nChoose an option (1-8): "))
            if choice.isdigit():
                choice = int(choice)
                break
            elif choice.isalpha():
                print(f"\nPlease enter a number, 1-8\n")
            else:
                print(f"\nInvalid input. Please enter a number, 1-8\n")
        # Handle user choice
        if choice == 1:
            clear_screen()
            create_contact()
        elif choice == 2:
            clear_screen()
            search_contacts(contacts_database)
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
            update_contact()
            pass
        elif choice == 5:
            clear_screen()
            delete_contact()
        elif choice == 6:
            clear_screen()
            generate_statistics()
            pass
        elif choice == 7:
            clear_screen()
            find_duplicates()
            pass
        elif choice == 8:
            clear_screen()
            print("\nExiting the program. Goodbye!\n")
            sys.exit()
        else:  
            clear_screen()
            print("\nInvalid choice. Please select a valid option.\n")

main_menu()