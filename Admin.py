import logging
from User import User

class Admin(User):
    def __init__(self, firstname):
        super().__init__(firstname)

    @staticmethod
    def add_contact_to_phone_book(contact, phone_book):
        phone_book.add_contact(contact)
        logging.info(f"Администратор добавил контакт {contact.user.firstname} в телефонную книгу {phone_book.tag}")

    @staticmethod
    def remove_contact_from_phone_book(contact, phone_book):
        phone_book.delete_contact(contact)
        logging.info(f"Администратор удалил контакт {contact.user.firstname} из телефонной книги {phone_book.tag}")
