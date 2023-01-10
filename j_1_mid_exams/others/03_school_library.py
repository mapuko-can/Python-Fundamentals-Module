# books = input().split("&")
#
# input_line = input()
#
# while input_line != "Done":
#
#     commands = input_line.split(" | ")
#     command = commands[0]
#
#     if command == "Add Book":
#         book_name = commands[1]
#         if book_name not in books:
#             books.insert(0, book_name)
#
#     elif command == "Take Book":
#         book_name = commands[1]
#         if book_name in books:
#             books.remove(book_name)
#
#     elif command == "Swap Books":
#         book_one = commands[1]
#         book_two = commands[2]
#         if book_one in books and book_two in books:
#             first_index = books.index(book_one)
#             second_index = books.index(book_two)
#             books[first_index], books[second_index] = books[second_index], books[first_index]
#
#     elif command == "Insert Book":
#         book_name = commands[1]
#         if book_name not in books:
#             books.append(book_name)
#
#     elif command == "Check Book":
#         index = int(commands[1])
#         if index in range(len(books)):
#             print(books[index])
#
#     input_line = input()
#
# print(", ".join(books))


def add_book(book):
    if book not in books:
        books.insert(0, book)


def take_book(book):
    if book in books:
        books.remove(book)


def swap_books(first_book, second_book):
    if book_one in books and book_two in books:
        first_index = books.index(first_book)
        second_index = books.index(second_book)
        books[first_index], books[second_index] = books[second_index], books[first_index]


def insert_book(book):
    if book not in books:
        books.append(book)


def check_book(index):
    if index in range(len(books)):
        print(books[index])


books = input().split("&")
input_line = input()

while input_line != "Done":
    commands = input_line.split(" | ")
    command = commands[0]

    if command == "Add Book":
        book_name = commands[1]
        add_book(book_name)

    elif command == "Take Book":
        book_name = commands[1]
        take_book(book_name)

    elif command == "Swap Books":
        book_one = commands[1]
        book_two = commands[2]
        swap_books(book_one, book_two)

    elif command == "Insert Book":
        book_name = commands[1]
        insert_book(book_name)

    elif command == "Check Book":
        i = int(commands[1])
        check_book(i)

    input_line = input()

print(", ".join(books))






