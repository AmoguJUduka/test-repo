class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

# Creating Contact instances
c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")

# Creating a new ContactList containing c1, c2, and c3
c = ContactList([c1, c2, c3])

# Searching for contacts with name 'John' in the ContactList
john_contacts = c.search('John')

# Printing the names and emails of matching contacts
for contact in john_contacts:
    print("Name:", contact.name)
    print("Email:", contact.email)
    print()