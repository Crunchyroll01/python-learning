

#Here are some examples of how you can run my code and recieve errors
#Although, it should never break from the function, just redirect you to put a new input :

# 1. create_contact() - Error: empty first name
'Enter first name: '
# Output: First name cannot be empty.

# 2. create_contact() - Error: first name is a number
'Enter first name: 123'
# Output: First name cannot be number.

# 3. create_contact() - Error: invalid email
'Enter email: notanemail'
# Output: Email must contain '@' and '.'

# 4. create_contact() - Error: state not 2 letters
'Enter state: California'
# Output: State must be a 2-letter abbreviation.

# 5. show_contacts() - Error: no contacts
'(show_contacts() when database is empty)'
# Output: No contacts are stored currently.

# 6. delete_contact() - Error: no contacts
'(delete_contact() when database is empty)'
# Output: No contacts are stored currently.

# 7. delete_contact() - Error: contact ID not found
'Enter the contact ID to delete (e.g., contact_1, etc.): contact_999'
# Output: Contact ID contact_999 not found.

# 8. search_contacts() - Error: no contacts
'(search_contacts() when database is empty)'
# Output: No contacts are stored currently.

# 9. search_contacts() - Error: name not found if searching before adding any contacts
'Enter the first or last name to search: Bob'
# Output: No contact found with the name: bob

# 10. update_contact() - Error: no contacts
'(update_contact() when database is empty)'
# Output: No contacts are stored currently.

# 11. update_contact() - Error: name not found
'Enter the first or last name to search: Bob'
# Output: No contact found with the name: bob, cannot update.

# 12. update_contact() - Error: invalid new first name
'Enter new first name: '
# Output: First name cannot be empty.

'Enter new first name: Alice'
# Output: New first name cannot be the same as the current first name.

# 13. generate_statistics() - Error: no contacts
'(generate_statistics() when database is empty)'
# Output: No contacts are stored currently.

# 14. find_duplicates() - Error: no contacts
'(find_duplicates() when database is empty)'
# Output: No contacts are stored currently.

# 15. find_duplicates() - Error: no duplicates
'(find_duplicates() when all contacts are unique)'
# Output: No duplicate contacts found.