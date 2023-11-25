from User import User

class Admin(User):
    def add_friend(self, other):
        raise Exception('Администраторы не могут иметь друзей.')

    def add_contact_to_phonebook(self, contact, phonebook):
        phonebook.contacts_list.append(contact)

    def delete_contact_to_phonebook(self,contact, phonebook):
        phonebook.contacts_list.remove(contact)