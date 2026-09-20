class BankAccount:
    def __init__(self, holder_name, account_number, balance=0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Money deposited successfully.")
        else:
            print("Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Money withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Amount must be greater than 0.")

    def check_balance(self):
        print("Current Balance:", round(self.balance, 2))

    def display_information(self):
        print("Account Holder:", self.holder_name)
        print("Account Number:", self.account_number)
        print("Balance:", round(self.balance, 2))

accounts = []

def find_account(account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None

while True:
    print("===== Bank Account System =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Account Information")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        print("Create Account:")
        holder_name = input("Enter account holder name: ")
        account_number = input("Enter account number: ")
        account = BankAccount(holder_name, account_number)
        accounts.append(account)
        print("Account created successfully!")
    elif choice == "2":
        account_number = input("Enter account number: ")
        account = find_account(account_number)
        if account is not None:
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Account not found.")
    elif choice == "3":
        account_number = input("Enter account number: ")
        account = find_account(account_number)
        if account is not None:
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Account not found.")
    elif choice == "4":
        account_number = input("Enter account number: ")
        account = find_account(account_number)
        if account is not None:
            account.check_balance()
        else:
            print("Account not found.")
    elif choice == "5":
        account_number = input("Enter account number: ")
        account = find_account(account_number)
        if account is not None:
            account.display_information()
        else:
            print("Account not found.")
    elif choice == "6":
        print("Thank you for using Bank Account System!")
        break
    else:
        print("Invalid choice. Please select 1-6.")