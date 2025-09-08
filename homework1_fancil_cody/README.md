# Contact Manager

## Project Description and Features

**Contact Manager** is a Python-based command-line application for storing, searching, updating, and deleting personal contact information. It allows users to manage a list of contacts with fields such as first name, last name, email, phone, and address. The program features input validation, timestamping of contact creation and updates, and a user-friendly menu-driven interface.

**Features:**
- Add new contacts with validation for each field
- Search contacts by first or last name (case-insensitive)
- List all contacts in the database
- Update any field of an existing contact, with update timestamp
- Delete contacts by contact ID
- Generate statistics (total contacts, unique cities/states, etc.)
- Find duplicate contacts by email, phone, first name, or last name
- Clear and readable terminal output


## How to Run the Program

1. **Requirements:**  
   - Python 3.10.6 or later installed on your system

2. **Running the Program:**  
   - Open a terminal or command prompt.
   - Navigate to the folder containing `contact_manager.py`.
   - Run the program with:
     python contact_manager.py




## Function Documentation with Examples

### `create_contact()`
Prompts the user to input and validate all fields for a new contact, then adds it to the database.

**Example:**
create_contact()
# Prompts for each field, validates, and adds the contact.


### `show_contacts()`
Displays all contacts currently stored in the database.

**Example:**

show_contacts()
# Prints all contacts in a readable format.


### `delete_contact()`
Prompts the user for a contact ID and deletes the corresponding contact.

**Example:**

delete_contact()
# User enters 'contact_1', and that contact is removed if it exists.


### `search_contacts(contacts_database)`
Allows the user to search for contacts by first or last name.

**Example:**
search_contacts(contacts_database)
# User enters 'alice', and all contacts with 'alice' in their first or last name are shown.


### `update_contact()`
Allows the user to update a specific field of a contact found by first or last name.

**Example:**
update_contact()
# User searches for a contact, selects a field to update, and enters the new value.


### `generate_statistics()`
Generates and displays statistics about the contacts in the database, such as total contacts, unique cities, and unique states.

**Example:**
generate_statistics()
# Prints statistics about the current contacts.


### `find_duplicates()`
Identifies and displays duplicate contacts based on email, phone number, first name, or last name.

**Example:**
find_duplicates()
# Prints duplicate contacts if found.


## Known Limitations and Future Improvements

- Contacts are not saved to disk; all data is lost when the program exits.
- No support for importing/exporting contacts to/from files.
- Duplicate detection is basic and may flag common names.
- No advanced search (e.g., by email or phone).
- No categories or groups for contacts.
- Planned features: export by category, persistent storage, improved duplicate handling.


## Sample Usage Scenarios

- **Adding a Contact:**  
  User selects "Add new Contact" and enters all required fields. The contact is validated and added to the database.

- **Searching for a Contact:**  
  User selects "Search contacts" and enters a name. All matching contacts are displayed.

- **Updating a Contact:**  
  User selects "Update contact," searches for a contact, chooses a field to update, and enters the new value. The contact's update timestamp is refreshed.

- **Deleting a Contact:**  
  User selects "Delete contact," enters the contact ID (e.g., `contact_2`), and the contact is removed from the database.

- **Viewing Statistics:**  
  User selects "Generate statistics" to see the total number of contacts, unique cities, and unique states.

- **Finding Duplicates:**  
  User selects "Find duplicates" to identify contacts with the same email, phone, or name.