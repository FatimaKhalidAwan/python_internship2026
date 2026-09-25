import pandas as pd
def create_data():
    data = {"Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Hamza"],
        "Roll Number": [101, 102, 103, 104, 105],
        "Marks": [85, 72, 39, 91, 68]}
    df = pd.DataFrame(data)
    return df

def display_students(df):
    print("All Students:")
    print(df)

def calculate_average(df):
    average = df["Marks"].mean()
    print("Average Marks:", round(average, 2))

def highest_marks(df):
    highest = df["Marks"].max()
    print("Highest Marks:", highest)

def lowest_marks(df):
    lowest = df["Marks"].min()
    print("Lowest Marks:", lowest)

def passing_students(df):
    passing = df[df["Marks"] >= 40]
    print("Passing Students:", len(passing))
    print(passing)

def failing_students(df):
    failing = df[df["Marks"] < 40]
    print("Failing Students:", len(failing))
    print(failing)

def top_student(df):
    highest_index = df["Marks"].idxmax()
    student_name = df.loc[highest_index, "Name"]
    highest_mark = df.loc[highest_index, "Marks"]
    print("Top Student:", student_name)
    print("Marks:", highest_mark)

def students_above_80(df):
    students = df[df["Marks"] > 80]
    print("Students Above 80 Marks:")
    print(students)

def add_grades(df):
    def calculate_grade(marks):
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"
    df["Grade"] = df["Marks"].apply(calculate_grade)

def main():
    df = create_data()
    print("===== STUDENT PERFORMANCE ANALYSIS =====")
    print("Total Students:", len(df))
    display_students(df)
    calculate_average(df)
    highest_marks(df)
    lowest_marks(df)
    passing_students(df)
    failing_students(df)
    top_student(df)
    students_above_80(df)
    add_grades(df)
    print("Students With Grades:")
    print(df)

main()