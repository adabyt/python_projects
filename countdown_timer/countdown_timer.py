import time


def countdown_timer(seconds):
    """
    Counts down from a given number of seconds,
    displaying the remaining time in HH:MM:SS format.

    Args:
        seconds (int): Number of seconds to count down from.
    """
    for remaining in range(seconds, 0, -1):
        hrs = remaining // 3600
        mins = (remaining % 3600) // 60
        secs = remaining % 60
        print(f"{hrs:02}:{mins:02}:{secs:02}")
        time.sleep(1)
    print("BEEP BEEP BEEP")


def count(end, start=0):
    """
    Simple countdown from end to start by 1-second intervals,
    printing numbers directly without formatting.

    Args:
        end (int): Number to count down from.
        start (int): Number to count down to (default 0).
    """
    for x in range(end, start, -1):
        print(x)
        time.sleep(1)
    print("BEEP BEEP BEEP")


def main():
    """
    Main function to prompt user for countdown seconds and run timer.
    Validates input to ensure a positive integer is provided.
    """
    print("Welcome to the Countdown Timer\n")
    try:
        timer = int(input("Enter the number of seconds to count down: "))
        if timer <= 0:
            print("Please enter a positive number.")
            return
        print()
        countdown_timer(timer)
    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
