# Description: This file contains the test cases for the phonebook application.
from phone_book import PhoneBook
from contact import Contact
import unittest
import datetime

class Test_PhoneBook(unittest.TestCase):
    def setUp(self):
        self.phonebook = PhoneBook()
    def test_add_contact(self):
        contact = Contact("John", "Doe", "1234567890", "john@gmail.com", "123 Main St")
        self.phonebook.add_contact(contact)  # Add a contact
        self.assertEqual(len(self.phonebook.contacts), 1)
        self.assertEqual(self.phonebook.contacts[0].first_name, "John")
        self.assertEqual(self.phonebook.contacts[0].last_name, "Doe")
        self.assertEqual(self.phonebook.contacts[0].phone_number, "1234567890")
        self.assertEqual(self.phonebook.contacts[0].email, "john@gmail.com")
        self.assertEqual(self.phonebook.contacts[0].address, "123 Main St")
    def test_import_contacts(self):
        self.phonebook.import_contacts("data.csv")  # Import contacts from CSV file
        self.assertEqual(len(self.phonebook.contacts), 4)
    def test_search_contact(self):
        self.phonebook.import_contacts("data.csv")
        results = self.phonebook.search_contact("Tom")
        self.assertEqual(len(results), 0)
    def test_update_contact(self):
        self.phonebook.import_contacts("data.csv")
        contact = self.phonebook.search_contact("Johnson")[0]
        self.phonebook.update_contact(contact, first_name="Tommy")
        self.assertEqual(len(self.phonebook.search_contact("Tommy")), 1)
        self.assertEqual(len(self.phonebook.search_contact("Johnson")), 0)
    def test_delete_contact(self):
        self.phonebook.import_contacts("data.csv")
        contact = self.phonebook.search_contact("Johnson")[0]
        self.phonebook.delete_contact(contact)
        self.assertEqual(len(self.phonebook.search_contact("Johnson")), 0)
    def test_search_contact_by_updated_time(self):
        self.phonebook.import_contacts("data.csv")
        results = self.phonebook.search_contact_by_time(datetime.datetime(2021, 1, 1), datetime.datetime(2021, 1, 31))
        self.assertEqual(len(results), 0)

        results = self.phonebook.search_contact_by_time(datetime.datetime(2024, 1, 1), datetime.datetime(2024, 12, 31))
        self.assertEqual(len(results), 4)
    
    def test_group_contact_by_initial_letter(self):
        self.phonebook.import_contacts("data.csv")
        # Group contacts by first name
        results = self.phonebook.group_contacts_by_initial_letter("first_name")
        self.assertEqual(len(results), 3)
        self.assertEqual(len(results['J']), 2)
        self.assertEqual(len(results['L']), 1)
        self.assertEqual(len(results['E']), 1)
        self.assertIsNone(results.get('T'))
        # Group contacts by last name
        results = self.phonebook.group_contacts_by_initial_letter("last_name")
        self.assertEqual(len(results), 3)
        self.assertEqual(len(results['D']), 1)
        self.assertEqual(len(results['S']), 2)
        self.assertEqual(len(results['Y']), 1)
        self.assertIsNone(results.get('T'))

    def test_export_contacts(self):
        self.phonebook.import_contacts("data.csv")
        self.phonebook.export_contacts("export.csv")
        with open("export.csv", "r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 5)
            self.assertEqual(lines[0].strip(), "first_name,last_name,phone_number,email,address")
            self.assertEqual(lines[1].strip(), "John,Smith,(123) 456-7890,john@example.com,456 Edward St")
        

if __name__ == "__main__":
    unittest.main()