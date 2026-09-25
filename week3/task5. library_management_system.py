class Book:

    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True

    def display_book(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        if self.available:
            print("Status: Available")
        else:
            print("Status: Issued")

books = []

def find_book(book_id):
    for book in books:
        if book.book_id == book_id:
            return book
    return None

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book_id = input("Enter book ID: ")
    if find_book(book_id) is not None:
        print("A book with this ID already exists.")
        return
    book = Book(title, author, book_id)
    books.append(book)
    print("Book added successfully!")

def view_books():
    if len(books) == 0:
        print("No books available.")
        return
    for book in books:
        book.display_book()

def search_book():
    search = input("Enter Book ID or title: ").lower()
    found = False
    for book in books:
        if (book.book_id.lower() == search or
                book.title.lower() == search):
            book.display_book()
            found = True
    if not found:
        print("Book not found.")

def issue_book():
    book_id = input("Enter Book ID: ")
    book = find_book(book_id)
    if book is None:
        print("Book not found.")
    elif book.available:
        book.available = False
        print("Book issued successfully.")
    else:
        print("Book is already issued.")

def return_book():
    book_id = input("Enter Book ID: ")
    book = find_book(book_id)
    if book is None:
        print("Book not found.")
    elif not book.available:
        book.available = True
        print("Book returned successfully.")
    else:
        print("Book is already available.")

def delete_book():
    book_id = input("Enter Book ID: ")
    book = find_book(book_id)
    if book is None:
        print("Book not found.")
    else:
        books.remove(book)
        print("Book deleted successfully.")

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        print("Thank you for using Library Management System!")
        break
    else:
        print("Invalid choice. Please select 1-7.")