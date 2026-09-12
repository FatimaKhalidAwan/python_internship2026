import json
FILE_NAME = "students.json"

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def add_student(students):
    print("Add Student")
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    for student in students:
        if student["roll_number"] == roll_number:
            print("A student with this roll number already exists.")
            return
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
    grade = calculate_grade(marks)
    student = {
        "name": name,
        "roll_number": roll_number,
        "marks": marks,
        "grade": grade}
    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    print("All Students")
    if len(students) == 0:
        print("No students found.")
        return
    for student in students:
        print("Name:", student["name"])
        print("Roll Number:", student["roll_number"])
        print("Marks:", student["marks"])
        print("Grade:", student["grade"])


def search_student(students):
    roll_number = input("Enter roll number to search a student: ")
    for student in students:
        if student["roll_number"] == roll_number:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_number"])
            print("Marks:", student["marks"])
            print("Grade:", student["grade"])
            return
    print("Student not found.")


def update_student(students):
    roll_number = input("Enter student's roll number to update: ")
    for student in students:
        if student["roll_number"] == roll_number:
            print("Current Name:", student["name"])
            new_name = input("Enter new name: ")
            print("Current Marks:", student["marks"])
            while True:
                try:
                    new_marks = float(input("Enter new marks (0-100): "))
                    if 0 <= new_marks <= 100:
                        break
                    else:
                        print("Marks must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")
            student["name"] = new_name
            student["marks"] = new_marks
            student["grade"] = calculate_grade(new_marks)
            save_students(students)
            print("Student updated successfully!")
            return
    print("Student not found.")


def delete_student(students):
    roll_number = input("Enter roll number to delete student's data: ")
    for student in students:
        if student["roll_number"] == roll_number:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return
    print("Student not found.")


def calculate_average(students):
    if len(students) == 0:
        print("No students available.")
        return
    total_marks = 0
    for student in students:
        total_marks += student["marks"]

    average = total_marks / len(students)

    print("Average Marks:", round(average, 2))


def main():
    students = load_students()
    while True:
        print("Welcome to Student Management System:")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Average Marks")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            calculate_average(students)
        elif choice == "7":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice. Please select 1-7.")

main()