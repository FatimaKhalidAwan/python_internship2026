def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Please enter a valid mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_total_marks(subjects):
    total = 0
    for subject in subjects:
        marks = get_marks(subject)
        total += marks
    return total


def percentage_calculator(marks_obtained, total_marks):
    return (marks_obtained / total_marks) * 100


def grade_calculator(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 85:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 45:
        return 'D'
    else:
        return 'F'


def result_calculator(percentage):
    if percentage >= 45:
        return 'Passed'
    else:
        return 'Failed'


def calculate_results(name, subjects):
    total_marks = get_total_marks(subjects)
    percentage = percentage_calculator(total_marks,len(subjects) * 100)
    grade = grade_calculator(percentage)
    result = result_calculator(percentage)
    print("Student Result:")
    print("Name:", name)
    print("Total Marks:", total_marks, "/", len(subjects) * 100)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Result:", result)
    return percentage

subjects = ['Math','Science','English','Physics','Chemistry','History','Islamiat','Geography']
students = []
while True:
    name = input("Enter your name: ")
    percentage = calculate_results(name, subjects)
    students.append((name, percentage))
    choice = input("Do you want to enter another student? (yes/no): ")
    if choice.lower() != "yes":
        break
highest_student = max(students, key=lambda student: student[1])
print("Highest Percentage Student:")
print("Student:", highest_student[0])
print("Percentage:", round(highest_student[1], 2), "%")

