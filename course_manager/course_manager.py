def main():
    """
    Main program loop that presents a menu for managing students and their enrolled courses.
    Uses a dictionary with student names as keys and a list of courses as values.
    """
    students = {}  # Dictionary to store student names and their courses

    # Map user choices to functions
    actions = {
        1: lambda: add(students),
        2: lambda: view(students),
        3: lambda: search(students),
        4: lambda: remove(students),
        5: exit_programme,
    }

    while True:
        show_menu()

        try:
            prompt = int(input("Please select an option (1–5): "))
            action = actions.get(prompt)

            if action:
                action()
            else:
                print("\nInvalid input. Please enter a number between 1–5.")
        except ValueError:
            print("\nInvalid input. Please enter a number between 1–5.")


def show_menu():
    """
    Display the main menu options to the user.
    """
    print("\nWelcome to the Student Course Manager!")
    print("1. Add a student")
    print("2. View all students")
    print("3. Search for a course for enrolled students")
    print("4. Remove a student")
    print("5. Exit")


def add(students):
    """
    Add a student and their courses to the students dictionary.
    The user can enter multiple courses for a student.

    Args:
        students (dict): Dictionary mapping student names to list of courses.
    """
    while True:
        courses = []

        student = input(
            "\nEnter the name of a student (first last) (or press q to return to main menu): "
        ).title()
        if student.lower() == "q":
            break

        # Collect courses for the student
        while True:
            course = input(
                "Enter a course the student is enrolled in (or press q to finish adding courses): "
            ).title()
            if course.lower() == "q":
                break
            courses.append(course)

        if courses:
            students[student] = sorted(courses)
            print(f"{student} added with courses: {', '.join(students[student])}")
        else:
            print("No courses entered. Student not added.")


def view(students):
    """
    Display all students and their enrolled courses in alphabetical order.

    Args:
        students (dict): Dictionary mapping student names to list of courses.
    """
    if not students:
        print("\nNo students to display.")
        return

    for student in sorted(students.keys()):
        print(f"\nStudent: {student}")
        print("Courses:")
        for course in students[student]:
            print(f" - {course}")


def search(students):
    """
    Search and display students enrolled in a specific course.

    Args:
        students (dict): Dictionary mapping student names to list of courses.
    """
    if not students:
        print("\nNo students to display.")
        return

    search_course = input(
        "\nEnter the course name to search for (or press q to return): "
    ).title()

    if search_course.lower() == "q":
        return

    found = False
    for student, courses in students.items():
        if search_course in courses:
            print(student)
            found = True

    if not found:
        print("\nNo students enrolled in that course.")


def remove(students):
    """
    Remove a student from the dictionary by name.

    Args:
        students (dict): Dictionary mapping student names to list of courses.
    """
    if not students:
        print("\nNo students to display.")
        return

    to_remove = input(
        "\nEnter the name of the student to remove (or press q to return): "
    ).title()

    if to_remove.lower() == "q":
        return

    if to_remove in students:
        del students[to_remove]
        print(f"\n{to_remove} removed.")
    else:
        print("\nNo matching student found.")


def exit_programme():
    """
    Exit the program gracefully.
    """
    print("\nExiting the program...")
    print("Goodbye!")
    exit()


if __name__ == "__main__":
    main()
