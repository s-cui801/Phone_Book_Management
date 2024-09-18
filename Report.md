Report

0. Overview

1. Set Up Python Development Environment

   Ensure your virtual environment is activated in VSCode.

   Create the main Python files:

   - `contact.py` (for the `Contact` class).
   - `phone_book.py` (for the `PhoneBook` class).
   - `main.py` (for the command-line interface).

2. User Interface

3. Contact Information

   Basic Contact class (without advanced functionalities):

   ```python
   # This file represents an individual contact entry with attributes and timestamps.
   from datetime import datetime
   
   class Contact:
       def __init__(self, first_name, last_name, phone_number, email=None, address=None):
           # Initialize the contact with the provided attributes.
           # email and address are optional fields.
           self.first_name = first_name
           self.last_name = last_name
           self.phone_number = phone_number
           self.email = email
           self.address = address
           self.created_at = datetime.now().replace(microsecond=0)  # Timestamp for when contact was created
           self.updated_at = datetime.now().replace(microsecond=0)  # Timestamp for when contact was last updated
   
       def update_contact(self, first_name=None, last_name=None, phone_number=None, email=None, address=None):
           # Update the contact and update the timestamp
           # if the attribute is provided.
           if first_name:
               self.first_name = first_name
           if last_name:
               self.last_name = last_name
           if phone_number:
               self.phone_number = phone_number
           if email:
               self.email = email
           if address:
               self.address = address
           self.updated_at = datetime.now().replace(microsecond=0)
       
       def __str__(self):
           # Return a string representation of the contact
           # For optional fields, print None if the value is not provided.
           return f"{self.first_name} {self.last_name} - {self.phone_number} - {self.email or None} - {self.address or None} (Created: {self.created_at}, Updated: {self.updated_at})"
       
   ```

   

4. Basic CRUD Operations

   In phonebook class. The `PhoneBook` class will manage CRUD operations for all contacts.

   1. Add single contact

   2. Import contacts via cvs file

   3. Search contacts using phone number or name

   4. Update contact

      User needs to search for the contact that they want to update.

      

   5. delete contact

   

5. Search Functionality

   1. Filters to search for contacts added within a specific time frame.

6. Sorting and Grouping

7. Logging and Auditing

   **Logging actions** such as adding, updating, deleting, and searching for contacts helps track changes.

   You should configure **log level** (e.g., `INFO`, `ERROR`, etc.) depending on the severity of events.

   Use the `PhoneBook` class to log operations rather than the `PhoneBookCLI`, since the `PhoneBook` class is where the actual data handling occurs.

8. Input Validation

   1. Validation for contact attributes

      Two parts: 

      Validation for required fields

      Validation for phone number and email format, using Regular Expression(正则表达式)

      If contact attributes are not legal, raise ValueError accordingly.

      Integrate validation into Contact class:

      ```python
      #contact.py
      def __init__(self, first_name, last_name, phone_number, email=None, address=None): 
              # First name, last name and phone number are required fields.
              # The email and address are optional fields.
              # Initialize the contact with the provided attributes.
              # Raise a ValueError if required fields are missing or if the phone number or email is in an invalid format.
              
              #Validation for required fields
              if not first_name:
                  raise ValueError("First name is required.")
              if not last_name:
                  raise ValueError("Last name is required.")
              if not phone_number:
                  raise ValueError("Phone number is required.")
      
              # Validation for email format
              if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                  raise ValueError("Invalid email address")
              
              # Validation for phone number format
              if not re.match(r"\(\d{3}\) \d{3}-\d{4}", phone_number):
                  raise ValueError("Phone number must be in the format (###) ###-####")
      ```

      Tests for contact class:



​			