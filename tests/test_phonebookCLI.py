import unittest
from unittest.mock import patch, MagicMock
from phone_book_CLI import PhoneBookCLI
from contact import Contact

class TestPhoneBookCLI(unittest.TestCase):
    def setUp(self):
        self.cli = PhoneBookCLI()
        self.cli.phonebook = MagicMock()

    @patch('builtins.input', side_effect=["John", "Doe", "(123) 456-7890", "john@example.com", "123 Main St"])
    def test_create_single_contact(self, mock_input):
        self.cli.create_single_contact()
        self.cli.phonebook.add_contact.assert_called_once_with("John", "Doe", "(123) 456-7890", "john@example.com", "123 Main St")

    @patch('builtins.input', side_effect=["John", "Doe", "(123) 456-7890", "john@example.com", "123 Main St"])
    def test_create_single_contact_invalid_phone(self, mock_input):
        self.cli.phonebook.add_contact.side_effect = ValueError("Invalid phone number format")
        self.cli.create_single_contact()
        self.cli.phonebook.add_contact.assert_called_once_with("John", "Doe", "(123) 456-7890", "john@example.com", "123 Main St")

    @patch('builtins.input', side_effect=["data.csv"])
    def test_import_contacts(self, mock_input):
        self.cli.import_contacts()
        self.cli.phonebook.import_contacts.assert_called_once_with("data.csv")

    @patch('builtins.input', side_effect=["John"])
    def test_search_contact_by_name_or_phone_number(self, mock_input):
        self.cli.phonebook.search_contact.return_value = [Contact("John", "Doe", "(123) 456-7890", "john@example.com", "123 Main St")]
        self.cli.search_contact_by_name_or_phone_number()
        self.cli.phonebook.search_contact.assert_called_once_with("John")

    @patch('builtins.input', side_effect=["John", "1, 22,    2"])
    def test_delete_contact_by_search(self, mock_input):
        self.cli.phonebook.search_contact.return_value = [
            Contact("John", "Doe", "(123) 456-7890", "john@example.com", "123 Main St"),
            Contact("Jane", "Doe", "(123) 456-7891", "jane@example.com", "124 Main St"),
            Contact("Jim", "Beam", "(123) 456-7892", "jim@example.com", "125 Main St")
        ]
        self.cli.delete_contact_by_search()
        self.cli.phonebook.delete_contact.assert_any_call(self.cli.phonebook.search_contact.return_value[1])
        self.cli.phonebook.delete_contact.assert_any_call(self.cli.phonebook.search_contact.return_value[2])
        self.assertEqual(self.cli.phonebook.delete_contact.call_count, 2)

if __name__ == "__main__":
    unittest.main()