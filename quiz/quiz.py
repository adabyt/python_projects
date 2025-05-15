def main():
    """
    Runs a multiple-choice quiz game.
    Presents questions and options, validates user input,
    tracks score, and displays results at the end.
    """

    # List of quiz questions
    questions = (
        "1. What is the tallest mountain on Earth?",
        "2. How many wives did Henry VIII have?",
        "3. What is the largest animal on Earth?",
        "4. When did WW1 start?",
        "5. What is the national flower of Japan",
        "6. What is the smallest planet in our Solar System",
        "7. What is the hottest temperature in °C recorded on Earth?",
        "8. What is the capital of Iceland?",
        "9. How many elements are in the periodic table?",
        "10. Who was the first James Bond?",
    )

    # Corresponding multiple choice options for each question
    options = (
        ["A. Kilimanjaro", "B. Mount Everest", "C. K2", "D. Mount Etna"],
        ["A. 5", "B. 6", "C. 7", "D. 8"],
        ["A. Blue Whale", "B. Giraffe", "C. Asian Elephant", "D. Crocodile"],
        ["A. 1910", "B. 1912", "C. 1914", "D. 1916"],
        ["A. Ume", "B. Cherry Blossom", "C. Sakura", "D. Chrysanthemum"],
        ["A. Uranus", "B. Venus", "C. Mercury", "D. Pluto"],
        ["A. 55.7", "B. 56.7", "C. 57.7", "D. 58.7"],
        ["A. Reykjavik", "B. Keflavik", "C. Akranes", "D. Kopavogur"],
        ["A. 115", "B. 116", "C. 117", "D. 118"],
        ["A. Roger Moore", "B. Barry Nelson", "C. Bob Holness", "D. Sean Connery"],
    )

    # Correct answers aligned with questions
    answers = ["B", "B", "A", "C", "D", "C", "B", "A", "D", "C"]

    score = 0  # Initialize score counter
    guesses = []  # Store user's guesses for review

    # Loop through questions using enumerate for indexing
    for idx, question in enumerate(questions):
        print("------------------------------------------------------------")
        print(question)

        # Display all available options for the current question
        for option in options[idx]:
            print(option)

        # Prompt user until valid input (A-D) is entered
        while True:
            guess = input("Pick an option (A, B, C, or D): ").upper()
            if guess in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")

        guesses.append(guess)

        # Check if guess is correct and update score
        if guess == answers[idx]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"The correct answer was: {answers[idx]}")

    print("------------------------------------------------------------")
    print("\n~~~~~~~~~~ RESULTS ~~~~~~~~~~")
    print("ANSWERS: ", " ".join(answers))
    print("GUESSES: ", " ".join(guesses))

    # Calculate and display final score percentage
    final_score = (score / len(questions)) * 100
    print(f"Final score: {final_score}%")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    main()
