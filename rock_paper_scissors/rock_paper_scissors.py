import random


def main():
    """
    Main game loop for Rock, Paper, Scissors.
    Tracks wins, losses, and ties until the player decides to quit.
    """
    options = ("rock", "paper", "scissors")
    playing = True
    wins = losses = ties = 0  # Initialize score counters

    while playing:
        player = None
        computer = random.choice(options)  # Computer randomly selects

        # Prompt player until a valid choice is made
        while player not in options:
            player = input("Pick one (rock, paper, or scissors): ").lower()

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        # Determine the outcome of this round
        if player == computer:
            print("Tie!")
            ties += 1
        elif (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
        ):
            print("Win!")
            wins += 1
        else:
            print("Loss!")
            losses += 1

        # Ask if the player wants to play again
        while True:
            again = input("Play again (y/n)?: ").lower()
            if again in ("y", "n"):
                break
            print("Invalid input. Please enter 'y' or 'n'.")

        # Exit if player chooses not to continue
        if again != "y":
            print(
                f"Thank you for playing! Final stats - Wins: {wins}, Losses: {losses}, Ties: {ties}"
            )
            playing = False


if __name__ == "__main__":
    main()
