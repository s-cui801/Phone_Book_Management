import time
import unittest
from datetime import datetime
from contact import Contact

class TestContact(unittest.TestCase):

    def test_contact_initialization(self):
        contact = Contact("John", "Doe", "(123) 456-7890", "john.doe@example.com", "123 Elm Street")
        self.assertEqual(contact.first_name, "John")
        self.assertEqual(contact.last_name, "Doe")
        self.assertEqual(contact.phone_number, "(123) 456-7890")
        self.assertEqual(contact.email, "john.doe@example.com")
        self.assertEqual(contact.address, "123 Elm Street")
        self.assertIsInstance(contact.created_at, datetime)
        self.assertIsInstance(contact.updated_at, datetime)

    def test_contact_initialization_without_optional_fields(self):
        contact = Contact("Jane", "Doe", "(987) 654-3210")
        self.assertEqual(contact.first_name, "Jane")
        self.assertEqual(contact.last_name, "Doe")
        self.assertEqual(contact.phone_number, "(987) 654-3210")
        self.assertIsNone(contact.email)
        self.assertIsNone(contact.address)
        self.assertIsInstance(contact.created_at, datetime)
        self.assertIsInstance(contact.updated_at, datetime)

    def test_invalid_phone_number_format(self):
        with self.assertRaises(ValueError):
            Contact("John", "Doe", "123-456-7890")

    def test_invalid_email_format(self):
        with self.assertRaises(ValueError):
            Contact("John", "Doe", "(123) 456-7890", "john.doe@com")

    def test_missing_required_fields(self):
        with self.assertRaises(ValueError):
            Contact("", "Doe", "(123) 456-7890")
        with self.assertRaises(ValueError):
            Contact("John", "", "(123) 456-7890")
        with self.assertRaises(ValueError):
            Contact("John", "Doe", "")

    def test_update_contact(self):
        contact = Contact("John", "Doe", "(123) 456-7890")
        old_updated_at = contact.updated_at
        time.sleep(1)
        contact.update_contact(first_name="Johnny", email="johnny.doe@example.com")
        self.assertEqual(contact.first_name, "Johnny")
        self.assertEqual(contact.email, "johnny.doe@example.com")
        self.assertNotEqual(contact.updated_at, old_updated_at)

    def test_str_representation(self):
        contact = Contact("John", "Doe", "(123) 456-7890", "john.doe@example.com", "123 Elm Street")
        expected_str = f"John Doe - (123) 456-7890 - john.doe@example.com - 123 Elm Street (Created: {contact.created_at}, Updated: {contact.updated_at})"
        self.assertEqual(str(contact), expected_str)

if __name__ == '__main__':
    unittest.main()