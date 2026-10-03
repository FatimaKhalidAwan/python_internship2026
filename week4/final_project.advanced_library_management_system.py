import json
from datetime import datetime, timedelta
BOOKS_FILE = "books.json"
MEMBERS_FILE = "members.json"
TRANSACTIONS_FILE = "transactions.json"

class Book:
    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.available = True
        self.issued_to = None
        self.issue_date = None
        self.return_date = None

    def to_dictionary(self):
        return {"book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "available": self.available,
            "issued_to": self.issued_to,
            "issue_date": self.issue_date,
            "return_date": self.return_date}

    def display_book(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Category:", self.category)
        if self.available:
            print("Status: Available")
        else:
            print("Status: Issued")
            print("Issued To:", self.issued_to)
            print("Issue Date:", self.issue_date)

class Member:
    def __init__(self, member_id, name, phone):
        self.member_id = member_id
        self.name = name
        self.phone = phone

    def to_dictionary(self):
        return {"member_id": self.member_id, "name": self.name, "phone": self.phone}

    def display_member(self):
        print("Member ID:", self.member_id)
        print("Name:", self.name)
        print("Phone:", self.phone)

books = []
members = []
transactions = []

def save_books():
    data = []
    for book in books:
        data.append(book.to_dictionary())
    with open(BOOKS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def save_members():
    data = []
    for member in members:
        data.append(member.to_dictionary())
    with open(MEMBERS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def save_transactions():
    with open(TRANSACTIONS_FILE, "w") as file:
        json.dump(transactions, file, indent=4)

def load_books():
    try:
        with open(BOOKS_FILE, "r") as file:
            data = json.load(file)
        for item in data:
            book = Book(item["book_id"], item["title"], item["author"], item["category"])
            book.available = item["available"]
            book.issued_to = item["issued_to"]
            book.issue_date = item["issue_date"]
            book.return_date = item["return_date"]
            books.append(book)
    except FileNotFoundError:
        print("No books file found. Starting with empty library.")
    except json.JSONDecodeError:
        print("Books file is empty or corrupted.")

def load_members():
    try:
        with open(MEMBERS_FILE, "r") as file:
            data = json.load(file)
        for item in data:
            member = Member(item["member_id"], item["name"], item["phone"])
            members.append(member)
    except FileNotFoundError:
        print("No members file found. Starting with no members.")
    except json.JSONDecodeError:
        print("Members file is empty or corrupted.")

def load_transactions():
    global transactions
    try:
        with open(TRANSACTIONS_FILE, "r") as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []
    except json.JSONDecodeError:
        transactions = []

def find_book(book_id):
    for book in books:
        if book.book_id.lower() == book_id.lower():
            return book
    return None

def find_member(member_id):
    for member in members:
        if member.member_id.lower() == member_id.lower():
            return member
    return None

def add_book():
    book_id = input("Enter Book ID: ")
    if find_book(book_id) is not None:
        print("A book with this ID already exists.")
        return
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    category = input("Enter Category: ")
    book = Book(book_id, title, author, category)
    books.append(book)
    save_books()
    print("Book added successfully!")

def view_books():
    if len(books) == 0:
        print("No books available.")
        return
    for book in books:
        book.display_book()

def search_book():
    search = input("Enter Book ID, Title or Author: ").lower()
    found = False
    for book in books:
        if (search in book.book_id.lower() or search in book.title.lower() or search in book.author.lower()):
            book.display_book()
            found = True
    if not found:
        print("No matching book found.")

def update_book():
    book_id = input("Enter Book ID: ")
    book = find_book(book_id)
    if book is None:
        print("Book not found.")
        return
    book.display_book()
    new_title = input("Enter new title: ")
    new_author = input("Enter new author: ")
    new_category = input("Enter new category: ")
    book.title = new_title
    book.author = new_author
    book.category = new_category
    save_books()
    print("Book updated successfully!")

def delete_book():
    book_id = input("Enter Book ID: ")
    book = find_book(book_id)
    if book is None:
        print("Book not found.")
        return
    if not book.available:
        print("This book is currently issued.")
        print("Return the book before deleting it.")
        return
    book.display_book()
    confirmation = input("Are you sure you want to delete this book? (yes/no): ").lower()
    if confirmation == "yes":
        books.remove(book)
        save_books()
        print("Book deleted successfully!")
    else:
        print("Delete operation cancelled.")

def add_member():
    member_id = input("Enter Member ID: ")
    if find_member(member_id) is not None:
        print("A member with this ID already exists.")
        return
    name = input("Enter Member Name: ")
    phone = input("Enter Phone Number: ")
    member = Member(member_id, name, phone)
    members.append(member)
    save_members()
    print("Member added successfully!")

def view_members():
    if len(members) == 0:
        print("No members available.")
        return
    for member in members:
        member.display_member()

def search_member():
    search = input("Enter Member ID or Name: ").lower()
    found = False
    for member in members:
        if (search in member.member_id.lower() or search in member.name.lower()):
            member.display_member()
            found = True
    if not found:
        print("Member not found.")

def delete_member():
    member_id = input("Enter Member ID: ")
    member = find_member(member_id)
    if member is None:
        print("Member not found.")
        return
    for book in books:
        if book.issued_to == member.member_id:
            print("This member currently has an issued book.")
            print("Return the book before deleting the member.")
            return
    member.display_member()
    confirmation = input("Are you sure you want to delete this member? (yes/no): ").lower()
    if confirmation == "yes":
        members.remove(member)
        save_members()
        print("Member deleted successfully!")
    else:
        print("Delete operation cancelled.")

def issue_book():
    book_id = input("Enter Book ID: ")
    book = find_book(book_id)
    if book is None:
        print("Book not found.")
        return
    if not book.available:
        print("This book is already issued.")
        print("Issued to:", book.issued_to)
        return
    member_id = input("Enter Member ID: ")
    member = find_member(member_id)
    if member is None:
        print("Member not found.")
        return
    current_date = datetime.now()
    return_date = current_date + timedelta(days=14)
    book.available = False
    book.issued_to = member.member_id
    book.issue_date = current_date.strftime("%Y-%m-%d")
    book.return_date = return_date.strftime("%Y-%m-%d")
    transaction = {"type": "Issue",
        "book_id": book.book_id,
        "book_title": book.title,
        "member_id": member.member_id,
        "member_name": member.name,
        "date": current_date.strftime("%Y-%m-%d"),
        "expected_return_date": return_date.strftime("%Y-%m-%d")}
    transactions.append(transaction)
    save_books()
    save_transactions()
    print("\nBook issued successfully!")
    print("Book:", book.title)
    print("Member:", member.name)
    print("Issue Date:", book.issue_date)
    print("Return Date:", book.return_date)

def return_book():
    book_id = input("Enter Book ID: ")
    book = find_book(book_id)
    if book is None:
        print("Book not found.")
        return
    if book.available:
        print("This book is already available.")
        return
    current_date = datetime.now()
    transaction = {"type": "Return",
        "book_id": book.book_id,
        "book_title": book.title,
        "member_id": book.issued_to,
        "date": current_date.strftime("%Y-%m-%d")}
    transactions.append(transaction)
    book.available = True
    book.issued_to = None
    book.issue_date = None
    book.return_date = None
    save_books()
    save_transactions()
    print("Book returned successfully!")

def view_issued_books():
    found = False
    for book in books:
        if not book.available:
            book.display_book()
            found = True
    if not found:
        print("No books are currently issued.")

def view_available_books():
    found = False
    for book in books:
        if book.available:
            book.display_book()
            found = True
    if not found:
        print("No books are currently available.")

def overdue_books():
    today = datetime.now().date()
    found = False
    for book in books:
        if not book.available and book.return_date is not None:
            return_date = datetime.strptime(book.return_date, "%Y-%m-%d").date()
            if today > return_date:
                print("Book:", book.title)
                print("Book ID:", book.book_id)
                print("Issued To:", book.issued_to)
                print("Due Date:", book.return_date)
                print("Status: OVERDUE")
                found = True
    if not found:
        print("No overdue books.")

def search_by_category():
    category = input("Enter category: ").lower()
    found = False
    for book in books:
        if book.category.lower() == category:
            book.display_book()
            found = True
    if not found:
        print("No books found in this category.")

def view_transactions():
    if len(transactions) == 0:
        print("No transactions found.")
        return
    for transaction in transactions:
        print("Transaction Type:",transaction["type"])
        print("Book:", transaction["book_title"])
        print("Book ID:", transaction["book_id"])
        print("Member ID:", transaction["member_id"])
        print("Date:", transaction["date"])
        if transaction["type"] == "Issue":
            print("Expected Return Date:", transaction["expected_return_date"])

def library_statistics():
    total_books = len(books)
    total_members = len(members)
    available_books = 0
    issued_books = 0
    for book in books:
        if book.available:
            available_books += 1
        else:
            issued_books += 1
    print("Total Books:", total_books)
    print("Available Books:", available_books)
    print("Issued Books:", issued_books)
    print("Total Members:", total_members)
    print("Total Transactions:", len(transactions))

def category_statistics():
    if len(books) == 0:
        print("No books available.")
        return
    categories = {}
    for book in books:
        category = book.category
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1
    for category, count in categories.items():
        print(category, ":", count, "book(s)")

def export_books_to_csv():
    import csv
    file_name = "books_report.csv"
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Book ID", "Title", "Author", "Category", "Available", "Issued To"])
        for book in books:
            writer.writerow([book.book_id, book.title, book.author, book.category, book.available, book.issued_to])
    print("Book report exported successfully!")
    print("File:", file_name)

def main():
    load_books()
    load_members()
    load_transactions()
    while True:
        print("ADVANCED LIBRARY MANAGEMENT SYSTEM")
        print("----- BOOK MANAGEMENT -----")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("----- MEMBER MANAGEMENT -----")
        print("6. Add Member")
        print("7. View Members")
        print("8. Search Member")
        print("9. Delete Member")
        print("----- ISSUE / RETURN -----")
        print("10. Issue Book")
        print("11. Return Book")
        print("12. View Issued Books")
        print("13. View Available Books")
        print("14. View Overdue Books")
        print("----- SEARCH / REPORTS -----")
        print("15. Search by Category")
        print("16. View Transaction History")
        print("17. Library Statistics")
        print("18. Category Statistics")
        print("19. Export Books to CSV")
        print("20. Exit")
        choice = input("Enter your choice (1-20): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            add_member()
        elif choice == "7":
            view_members()
        elif choice == "8":
            search_member()
        elif choice == "9":
            delete_member()
        elif choice == "10":
            issue_book()
        elif choice == "11":
            return_book()
        elif choice == "12":
            view_issued_books()
        elif choice == "13":
            view_available_books()
        elif choice == "14":
            overdue_books()
        elif choice == "15":
            search_by_category()
        elif choice == "16":
            view_transactions()
        elif choice == "17":
            library_statistics()
        elif choice == "18":
            category_statistics()
        elif choice == "19":
            export_books_to_csv()
        elif choice == "20":
            print("Thank you for using Advanced Library Management System!")
            break
        else:
            print("Invalid choice. Please select a number from 1-20.")

main()