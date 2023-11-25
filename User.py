class User:
    def __init__(self):
        self.friends = []
        self.phone_books = {}

    def add_contact(self, contact, phone_book_tag):
        if phone_book_tag in self.phone_books:
            phone_book = self.phone_books[phone_book_tag]
            phone_book.add_contact(contact)
        else:
            print("Тег телефонной книжки не найден.")

    def share_phone_book(self, friend, phone_book_tag):
        if friend in self.friends:
            if phone_book_tag in self.phone_books:
                friend.phone_books[phone_book_tag] = self.phone_books[phone_book_tag]
            else:
                print("Тег телефонной книжки не найден.")
        else:
            print("Данный пользователь не является вашим другом.")

    def add_friend(self, friend):
        self.friends.append(friend)

    def remove_friend(self, friend):
        self.friends.remove(friend)