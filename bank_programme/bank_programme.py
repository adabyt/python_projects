def show_balance(balance):
    """
    Display the current balance formatted as currency.

    Args:
        balance (float): The current account balance.
    """
    print(f"\n💰 Your balance is: £{balance:.2f}\n")


def deposit():
    """
    Prompt user to enter an amount to deposit.
    Validates input and ensures the amount is positive.

    Returns:
        float: The amount deposited (0 if invalid input).
    """
    try:
        amount = float(input("Enter amount to deposit: £"))
        if amount < 0:
            print("Invalid amount. Must be positive.\n")
            return 0
        return amount
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        return 0


def withdraw(balance):
    """
    Prompt user to enter an amount to withdraw.
    Validates input, ensures the amount is positive and does not exceed balance.

    Args:
        balance (float): The current account balance.

    Returns:
        float: The amount withdrawn (0 if invalid input or insufficient funds).
    """
    try:
        amount = float(input("Enter amount to withdraw: £"))
        if amount > balance:
            print("Insufficient funds.\n")
            return 0
        elif amount < 0:
            print("Invalid amount. Must be positive.\n")
            return 0
        return amount
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        return 0


def main():
    """
    Main banking program loop.
    Displays menu, processes user choice for balance, deposit, withdrawal, or quit.
    """
    balance = 0.00

    while True:
        print("🔐 Welcome to the Bank CLI")
        print("1. Show Balance")
        print("2. Make Deposit")
        print("3. Make Withdrawal")
        print("4. Quit")

        try:
            choice = int(input("Choose an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.\n")
            continue

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            print("\nSession ended. Thank you for banking with us.\n")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.\n")


if __name__ == "__main__":
    main()
