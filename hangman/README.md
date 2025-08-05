# Hangman Game (Python CLI Project)

A classic Hangman word guessing game implemented in Python. The player tries to guess the hidden word one letter at a time before running out of allowed wrong guesses.

---

## Features

- Random word selection from a predefined list
- ASCII art visualization of the hangman state
- Tracks guessed letters and prevents repeated guesses
- Input validation for single alphabetic characters
- Clear win/lose conditions with informative messages

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/adabyt/hangman-game.git
cd hangman-game
```

### Run the Program

```bash
python hangman_game.py
```

---

## Example Interaction

```plaintext
Welcome to Hangman!
Try to guess the word, one letter at a time.
You can make up to 6 wrong guesses.

   
Word: _ _ _ _ _

Guessed letters: 

Enter a letter: a
 o 
Word: a _ _ _ _

Guessed letters: a

Enter a letter: e
 o 
 | 
Word: a _ _ _ e

Guessed letters: a e

... (game continues) ...
```

---

## Requirements

- Python 3.x
- No external libraries required

---

## File Structure

```
hangman-game/
├── hangman_game.py      # Main Python script
└── README.md            # Project documentation
```

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## Acknowledgments

This project was inspired by and adapted from the [BroCode Python tutorials](https://www.youtube.com/c/BroCodez), which provided valuable guidance on building CLI applications in Python.
