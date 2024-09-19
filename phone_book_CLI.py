# This file will provide a command-line interface for users to interact with the phonebook application.
from phone_book import PhoneBook
from contact import Contact
from datetime import datetime

ATTRIBUTE_DICT = {"1": "first_name", "2": "last_name", "3": "created_at", "4": "updated_at"}
ORDER_DICT = {"1": False, "2": True}
GROUP_DICT = {"1": "first_name", "2": "last_name", "3": "phone_number"}

class PhoneBookCLI:
    def __init__(self):
        self.phonebook = PhoneBook()

    def create_single_contact(self):
        first_name = input("First Name (Required): ")
        last_name = input("Last Name (Required): ")
        phone_number = input("Phone Number (Required, Format (###) ###-####): ")
        email = input("Email (Optional): ")
        address = input("Address (Optional): ")

        try:
            self.phonebook.add_contact(first_name, last_name, phone_number, email, address)
            print("Contact added successfully.")
            print(f"New contact: {self.phonebook.contacts[-1]}")
        except ValueError as ve:
            print(f"Error: {ve}")

    def import_contacts(self):
        csv_file = input("Enter CSV file path: ")
        try:
            self.phonebook.import_contacts(csv_file)
            print("Contacts imported successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")
    
    def search_contact_by_name_or_phone_number(self):
        keyword = input("Search by name or phone number: ")
        results = self.phonebook.search_contact(keyword)
        if results:
            for idx, contact in enumerate(results):
                print(f"{idx}: {contact}")
        else:
            print("No contacts found.")

    def search_contact_by_updated_time(self):
        '''
            Search contacts by time range.
            Print the contacts created or updated within the specified time range.
        '''
        while True:
            # Get valid start and end time from the user
            start_time = self.__get_valid_time("Enter start time (Format: YYYY-MM-DD) or type 'menu' to return to the main menu: ")
            if start_time is None:
                return
            end_time = self.__get_valid_time("Enter end time (Format: YYYY-MM-DD) or type 'menu' to return to the main menu: ")
            if end_time is None:
                return
        
            # Check if the start time is greater than the end time
            if start_time > end_time:
                print("Error: Start time cannot be greater than end time.")
                input_str = input("Type 'menu' to return to the main menu or press ENTER to continue: ")
                if input_str.lower() == "menu":
                    return
                continue
            else:
                break  
        # Search for contacts within the specified time range
        contacts = self.phonebook.search_contact_by_updated_time(start_time, end_time)

        # Print the search results
        for contact in contacts:
            print(contact)
    
    def search_contact_by_created_time(self):
        '''
            Search contacts by time range.
            Print the contacts created within the specified time range.
        '''
        while True:
            # Get valid start and end time from the user
            start_time = self.__get_valid_time("Enter start time (Format: YYYY-MM-DD) or type 'menu' to return to the main menu: ")
            if start_time is None:
                return
            end_time = self.__get_valid_time("Enter end time (Format: YYYY-MM-DD) or type 'menu' to return to the main menu: ")
            if end_time is None:
                return
        
            # Check if the start time is greater than the end time
            if start_time > end_time:
                print("Error: Start time cannot be greater than end time.")
                input_str = input("Type 'menu' to return to the main menu or press ENTER to continue: ")
                if input_str.lower() == "menu":
                    return
                continue
            else:
                break  
        # Search for contacts within the specified time range
        contacts = self.phonebook.search_contact_by_created_time(start_time, end_time)

        # Print the search results
        for contact in contacts:
            print(contact)

    def group_contacts_by_initial_letter(self, key):
        contacts = self.phonebook.group_contacts_by_initial_letter(key)
        for initial, contact_list in contacts.items():
            print(f"{len(contact_list)} contacts with {key} starting with '{initial}':")
            for contact in contact_list:
                print(contact)
    
    def group_contacts_by_area_code(self):
        contacts = self.phonebook.group_contacts_by_area_code()
        for area_code, contact_list in contacts.items():
            print(f"{len(contact_list)} contacts with phone number area code '{area_code}':")
            for contact in contact_list:
                print(contact)

    def list_grouped_contacts(self):
        while True:
            print("1. Group by First Name")
            print("2. Group by Last Name")
            print("3. Group by Phone Area Code")
            print("4. Return to main menu")
            choice = input("Enter your choice: ")
            if choice == "4":
                return
            if choice <= "0" or choice > "4":
                print("Invalid choice. Please enter a number between 1 and 3.")
                continue
            elif choice == "1" or choice == "2":
                key = ATTRIBUTE_DICT[choice]
                self.group_contacts_by_initial_letter(key)
            else:
                self.group_contacts_by_area_code()

    
    def list_all_contacts(self):
        contacts = self.phonebook.list_contacts()
        # Note that print(contacts) will result in printing None at the end.
        for contact in contacts:
            print(contact)
    
    def list_sorted_contacts(self):
        while True:
            print("1. Sort by First Name")
            print("2. Sort by Last Name")
            print("3. Sort by Created Time")
            print("4. Sort by Updated Time")
            print("5. Return to main menu")
            choice = input("Enter your choice: ")
            if choice == "5":
                return
            if choice <= "0" or choice > "5":
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
            else:
                # Get the attribute and order for sorting
                key = ATTRIBUTE_DICT[choice]
                while True:
                    print("1. Ascending order")
                    print("2. Descending order")
                    choice = input("Enter your choice: ")
                    if choice <= "0" or choice > "2":
                        print("Invalid choice. Please enter a number between 1 and 2.")
                        continue
                    else:
                        order = ORDER_DICT[choice]
                        break
                break
        contacts = self.phonebook.sort_contacts(key, order)
        print("Contacts sorted by", key, "in", "ascending" if not order else "descending", "order:")
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

        try:
            self.phonebook.update_contact(contact, first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, address=address)
            print("Contact updated successfully.")
            print(f"Updated contact: {contact}")
        except ValueError as ve:
            print(f"Error: {ve}")
            return

    def delete_contact_by_search(self):
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
        contact_index = input("Enter contact index to delete (Seperate multiple choices with ','): ")

        contact_indices = [int(idx.strip()) for idx in contact_index.split(',')]

        for idx in contact_indices:

            # If the contact index is invalid, print message and return
            if idx < 0 or idx >= len(results):
                print(f"Contact index {idx} is invalid.")   
                continue
            
            contact = results[idx]

            # Delete the contact
            self.phonebook.delete_contact(contact)

            # Print the deleted contact
            print(f"Contact deleted:{contact}")

    def delete_all_contacts(self):
        print("Are you sure you want to delete all contacts?(y/n)")
        choice = input("Enter your choice: ")
        if choice.lower() == "y":
            self.phonebook.delete_all_contacts()
            print("All contacts deleted.")
        else: 
            return
    
    def main(self):
        while True:
            print("1. Add Contact")
            print("2. Search Contact")
            print("3. List Contacts")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Sort Contacts")
            print("7. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("1. Add contacts manually")
                print("2. Load contacts from CSV file")
                print("Enter any other key to return to the main menu")
                choice = input("Enter your choice: ")
                if choice == "1":
                    while True:
                        self.create_single_contact()
                        choice = input("Add another contact? (y/n): ")
                        if choice.lower() != "y":
                            break
                elif choice == "2":
                    while True:
                        self.import_contacts()
                        choice = input("Import another CSV file? (y/n): ")
                        if choice.lower() != "y":
                            break

            elif choice == "2":
                print("1. Search by name or phone number")
                print("2. Search by updated time range")
                print("3. Search by created time range")
                print("Enter any other key to return to the main menu")
                choice = input("Enter your choice: ")
                if choice == "1":
                    while True:
                        self.search_contact_by_name_or_phone_number()
                        choice = input("Search another contact? (y/n): ")
                        if choice.lower() != "y":
                            break
                elif choice == "2":
                    while True:
                        self.search_contact_by_updated_time()
                        choice = input("Search another contact? (y/n): ")
                        if choice.lower() != "y":
                            break
                elif choice == "3":
                    while True:
                        self.search_contact_by_created_time()
                        choice = input("Search another contact? (y/n): ")
                        if choice.lower() != "y":
                            break

            elif choice == "3":
                contacts = self.phonebook.list_contacts()
                # Print message if no contacts are found
                if not contacts:
                    print("No contacts found.")
                    continue
                print("1. List all contacts")
                print("2. List contacts in groups")
                print("Enter any other key to return to the main menu")
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.list_all_contacts()
                elif choice == "2":
                    self.list_grouped_contacts()

            elif choice == "4":
                self.update_contact()

            elif choice == "5":
                while True:
                    print("1. Search to delete contacts")
                    print("2. Delete all contacts")
                    print("Enter any other key to return to the main menu")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        while True:
                            self.delete_contact_by_search()
                            choice = input("Delete other contacts by search? (y/n): ")
                            if choice.lower() != "y":
                                break
                    elif choice == "2":
                        self.delete_all_contacts()
                        print("All contacts deleted.")
                        break
                    else:
                        break
                    

            elif choice == "6":
                self.list_sorted_contacts()

            elif choice == "7":
                break
    
    def __get_valid_time(self, prompt):
        while True:
            time_str = input(prompt)
            if time_str.lower() == "menu":
                return None
            try:
                time = datetime.strptime(time_str, "%Y-%m-%d")
                return time
            except ValueError:
                print("Invalid time format. Please use YYYY-MM-DD.")


if __name__ == "__main__":
    phonebook_cli = PhoneBookCLI()
    phonebook_cli.main()

