import random


def spin_row():
    """Return a list of 3 randomly chosen symbols to simulate a slot machine row."""
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    """Print the slot machine row in a visually formatted layout."""
    print()
    print("************")
    print(" | ".join(row))
    print("************")
    print()


def generate_payout(row, bet):
    """
    Check if all symbols match.
    Return the payout amount based on the matching symbol's value.
    """
    if row[0] == row[1] == row[2]:
        payouts = {"🍒": 2, "🍉": 3, "🍋": 5, "🔔": 10, "⭐": 20}
        return bet * payouts.get(row[0], 0)
    return 0  # No win


def main():
    balance = 100  # Starting player balance

    print("\n*************************")
    print("*** SLOT MACHINE GAME ***")
    print("***  🍒 🍉 🍋 🔔 ⭐  ***")
    print("*************************\n")

    # Main game loop
    while balance > 0:
        print(f"Current balance: £{balance}")
        bet = input("Place your bet: £")

        # Validate input is a number
        if not bet.isdigit():
            print("Please enter a valid number.\n")
            continue

        bet = int(bet)

        # Check bet amount is valid
        if bet <= 0:
            print("Bet must be greater than £0.\n")
            continue

        if bet > balance:
            print("Insufficient funds.\n")
            continue

        # Deduct bet and spin the reels
        balance -= bet
        print("****** SPINNING ******\n")
        row = spin_row()
        print_row(row)

        # Calculate payout based on result
        payout = generate_payout(row, bet)

        if payout > 0:
            print(f"CONGRATULATIONS! You won £{payout}!\n")
        else:
            print("Sorry! Better luck next time.\n")

        # Update balance with any winnings
        balance += payout

        # Ask if the player wants to continue
        while True:
            play_again = input("Would you like to play again? (Y/N): ").strip().upper()
            if play_again in ("Y", "N"):
                break
            print("Invalid input. Please enter 'Y' or 'N'.")

        if play_again != "Y":
            print("Thank you for playing!")
            break

    print(f"Final balance: £{balance}")


if __name__ == "__main__":
    main()
