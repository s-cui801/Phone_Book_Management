# Description: This file contains the test cases for the phonebook application.
from phone_book import PhoneBook
from contact import Contact
import unittest

class Test_PhoneBook(unittest.TestCase):
    def setUp(self):
        self.phonebook = PhoneBook()
    def test_add_contact(self):
        self.phonebook.add_contact(Contact("John", "Doe", "1234567890", "john@gmail.com", "123 Main St"))  # Add a contact
        self.assertEqual(len(self.phonebook.contacts), 1)
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

if __name__ == "__main__":
    unittest.main()