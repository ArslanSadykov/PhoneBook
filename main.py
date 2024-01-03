import logging
from User import User
from Admin import Admin
from Contact import Contact
logging.basicConfig(level=logging.DEBUG)


user1 = User("Арслан")
user2 = User("Адель")
user3 = User("Ильмир")
admin = Admin(user1)

user1.add_friends(user2)

user1.add_phone_book('Семья')
user2.add_phone_book('Работа')

contact1 = Contact(user1, '7', '8006666666')
contact2 = Contact(user2, '8', '8007777777')

Admin.add_contact_to_phone_book(contact2, user1.phone_books['Семья'])
Admin.remove_contact_from_phone_book(contact2, user1.phone_books['Семья'])

user1.add_contact(contact1, 'Семья')
user2.add_contact(contact2, 'Работа')

user1.share_phone_books(user2, 'Семья')
user1.share_phone_books(user3, 'Семья')

filtered_contacts_user = user1.phone_books['Семья'].filter_user(user='user1')

filtered_contacts_code = user1.phone_books['Семья'].filter_country_code(country_code='7')
