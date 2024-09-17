# This file will manage CRUD operations for the phonebook application.

import csv
from contact import Contact

class PhoneBook:
    def __init__(self):
        self.contacts = []  # List to store Contact objects

    def add_contact(self, contact):
        # Add a contact to the phone book
        self.contacts.append(contact)

    def import_contacts(self, csv_file):
        # Read contacts from a CSV file and add them to the phone book
        #  the CSV file should include at least the following columns: 
        # first_name, last_name, and phone_number. 
        # Optionally, it can also include email and address.
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contact = Contact(row['first_name'], row['last_name'], row['phone_number'], row.get('email'), row.get('address'))
                self.add_contact(contact)

    def search_contact(self, keyword):
        # TODO: Implement wildcard search on first_name and last_name; e.g. "John" should match "John" and "Johnny"
        # TODO: Implement search by phone number
        # Search for contacts by keyword (name or phone number)
        # Return a list of contacts that match the keyword. Return an empty list if no contacts are found.
        results = [contact for contact in self.contacts if keyword.lower() in contact.first_name.lower() or keyword.lower() in contact.last_name.lower() or keyword in contact.phone_number]
        return results

    def update_contact(self, contact, **kwargs):
        # The **kwargs parameter is a special syntax in Python that allows the method to accept an arbitrary number of keyword arguments. 
        # These keyword arguments are passed as a dictionary, where the keys are the argument names and the values are the corresponding values.
        
        contact.update_contact(**kwargs)
        # Print the updated contact
        print(f"Contact updated:{contact}")
        
    def delete_contact(self, contact):
        # Delete a contact by index
        self.contacts.remove(contact)

    def list_contacts(self):
        # List all contacts
        return self.contacts
    
    def export_contacts(self, csv_file):
        # Export contacts to a CSV file
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['first_name', 'last_name', 'phone_number', 'email', 'address'])
            for contact in self.contacts:
                writer.writerow([contact.first_name, contact.last_name, contact.phone_number, contact.email, contact.address])
    
    

