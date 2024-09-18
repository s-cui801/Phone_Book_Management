# This file represents an individual contact entry with attributes and timestamps.
from datetime import datetime
import re

class Contact:
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
        
        # Set the validated attributes and timestamps for the contact
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.created_at = datetime.now().replace(microsecond=0)  # Timestamp(Round to sec) for when contact was created
        self.updated_at = datetime.now().replace(microsecond=0)  # Timestamp(Round to sec) for when contact was last updated

    def update_contact(self, first_name=None, last_name=None, phone_number=None, email=None, address=None):
        # Update provided fields of contact and update the timestamp
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        # Validation for phone number format
        if phone_number and not re.match(r"\(\d{3}\) \d{3}-\d{4}", phone_number):
            raise ValueError("Phone number must be in the format (###) ###-####")
        # Validation for email format
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")
        if address:
            self.address = address
        self.updated_at = datetime.now().replace(microsecond=0)
    
    def __str__(self):
        # Return a string representation of the contact
        # For optional fields, print None if the value is not provided.
        return f"{self.first_name} {self.last_name} - {self.phone_number} - {self.email or None} - {self.address or None} (Created: {self.created_at}, Updated: {self.updated_at})"
    