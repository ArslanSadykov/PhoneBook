from Contact import Contact
from User import User

user = User()

while True:
    print("Выберите действие:")
    print("1. Добавить новый контакт.")
    print("2. Поделиться книжкой с другом.")
    print("3. Добавить друга.")
    print("4. Удалить друга.")
    print("5. Выход.")

    choice = input("Введите пункт действия: ")

    if choice == "1":
        name = input("Введите имя контакта: ")
        country_code = input("Введите код страны: ")
        phone_number = input("Введите номер телефона без кода страны: ")
        tag = input("Введите тег книжки: ")

        contact = Contact(name, country_code, phone_number)
        user.add_contact(contact, tag)

    elif choice == "2":
        friend_name = input("Введите имя друга: ")
        friend = User()
        friend.name = friend_name
        friend_phone_book_tag = input("Введите тег книжки друга: ")
        user.share_phone_book(friend, friend_phone_book_tag)

    elif choice == "3":
        friend_name = input("Введите имя друга: ")
        friend = User()
        friend.name = friend_name
        user.add_friend(friend)

    elif choice == "4":
        friend_name = input("Введите имя друга: ")
        friend = User()
        friend.name = friend_name
        user.remove_friend(friend)

    elif choice == "5":
        break

    else:
        print("Неверный выбор. Попробуйте снова.")