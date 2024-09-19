# This file will manage CRUD operations for the phonebook application.

import csv
import logging
from contact import Contact
# Configure logging
logging.basicConfig(filename='phonebook.log', level=logging.INFO, format='%(asctime)s - %(message)s')

ORDER_DICT_LOGGING = {False: "ascending", True: "descending"} # Dictionary to map boolean values to string values. Static

class PhoneBook:
    def __init__(self):
        self.contacts = []  # List to store Contact objects

    def add_contact(self, first_name, last_name, phone_number, email=None, address=None):
        '''
            Create a new contact with the provided attributes.
            Raise a ValueError if the contact cannot be created due to missing or invalid attributes.
        '''
        try:
            new_contact = Contact(first_name, last_name, phone_number, email, address)
            self.contacts.append(new_contact)
        except ValueError as ve:
            # Log the error and re-raise it to be handled by CLI
            logging.error(f"Failed to add new contact: {ve}")
            raise ve
        

    def import_contacts(self, csv_file):
        '''
            Read contacts from a CSV file and add them to the phone book.
            The first row of the CSV file should be the header row.
            Raise a ValueError if the file is not found, cannot be read, or has invalid CSV format.
        '''
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
        '''
            Search for contacts by keyword (name or phone number).
            Return a list of contacts that match the keyword.
            Return an empty list if no contacts are found.
        '''
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
        '''
            Update a contact with the provided keyword arguments.
            The **kwargs parameter is a special syntax in Python that allows the method to accept an arbitrary number of keyword arguments.
            These keyword arguments are passed as a dictionary, where the keys are the argument names and the values are the corresponding values.
            Raise a ValueError if the contact cannot be updated due to missing or invalid attributes.
        '''
        try:
            contact.update_contact(**kwargs)
        except ValueError as ve:
            # Log the error and re-raise it to be handled by CLI
            logging.error(f"Failed to update contact: {ve}")
        
        
    def delete_contact(self, contact):
        '''
            Delete a contact from the phone book.
        '''
        self.contacts.remove(contact)
        logging.info(f"Contact deleted: {contact}")
    
    def delete_all_contacts(self):
        '''
            Delete all contacts from the phone book.
        '''
        self.contacts = []
        logging.info("All contacts deleted.")

    def list_contacts(self):
        '''
            List all contacts in the phone book.
            Return a list of all contacts.
        '''
        logging.info("Listing all contacts.")
        return self.contacts
    
    def sort_contacts(self, key='first_name', reverse=False):
        '''
            Sort contacts by the specified key.
            Return a list of sorted contacts.
            The key parameter specifies the attribute to sort by (e.g., 'first_name', 'last_name', 'phone_number', 'email', 'address').
            By default, contacts are sorted by first name in ascending order.
            Raise a ValueError if the key is not a valid attribute of the Contact class.
        '''
        # Sort contacts by the specified key
        self.contacts.sort(key=lambda x: getattr(x, key), reverse=reverse)
        logging.info(f"Contacts sorted by {key} in {ORDER_DICT_LOGGING[reverse]} order.")
        return self.contacts
    
    def group_contacts_by_initial_letter(self, key):
        '''
            Group contacts by the initial letter of the specified key.
            Return a dictionary where the keys are the initial letters and the values are lists of contacts.
            The key parameter specifies the attribute to group by (e.g., 'first_name', 'last_name', 'phone_number', 'email', 'address').
            Raise a ValueError if the key is not a valid attribute of the Contact class.
        '''
        # Group contacts by the initial letter of the specified key
        groups = {}
        for contact in self.contacts:
            initial = getattr(contact, key)[0].upper()
            if initial not in groups:
                groups[initial] = []
            groups[initial].append(contact)
        groups = dict(sorted(groups.items())) # Sort the dictionary by key
        logging.info(f"Contacts grouped by initial letter of {key}: {groups}")
        return groups
    
    def group_contacts_by_area_code(self):
        '''
            Group contacts by the area code of their phone numbers.
            Return a dictionary where the keys are the area codes and the values are lists of contacts.
            Return an empty dictionary if no contacts have phone numbers.
        '''
        # Group contacts by the area code of their phone numbers
        groups = {}
        for contact in self.contacts:
            area_code = contact.phone_number[1:4]
            if area_code not in groups:
                groups[area_code] = []
            groups[area_code].append(contact)
        groups = dict(sorted(groups.items())) # Sort the dictionary by key
        logging.info(f"Contacts grouped by area code: {groups}")
        return groups
         
    def export_contacts(self, csv_file):
        '''
            Export contacts to a CSV file.
            The CSV file will contain the following columns: first_name, last_name, phone_number, email, address.
            Raise a ValueError if the contacts cannot be exported due to an IO error.
        '''
        try:
            with open(csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['first_name', 'last_name', 'phone_number', 'email', 'address'])
                for contact in self.contacts:
                    writer.writerow([contact.first_name, contact.last_name, contact.phone_number, contact.email, contact.address])
                logging.info(f"Contacts exported to {csv_file}")
        except IOError as ioe:
            logging.error(f"Error writing to file {csv_file}: {ioe}")
            print(f"Error writing to file {csv_file}: {ioe}")

