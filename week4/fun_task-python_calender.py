import calendar
print(".....PYTHON CALENDAR.....")
while True:
    print("1. Display Monthly Calendar")
    print("2. Display Full Year Calendar")
    print("3. Check Leap Year")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        year = int(input("Enter year: "))
        month = int(input("Enter month (1-12): "))
        if month >= 1 and month <= 12:
            print(".....MONTHLY CALENDAR.....")
            print(calendar.month(year, month))
        else:
            print("Invalid month. Please enter 1-12.")
    elif choice == "2":
        year = int(input("Enter year: "))
        print("\n.....FULL YEAR CALENDAR.....")
        print(calendar.calendar(year))
    elif choice == "3":
        year = int(input("Enter year: "))
        if calendar.isleap(year):
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    elif choice == "4":
        print("Thank you for using Python Calendar!")
        break
    else:
        print("Invalid choice. Please select 1-4.")