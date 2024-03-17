class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone='', email='', social_media={}, **kwargs):
        super().__init__(**kwargs)
        self.phone = phone
        self.email = email
        self.social_media = social_media

    def update_social_media(self, platform, username):
        self.social_media[platform] = username

    def get_social_media(self):
        return self.social_media


class MailSender:  #Maxim class. it cannot exist on its own
    def send_mail(self,message):
        print("Sending email to: ", self.email) 

class EmailableContact(Contact, MailSender): # multi-level inheritance
    pass


# Creating Contact instances
c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")


e = EmailableContact("John Smith", "jsmith@example.net")
# Creating a new ContactList containing c1, c2, and c3
c = ContactList([c1, c2, c3])

# Searching for contacts with name 'John' in the ContactList
john_contacts = c.search('John')

# Printing the names and emails of matching contacts
for contact in john_contacts:
    print("Name:", contact.name)
    print("Email:", contact.email)
    print()
e.send_mail("Hello, test email here")
# Example usage

friend = Friend(
    name='Amogu Uduka',
    phone='662-497-4975',
    email='auduka@gmu.edu',
    social_media={'Twitter': '@UdukaA', 'Instagram': 'amogujuduka'}
)

# Adding more social media information
friend.update_social_media('LinkedIn', 'Amogu J. Uduka')
print(friend.get_social_media())





