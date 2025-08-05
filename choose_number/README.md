# Number Guessing Game (Python CLI Project)

A simple command-line number guessing game implemented in Python. The player tries to guess a randomly generated number between a specified range, receiving feedback whether their guess should be higher or lower.

---

## Features

- Random number generation within a user-defined range (default 1-100)
- Input validation to ensure numeric input and valid range
- Counts and displays the number of guesses taken
- User-friendly CLI with clear prompts and feedback

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/adabyt/number-guessing-game.git
cd number-guessing-game
```

### Run the Program

```bash
python number_guessing_game.py
```

---

## Example Interaction

```plaintext
~~~~~~~~~~ NUMBER GUESSING GAME ~~~~~~~~~~
Enter a number between 1 and 100: 50
HIGHER!
Enter a number between 1 and 100: 75
LOWER!
Enter a number between 1 and 100: 63
CORRECT! The number was: 63
Number of guesses: 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

---

## Requirements

- Python 3.x
- No external libraries required

---

## File Structure

```
number-guessing-game/
├── number_guessing_game.py   # Main Python script
└── README.md                 # Project documentation
```

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---


## Acknowledgments

This project was inspired by and adapted from the [BroCode Python tutorials](https://www.youtube.com/c/BroCodez), which provided valuable guidance on building CLI applications in Python.
