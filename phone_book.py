# This file will manage CRUD operations for the phonebook application.

import csv
import logging
from contact import Contact
# Configure logging
logging.basicConfig(filename='phonebook.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class PhoneBook:
    def __init__(self):
        self.contacts = []  # List to store Contact objects

    def add_contact(self, first_name, last_name, phone_number, email=None, address=None):
        # Create a new contact with the provided attributes
        # Raise a ValueError if the contact cannot be created due to missing or invalid attributes
        try:
            new_contact = Contact(first_name, last_name, phone_number, email, address)
            self.contacts.append(new_contact)
        except ValueError as ve:
            # Log the error and re-raise it to be handled by CLI
            logging.error(f"Failed to add new contact: {ve}")
            raise ve
        

    def import_contacts(self, csv_file):
        # Read contacts from a CSV file and add them to the phone book
        # The first row of the CSV file should be the header row.
        try:
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        first_name = row['first_name']
                        last_name = row['last_name']
                        phone_number = row['phone_number']
                        email = row.get('email', None)
                        address = row.get('address', None) # Using dict.get() to handle missing 'address' key
                        # Try to add a new contact. This will raise a ValueError if data is invalid.
                        self.add_contact(first_name, last_name, phone_number, email, address)
                    except ValueError as ve:
                        # Log the error and continue to the next row
                        logging.error(f"Error in row{reader.line_num}: {ve}")
                        print(f"Skipping invalid row{reader.line_num}: {ve}")
                        continue
        
        except FileNotFoundError:
            logging.error(f"File not found: {csv_file}")
            print(f"File not found: {csv_file}")
        except IOError as ioe:
            logging.error(f"Error reading file {csv_file}: {ioe}")
            print(f"Error reading file {csv_file}: {ioe}")
        except csv.Error as cve:
            logging.error(f"CSV parsing error in file {csv_file} : {cve}")
            print(f"Invalid CSV format in file {csv_file}: {cve}")       
                

    def search_contact(self, keyword):
        # Search for contacts by keyword (name or phone number)
        # Return a list of contacts that match the keyword. Return an empty list if no contacts are found.
        results = [contact for contact in self.contacts if keyword.lower() in contact.first_name.lower() or keyword.lower() in contact.last_name.lower() or keyword in contact.phone_number]
        logging.info(f"Search results for '{keyword}': {results}")
        return results
    
    def search_contact_by_updated_time(self, start_time, end_time):
        '''
            Search for contacts updated within a specific time range.
            Raise a ValueError if the start time is greater than the end time. 
            Return a list of contacts that were updated within the specified time range.
            Return an empty list if no contacts are found.
        '''
        results = [contact for contact in self.contacts if start_time <= contact.updated_at <= end_time]
        logging.info(f"Search results for contacts updated between {start_time} and {end_time}: {results}")
        return results
    
    def search_contact_by_created_time(self, start_time, end_time):
        '''
            Search for contacts created within a specific time range.
            Raise a ValueError if the start time is greater than the end time. 
            Return a list of contacts that were created within the specified time range.
            Return an empty list if no contacts are found.
        '''
        results = [contact for contact in self.contacts if start_time <= contact.created_at <= end_time]
        logging.info(f"Search results for contacts created between {start_time} and {end_time}: {results}")
        return results


    def update_contact(self, contact, **kwargs):
        # Update a contact with the provided keyword arguments
        # The **kwargs parameter is a special syntax in Python that allows the method to accept an arbitrary number of keyword arguments. 
        # These keyword arguments are passed as a dictionary, where the keys are the argument names and the values are the corresponding values.   
        try:
            contact.update_contact(**kwargs)
        except ValueError as ve:
            # Log the error and re-raise it to be handled by CLI
            logging.error(f"Failed to update contact: {ve}")
        
        
    def delete_contact(self, contact):
        # Delete a contact by index
        self.contacts.remove(contact)
        logging.info(f"Contact deleted: {contact}")

    def list_contacts(self):
        # List all contacts
        logging.info("Listing all contacts.")
        return self.contacts
    
    def export_contacts(self, csv_file):
        # Export contacts to a CSV file
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['first_name', 'last_name', 'phone_number', 'email', 'address'])
            for contact in self.contacts:
                writer.writerow([contact.first_name, contact.last_name, contact.phone_number, contact.email, contact.address])
            logging.info(f"Contacts exported to {csv_file}")
    

