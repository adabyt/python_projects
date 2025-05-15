import random

# List of possible words to guess
words = (
    "apple",
    "banana",
    "blueberry",
    "coconut",
    "kiwi",
    "mango",
    "peach",
    "pear",
    "pineapple",
    "plum",
)

# ASCII art representing the hangman at different stages
hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\"),
}


def display_man(wrong_guesses):
    """Print the hangman ASCII art based on number of wrong guesses."""
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    """Display the current guessed word state with underscores and guessed letters."""
    print("Word: " + " ".join(hint))


def display_answer(answer):
    """Display the complete answer word."""
    print("Answer: " + " ".join(answer))


def main():
    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    print(f"You can make up to {len(hangman_art) - 1} wrong guesses.\n")

    # Randomly select a word from the list
    answer = random.choice(words)
    # Create the initial hint with underscores for each letter
    hint = ["_"] * len(answer)
    wrong_guesses = 0  # Counter for incorrect guesses
    guessed_letters = set()  # Track letters guessed so far

    # Main game loop
    while True:
        display_man(wrong_guesses)  # Show hangman art for current wrong guesses
        display_hint(hint)  # Show the current guessed word state
        print(
            f"Guessed letters: {' '.join(sorted(guessed_letters))}\n"
        )  # Show guessed letters

        guess = input("Enter a letter: ").lower()

        # Validate input: must be a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.\n")
            continue

        # Check if letter was already guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.\n")
            continue

        guessed_letters.add(guess)

        # Update hint if guess is correct
        if guess in answer:
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
        else:
            # Increase wrong guess count if incorrect
            wrong_guesses += 1

        # Check for win condition (no underscores left)
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("\nCongratulations! YOU WIN!")
            break
        # Check for lose condition (max wrong guesses)
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            print("\nGAME OVER! YOU LOSE!")
            print(f"The word was: {answer}")
            break


if __name__ == "__main__":
    main()
