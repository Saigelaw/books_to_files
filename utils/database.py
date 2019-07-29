"""
concerned with adding and retrieving books into the system
"""
books_file = 'books.txt'


def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f"{name},{author},0\n")


def show_books():
    with open(books_file, 'r') as file_read:
        books_saved = [book.strip().split(',') for book in file_read.readlines()]

    return [
        {'name': book[0], 'author': book[1], 'read': book[2]}
        for book in books_saved
    ]


def mark_read(name):
    books = show_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
    # global books  # tells python that global variable is being used as a local variable
    books = show_books()
    books = [book for book in books if book['name'] != name]  # Add each book that book['name'] != name
    _save_all_books(books)

# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)
