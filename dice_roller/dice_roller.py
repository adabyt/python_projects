import random

# Dictionary storing ASCII art for dice faces 1 through 6
dice_art = {
    1: (
        "┌───────────┐",
        "│           │",
        "│     ●     │",
        "│           │",
        "└───────────┘",
    ),
    2: (
        "┌───────────┐",
        "│  ●        │",
        "│           │",
        "│        ●  │",
        "└───────────┘",
    ),
    3: (
        "┌───────────┐",
        "│  ●        │",
        "│     ●     │",
        "│        ●  │",
        "└───────────┘",
    ),
    4: (
        "┌───────────┐",
        "│  ●     ●  │",
        "│           │",
        "│  ●     ●  │",
        "└───────────┘",
    ),
    5: (
        "┌───────────┐",
        "│  ●     ●  │",
        "│     ●     │",
        "│  ●     ●  │",
        "└───────────┘",
    ),
    6: (
        "┌───────────┐",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "└───────────┘",
    ),
}


def roll_dice(num_dice):
    """
    Roll 'num_dice' dice, each yielding a random number between 1 and 6.

    Args:
        num_dice (int): Number of dice to roll.

    Returns:
        list: List of integers representing dice roll results.
    """
    return [random.randint(1, 6) for _ in range(num_dice)]


def print_dice(dice):
    """
    Print ASCII art representation of the dice rolled side-by-side.

    Args:
        dice (list): List of dice roll results.
    """
    print()
    # Print each line of dice ASCII art horizontally aligned
    for line in range(5):
        for die in dice:
            print(dice_art[die][line], end=" ")
        print()
    print()


def main():
    """
    Main program function that prompts user for number of dice,
    rolls the dice, prints the results and total sum.
    """
    print("🎲 Welcome to the Dice Roller!\n")

    while True:
        try:
            num_dice = int(input("How many dice will you roll?: "))
            if num_dice <= 0:
                print("Please enter a positive number.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

    dice = roll_dice(num_dice)
    print_dice(dice)

    total = sum(dice)
    print(f"🎯 Total rolled: {total}\n")


if __name__ == "__main__":
    main()
