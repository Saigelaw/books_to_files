from utils import database

USER_CHOICE = """
ENTER: 
'a' to add a book
'l' to list all books
'r' to mark book as read
'd' to delete a book
'q' to quit

Your Choice: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            add_book_prompt()
        elif user_input == 'l':
            list_books_prompt()
        elif user_input == 'r':
            read_book_prompt()
        elif user_input == 'd':
            delete_book_prompt()
        elif user_input == 'q':
            print('Thank You and goodbye!')
        else:
            print('Incorrect choice selected. Please try again.')
        user_input = input(USER_CHOICE)


def add_book_prompt():
    name = input("Enter the title of the book: ")
    author = input("Enter the name of the author: ")

    database.add_book(name, author)


def list_books_prompt():
    books = database.show_books()
    for book in books:
        read = 'YES' if book['read'] is '1' else 'NO'
        print(f"{book['name']} written by {book['author']}, read {read}")


def read_book_prompt():
    name = input("Enter the book that you have finished reading: ")
    database.mark_read(name)


def delete_book_prompt():
    name = input("Enter the name of the book you want to delete: ")
    database.delete_book(name)
    print(f"{name} successfully deleted")


menu()