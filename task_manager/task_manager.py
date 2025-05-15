from datetime import datetime, date


def main():
    """
    Main loop presenting a menu for task management:
    adding, viewing, filtering, removing tasks, or exiting.
    Tasks are stored as dictionaries in a list.
    """
    tasks = []
    actions = {
        1: lambda: add_task(tasks),
        2: lambda: view_tasks(tasks),
        3: lambda: filter_tasks(tasks),
        4: lambda: remove_task(tasks),
        5: exit_program,
    }

    print("Welcome to the Task Manager!")

    while True:
        print_menu()
        try:
            choice = int(input("\nPlease select an option (1-5): "))
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")


def print_menu():
    """
    Display the menu options to the user.
    """
    print("\nMenu:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Filter tasks by priority")
    print("4. Remove a task")
    print("5. Exit")


def add_task(tasks):
    """
    Add a new task with description, due date, and priority.
    Validates date format and priority input.

    Args:
        tasks (list): List of task dictionaries.
    """
    description = input("\nEnter task description (or 'q' to return): ").strip()
    if description.lower() == "q":
        return

    # Validate due date input
    while True:
        due_date_input = input("Enter due date (YYYY-MM-DD): ").strip()
        try:
            due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    # Validate priority input
    while True:
        priority = input("Enter priority (High, Medium, Low): ").strip().lower()
        if priority in ["high", "medium", "low"]:
            break
        else:
            print("Invalid priority. Use High, Medium, or Low.")

    task = {
        "description": description,
        "due_date": due_date,
        "priority": priority,
    }
    tasks.append(task)
    print("Task added.")


def view_tasks(tasks):
    """
    Display all tasks sorted by due date with ID, description, due date, and priority.

    Args:
        tasks (list): List of task dictionaries.
    """
    if not tasks:
        print("\nNo tasks to display.")
        return

    print("\nAll Tasks:")
    print(f"{'ID':<3} {'Description':<30} {'Due Date':<12} {'Priority':<6}")
    print("-" * 55)
    for idx, task in enumerate(sorted(tasks, key=lambda t: t["due_date"]), start=1):
        print(
            f"{idx:<3} {task['description'][:29]:<30} {task['due_date']}   {task['priority'].capitalize():<6}"
        )


def filter_tasks(tasks):
    """
    Filter tasks by priority and display matching tasks.

    Args:
        tasks (list): List of task dictionaries.
    """
    if not tasks:
        print("\nNo tasks to filter.")
        return

    level = (
        input("Filter by priority (High, Medium, Low) or 'q' to return: ")
        .strip()
        .lower()
    )
    if level == "q":
        return
    if level not in ["high", "medium", "low"]:
        print("Invalid input. Please enter High, Medium, or Low.")
        return

    filtered = [task for task in tasks if task["priority"] == level]

    if not filtered:
        print(f"\nNo tasks with {level.capitalize()} priority.")
        return

    print(f"\nTasks with {level.capitalize()} priority:")
    print(f"{'ID':<3} {'Description':<30} {'Due Date':<12}")
    print("-" * 50)
    for idx, task in enumerate(filtered, start=1):
        print(f"{idx:<3} {task['description'][:29]:<30} {task['due_date']}")


def remove_task(tasks):
    """
    Remove a task by its displayed ID.

    Args:
        tasks (list): List of task dictionaries.
    """
    if not tasks:
        print("\nNo tasks to remove.")
        return

    view_tasks(tasks)
    while True:
        try:
            idx = input(
                "\nEnter the ID of the task to remove (or 'q' to return): "
            ).strip()
            if idx.lower() == "q":
                return
            idx = int(idx)
            if 1 <= idx <= len(tasks):
                removed_task = tasks.pop(idx - 1)
                print(f"Task '{removed_task['description']}' removed.")
                return
            else:
                print(f"Invalid ID. Please enter a number between 1 and {len(tasks)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def exit_program():
    """
    Exit the program gracefully.
    """
    print("\nExiting Task Manager. Goodbye!")
    exit()


if __name__ == "__main__":
    main()
