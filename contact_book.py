class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self):
        print("\n" + "="*50)
        print("ADD NEW CONTACT".center(50))
        print("="*50)
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()
        address = input("Address: ").strip()
        
        # Basic validation
        if not name or not phone:
            print("\nError: Name and phone are required!")
            return
        
        self.contacts.append({
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        })
        print(f"\n✅ Contact '{name}' added successfully!")
    
    def view_contacts(self):
        print("\n" + "="*50)
        print("CONTACT LIST".center(50))
        print("="*50)
        
        if not self.contacts:
            print("No contacts found!".center(50))
            return
        
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        print("="*50)
    
    def search_contact(self):
        print("\n" + "="*50)
        print("SEARCH CONTACTS".center(50))
        print("="*50)
        search_term = input("Enter name or phone number: ").strip().lower()
        
        if not search_term:
            print("Please enter a search term")
            return
        
        results = []
        for contact in self.contacts:
            if (search_term in contact['name'].lower() or 
                search_term in contact['phone']):
                results.append(contact)
        
        if not results:
            print("No matching contacts found!")
            return
        
        print("\nSEARCH RESULTS:")
        print("="*50)
        for i, contact in enumerate(results, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        print("="*50)
        return results
    
    def update_contact(self):
        results = self.search_contact()
        if not results:
            return
        
        try:
            choice = int(input("\nEnter contact number to update: "))
            contact = results[choice-1]
        except (ValueError, IndexError):
            print("Invalid selection!")
            return
        
        print("\nCurrent Details:")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        
        print("\nEnter new details (leave blank to keep current):")
        name = input(f"Name [{contact['name']}]: ").strip() or contact['name']
        phone = input(f"Phone [{contact['phone']}]: ").strip() or contact['phone']
        email = input(f"Email [{contact['email']}]: ").strip() or contact['email']
        address = input(f"Address [{contact['address']}]: ").strip() or contact['address']
        
        # Update original contact in main list
        for idx, c in enumerate(self.contacts):
            if c['name'] == contact['name'] and c['phone'] == contact['phone']:
                self.contacts[idx] = {
                    'name': name,
                    'phone': phone,
                    'email': email,
                    'address': address
                }
                break
        
        print(f"\n✅ Contact '{name}' updated successfully!")
    
    def delete_contact(self):
        results = self.search_contact()
        if not results:
            return
        
        try:
            choice = int(input("\nEnter contact number to delete: "))
            contact = results[choice-1]
        except (ValueError, IndexError):
            print("Invalid selection!")
            return
        
        # Confirm deletion
        confirm = input(f"\nAre you sure you want to delete {contact['name']}? (y/n): ").lower()
        if confirm != 'y':
            print("Deletion canceled")
            return
        
        # Remove from main list
        for idx, c in enumerate(self.contacts):
            if c['name'] == contact['name'] and c['phone'] == contact['phone']:
                del self.contacts[idx]
                print(f"\nContact '{contact['name']}' deleted successfully!")
                return

# Main program
def main():
    book = ContactBook()
    
    while True:
        print("\n" + "="*50)
        print("CONTACT BOOK".center(50))
        print("="*50)
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            book.add_contact()
        elif choice == '2':
            book.view_contacts()
        elif choice == '3':
            book.search_contact()
        elif choice == '4':
            book.update_contact()
        elif choice == '5':
            book.delete_contact()
        elif choice == '6':
            print("\nThank you for using Contact Book!")
            break
        else:
            print("Invalid choice! Please enter 1-6")

if __name__ == "__main__":
    main()