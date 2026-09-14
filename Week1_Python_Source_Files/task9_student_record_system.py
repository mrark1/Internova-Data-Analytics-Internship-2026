"""
Task 9: Mini Python Project
------------------------------
Student Record Management System

Features:
1. Add student details.
2. Display all student records.
3. Search a student by name.
4. Delete a student record.

Data is stored using a list of dictionaries.
"""

students = []  # Each student is stored as a dictionary


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    branch = input("Enter branch: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "branch": branch,
        "marks": marks
    }
    students.append(student)
    print(f"\nStudent '{name}' added successfully!\n")


def display_students():
    if not students:
        print("\nNo student records found.\n")
        return

    print("\n----- All Student Records -----")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Roll No: {student['roll_no']}, "
              f"Branch: {student['branch']}, Marks: {student['marks']}")
    print()


def search_student():
    name = input("Enter the name of the student to search: ")
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"\nStudent Found -> Name: {student['name']}, "
                  f"Roll No: {student['roll_no']}, Branch: {student['branch']}, "
                  f"Marks: {student['marks']}\n")
            found = True
            break
    if not found:
        print(f"\nNo student found with the name '{name}'.\n")


def delete_student():
    name = input("Enter the name of the student to delete: ")
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print(f"\nStudent '{name}' deleted successfully!\n")
            return
    print(f"\nNo student found with the name '{name}'.\n")


def menu():
    while True:
        print("===== Student Record Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Name")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    menu()
