# This file will provide a command-line interface for users to interact with the phonebook application.
from phone_book import PhoneBook
from contact import Contact

class PhoneBookCLI:
    def __init__(self):
        self.phonebook = PhoneBook()

    def add_contact(self):
        #TODO: Add validation for everything
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email (Optional): ")
        address = input("Address (Optional): ")

        contact = Contact(first_name, last_name, phone_number, email, address)
        self.phonebook.add_contact(contact)

    def search_contact(self):
        keyword = input("Search by name or phone number: ")
        results = self.phonebook.search_contact(keyword)
        if results:
            for idx, contact in enumerate(results):
                print(f"{idx}: {contact}")
        else:
            print("No contacts found.")

    def list_contacts(self):
        contacts = self.phonebook.list_contacts()
        # Note that print(contacts) will result in printing None at the end.
        for contact in contacts:
            print(contact)

    def update_contact(self):
        # Search cantact using keyword
        keyword = input("Search by name or phone number: ")
        results = self.phonebook.search_contact(keyword)
        # If no contacts found, print message and return
        if not results:
            print("No contacts found.")
            return
        # Print the search results
        for idx, contact in enumerate(results):
            print(f"{idx}: {contact}")
        # Select contact to update
        contact_index = int(input("Enter contact index to update: "))
        # If the contact index is invalid, print message and return
        if contact_index < 0 or contact_index >= len(results):
            print("Invalid contact index.")   
            return
        
        contact = results[contact_index]

        # Update the contact
        first_name = input("First Name (leave blank to keep unchanged): ")
        last_name = input("Last Name (leave blank to keep unchanged): ")
        phone_number = input("Phone Number (leave blank to keep unchanged): ")
        email = input("Email (Optional, leave blank to keep unchanged): ")
        address = input("Address (Optional, leave blank to keep unchanged): ")

        self.phonebook.update_contact(contact, first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, address=address)

        # Print the updated contact
        print(f"Contact updated:{contact}")

    def delete_contact(self):
        # Search cantact using keyword
        keyword = input("Search by name or phone number: ")
        results = self.phonebook.search_contact(keyword)
        # If no contacts found, print message and return
        if not results:
            print("No contacts found.")
            return
        # Print the search results
        for idx, contact in enumerate(results):
            print(f"{idx}: {contact}")
        # Select contact to delete
        contact_index = int(input("Enter contact index to delete: "))
        # If the contact index is invalid, print message and return
        if contact_index < 0 or contact_index >= len(results):
            print("Invalid contact index.")   
            return
        
        contact = results[contact_index]

        # Delete the contact
        self.phonebook.delete_contact(contact)

        # Print the deleted contact
        print(f"Contact deleted:{contact}")

    def main(self):
        while True:
            print("1. Add Contact")
            print("2. Search Contact")
            print("3. List Contacts")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("1. Add Contact manually")
                print("2. Load contacts from CSV file")
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.add_contact()
                elif choice == "2":
                    csv_file = input("Enter CSV file name: ")
                    self.phonebook.import_contacts(csv_file)

            elif choice == "2":
                self.search_contact()

            elif choice == "3":
                self.list_contacts()

            elif choice == "4":
                self.update_contact()

            elif choice == "5":
                self.delete_contact()

            elif choice == "6":
                break


if __name__ == "__main__":
    phonebook_cli = PhoneBookCLI()
    phonebook_cli.main()

