import os


def main():
    """
    Main loop to display menu and execute user-selected contact management actions.
    """
    filename = "contacts.txt"  # File where contacts are stored

    # Mapping menu options to functions
    actions = {
        1: lambda: add_contact(filename),
        2: lambda: view_contacts(filename),
        3: lambda: search_contacts(filename),
        4: lambda: edit_contacts(filename),
        5: lambda: remove_contact(filename),
        6: exit_program,
    }

    while True:
        print_menu()
        try:
            choice = int(input("Choose an option (1-6): "))
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")


def print_menu():
    """
    Displays the menu options to the user.
    """
    print("\nContact Manager")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contacts")
    print("4. Edit contact")
    print("5. Remove contact")
    print("6. Exit")


def add_contact(filename):
    """
    Add a new contact to the file.

    Args:
        filename (str): The filename where contacts are stored.
    """
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    with open(filename, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added!")


def view_contacts(filename):
    """
    Read and display all contacts from the file.

    Args:
        filename (str): The filename where contacts are stored.
    """
    if not os.path.exists(filename):
        print("No contacts found.")
        return

    with open(filename, "r") as file:
        lines = file.readlines()

    if not lines:
        print("No contacts to display.")
        return

    for line in lines:
        name, phone, email = line.strip().split(",")
        print(f"Name: {name}, Phone: {phone}, Email: {email}")


def search_contacts(filename):
    """
    Search for contacts by name (case-insensitive) and display matches.

    Args:
        filename (str): The filename where contacts are stored.
    """
    if not os.path.exists(filename):
        print("No contacts found.")
        return

    search_term = input("Enter name to search for: ").strip().lower()

    with open(filename, "r") as file:
        matches = [line.strip() for line in file if search_term in line.lower()]

    if matches:
        for match in matches:
            name, phone, email = match.split(",")
            print(f"Name: {name}, Phone: {phone}, Email: {email}")
    else:
        print("No matching contacts found.")


def edit_contacts(filename):
    """
    Edit existing contact information.

    Args:
        filename (str): The filename where contacts are stored.
    """
    if not os.path.exists(filename):
        print("No contacts found.")
        return

    name_to_edit = input("Enter the name of the contact to edit: ").strip().lower()

    with open(filename, "r") as file:
        matches = [line.strip() for line in file if name_to_edit in line.lower()]

    if matches:
        for match in matches:
            name, phone, email = match.split(",")
            print(f"Current info — Name: {name}, Phone: {phone}, Email: {email}")

            new_name = input("Enter new name (or press ENTER to keep): ").strip()
            new_phone = input(
                "Enter new phone number (or press ENTER to keep): "
            ).strip()
            new_email = input("Enter new email (or press ENTER to keep): ").strip()

            # Keep original info if input is blank
            if new_name == "":
                new_name = name
            if new_phone == "":
                new_phone = phone
            if new_email == "":
                new_email = email

            with open(filename, "r") as file:
                filedata = file.read()

            # Replace old contact info with new contact info
            filedata = filedata.replace(name, new_name)
            filedata = filedata.replace(phone, new_phone)
            filedata = filedata.replace(email, new_email)

            with open(filename, "w") as file:
                file.write(filedata)
    else:
        print("No matching contacts found.")


def remove_contact(filename):
    """
    Remove a contact by name.

    Args:
        filename (str): The filename where contacts are stored.
    """
    if not os.path.exists(filename):
        print("No contacts found.")
        return

    name_to_remove = input("Enter the name of the contact to remove: ").strip().lower()

    with open(filename, "r") as file:
        lines = file.readlines()

    # Keep lines that do NOT match the contact to remove
    new_lines = [line for line in lines if name_to_remove not in line.lower()]

    with open(filename, "w") as file:
        file.writelines(new_lines)

    print("Contact removed (if it existed).")


def exit_program():
    """
    Exit the program gracefully.
    """
    print("Goodbye!")
    exit()


if __name__ == "__main__":
    main()
