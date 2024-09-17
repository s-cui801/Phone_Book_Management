# This file represents an individual contact entry with attributes and timestamps.
from datetime import datetime

class Contact:
    def __init__(self, first_name, last_name, phone_number, email=None, address=None):
        # Initialize the contact with the provided attributes.
        # email and address are optional fields.
        # TODO: Add validation for phone number and email.
        # TODO：Generate a unique ID for each contact.
        # TODO: Generate error messages for invalid input:
        #  e.g. "Invalid phone number format." or "Invalid email format."
        # e.g. "First name is required." or "Last name is required." or "Phone number is required."
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.created_at = datetime.now()  # Timestamp for when contact was created
        self.updated_at = datetime.now()  # Timestamp for when contact was last updated

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
        self.updated_at = datetime.now()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone_number} (Created: {self.created_at}, Updated: {self.updated_at})"
    