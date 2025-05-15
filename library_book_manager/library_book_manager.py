from datetime import datetime, date


def main():
    """
    Main loop that presents a menu for managing library books.
    Books are stored as dictionaries in a list.
    """
    books = []

    # Map menu choices to functions
    actions = {
        1: lambda: add_book(books),
        2: lambda: search_books(books),
        3: lambda: list_books(books),
        4: lambda: remove_book(books),
        5: exit_programme,
    }

    while True:
        print_menu()
        try:
            prompt = int(input("Please select an option (1-5): "))
            action = actions.get(prompt)
            if action:
                action()
            else:
                print("\nInvalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("\nInvalid input. Please try again.")


def print_menu():
    """
    Display the menu options to the user.
    """
    print("\nWelcome to the Library Manager!")
    print("1. Add a book")
    print("2. Search books")
    print("3. List all books")
    print("4. Remove a book")
    print("5. Exit")


def add_book(books):
    """
    Prompt user to add a book with title, author, and due date.
    Validates date format and determines if book is overdue.

    Args:
        books (list): List to store book dictionaries.
    """
    while True:
        title = input("\nEnter the book title: ").title()
        author = input("Enter the author's name: ").title()
        due_date_input = input("Enter the due date (YYYY-MM-DD): ")

        try:
            due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
            overdue = "Yes" if due_date < date.today() else "No"

            book = {
                "title": title,
                "author": author,
                "due_date": due_date.strftime("%Y-%m-%d"),
                "overdue_status": overdue,
            }

            books.append(book)
            print("Book added successfully.")
            break

        except ValueError:
            print("Error: Please use the format YYYY-MM-DD.")


def search_books(books):
    """
    Search books by title or author and display matches.

    Args:
        books (list): List of book dictionaries.
    """
    if not books:
        print("\nNo books to search.")
        return

    while True:
        choice = input("\nSearch by (1) Title, (2) Author, or 'q' to quit: ").lower()

        if choice == "1":
            keyword = input("Enter the book title: ").title()
            matches = [book for book in books if book["title"] == keyword]

        elif choice == "2":
            keyword = input("Enter the author's name: ").title()
            matches = [book for book in books if book["author"] == keyword]

        elif choice == "q":
            break
        else:
            print("Invalid input.")
            continue

        if matches:
            for book in matches:
                display_book(book)
        else:
            print("No matching books found.")


def list_books(books):
    """
    Display all books currently stored.

    Args:
        books (list): List of book dictionaries.
    """
    if not books:
        print("\nNo books to list.")
        return

    print("\nListing all books:")
    for book in books:
        display_book(book)


def remove_book(books):
    """
    Remove a book by title or author.

    Args:
        books (list): List of book dictionaries.
    """
    if not books:
        print("\nNo books to remove.")
        return

    to_remove = input(
        "Enter the title or author of the book to remove (or 'q' to quit): "
    ).title()

    if to_remove.lower() == "q":
        return

    removed = False
    for book in books[:]:  # Iterate over a copy to safely remove from list
        if book["title"] == to_remove or book["author"] == to_remove:
            books.remove(book)
            print("Book removed.")
            removed = True

    if not removed:
        print("No matching book found.")


def display_book(book):
    """
    Print details of a book.

    Args:
        book (dict): Book dictionary.
    """
    print(
        f"""
Title: {book['title']}
Author: {book['author']}
Due Date: {book['due_date']}
Overdue: {book['overdue_status']}
"""
    )


def exit_programme():
    """
    Exit the program gracefully.
    """
    print("\nExiting the program... Goodbye!")
    exit()


if __name__ == "__main__":
    main()
