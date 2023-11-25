class PhoneBook:
    def __init__(self, tag):
        self.contacts = []
        self.tag = tag

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def filter_by_country_code(self, country_code):
        filtered_contacts = []
        for contact in self.contacts:
            if contact.country_code == country_code:
                filtered_contacts.append(contact)
        return filtered_contacts

    def filter_by_user(self, user):
        filtered_contacts = []
        for contact in self.contacts:
            if contact.user == user:
                filtered_contacts.append(contact)
        return filtered_contacts




