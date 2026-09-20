import json
import csv
from datetime import date
FILE_NAME = "expenses.json"
CSV_FILE = "expenses.csv"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    name = input("Enter expense name: ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
    category = input("Enter category: ")
    expense_date = date.today().isoformat()
    expense = {"name": name,
        "amount": amount,
        "category": category,
        "date": expense_date}
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    print("All Expenses:")
    if len(expenses) == 0:
        print("No expenses found.")
        return
    for i, expense in enumerate(expenses, start=1):
        print("Expense #", i)
        print("Name:", expense["name"])
        print("Amount:", expense["amount"])
        print("Category:", expense["category"])
        print("Date:", expense["date"])

def calculate_total(expenses):
    print("Total Expenses:")
    if len(expenses) == 0:
        print("No expenses available.")
        return
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print("Total Expenses:", round(total, 2))

def search_by_category(expenses):
    category = input("Enter category to search: ")
    found = False
    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print("Name:", expense["name"])
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])
            print("Date:", expense["date"])
            found = True
    if not found:
        print("No expenses found in this category.")

def delete_expense(expenses):
    if len(expenses) == 0:
        print("No expenses available.")
        return
    for i, expense in enumerate(expenses, start=1):
        print(i, ".", expense["name"], "-", expense["amount"], "-", expense["category"], "-", expense["date"])
    while True:
        try:
            choice = int(input("Enter expense number to delete: "))
            if 1 <= choice <= len(expenses):
                deleted_expense = expenses.pop(choice - 1)
                save_expenses(expenses)
                print("Deleted:", deleted_expense["name"])
                return
            else:
                print("Please enter a valid expense number.")
        except ValueError:
            print("Please enter a number.")

def monthly_expenses(expenses):
    print("Monthly Expenses:")
    if len(expenses) == 0:
        print("No expenses available.")
        return
    month = input("Enter month (YYYY-MM): ")
    total = 0
    for expense in expenses:
        if expense["date"].startswith(month):
            total += expense["amount"]
    print("Total expenses for", month, ":", round(total, 2))

def category_wise_total(expenses):
    print("Category-wise Total:")
    if len(expenses) == 0:
        print("No expenses available.")
        return
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    for category, total in category_totals.items():
        print(category, ":", round(total, 2))

def export_to_csv(expenses):
    print("Exporting expenses to CSV...")
    if len(expenses) == 0:
        print("No expenses available.")
        return
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "amount", "category", "date"])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses exported to", CSV_FILE)

def main():
    expenses = load_expenses()
    while True:
        print("EXPENSE TRACKER:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Search by Category")
        print("5. Delete Expense")
        print("6. Monthly Expenses")
        print("7. Category-wise Total")
        print("8. Export to CSV")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            search_by_category(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            monthly_expenses(expenses)
        elif choice == "7":
            category_wise_total(expenses)
        elif choice == "8":
            export_to_csv(expenses)
        elif choice == "9":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-9.")

main()