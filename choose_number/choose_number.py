import random


def main():
    """
    Runs a number guessing game where the player tries to guess
    a randomly chosen number between low and high.
    Provides feedback to guess higher or lower until correct.
    """
    low = 1
    high = 100
    number = random.randint(low, high)  # Random number to guess
    guesses = 0  # Count of guesses made by player

    print("~~~~~~~~~~ NUMBER GUESSING GAME ~~~~~~~~~~")

    while True:
        guess = input(f"Enter a number between {low} and {high}: ")
        # Validate that input is a digit
        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            # Check if guess is within valid range
            if guess < low or guess > high:
                print("Number out of range")
            elif guess < number:
                print("HIGHER!")
            elif guess > number:
                print("LOWER!")
            else:
                # Correct guess
                print(f"CORRECT! The number was: {number}")
                print(f"Number of guesses: {guesses}")
                break
        else:
            print("Invalid input")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    main()
