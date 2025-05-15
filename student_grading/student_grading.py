def main():
    """
    Main program loop presenting a menu to manage student grades.
    Uses a dictionary mapping student names to grades.
    """
    student_grades = {}

    actions = {
        1: lambda: add_student(student_grades),
        2: lambda: view_students(student_grades),
        3: lambda: calculate_average(student_grades),
        4: lambda: remove_student(student_grades),
        5: lambda: exit_program(),
    }

    print("Welcome to the Student Grading System!")

    while True:
        print_menu()
        try:
            prompt = int(input("Enter an option (1-5): "))
            if prompt in actions:
                actions[prompt]()
            else:
                print("Invalid option. Please select between 1-5.")
        except ValueError:
            print("Invalid input. Please try again.")


def print_menu():
    """Display menu options."""
    print("\nMenu:")
    print("1. Add a student")
    print("2. View all students")
    print("3. Calculate average grade")
    print("4. Remove a student")
    print("5. Exit")


def add_student(student_grades):
    """
    Add a student and grade to the dictionary.

    Args:
        student_grades (dict): Maps student names to grades.
    """
    student, grade = add()
    student_grades[student] = grade


def add():
    """
    Prompt user to input a student name and valid grade (0-100).
    Returns:
        tuple: (student_name, grade)
    """
    student = input("Enter the name of a student: ")

    while True:
        try:
            grade = int(input("Enter the grade for that student (0-100): "))
            if 0 <= grade <= 100:
                return student, grade
            else:
                print("Invalid input. Please enter a number between 0-100.")
        except ValueError:
            print("Invalid input. Please enter a number between 0-100.")


def view_students(student_grades):
    """
    Display all students and their grades.

    Args:
        student_grades (dict): Maps student names to grades.
    """
    if not student_grades:
        print("\nNothing to display.")
    else:
        print()
        for student, grade in student_grades.items():
            print(f"{student}: {grade}")


def calculate_average(student_grades):
    """
    Calculate and print the average grade of all students.

    Args:
        student_grades (dict): Maps student names to grades.
    """
    if student_grades:
        average_grade = sum(student_grades.values()) / len(student_grades)
        print(f"\nThe average grade for all students is: {average_grade:.2f}")
    else:
        print("\nNo students in the list to calculate average.")


def remove_student(student_grades):
    """
    Remove a student by name from the dictionary.

    Args:
        student_grades (dict): Maps student names to grades.
    """
    while True:
        to_remove = input("\nEnter the student to remove: ")
        if to_remove in student_grades:
            student_grades.pop(to_remove)
            print(f"{to_remove} has been removed from the list.")
            break
        else:
            print("That student cannot be found. Please try again.")


def exit_program():
    """Exit the program gracefully."""
    print("\nGoodbye!")
    exit()


if __name__ == "__main__":
    main()
