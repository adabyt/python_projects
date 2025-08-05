# Slot Machine Game (Python CLI Project)

A simple, fun slot machine simulation built in Python. This command-line game allows users to place bets, spin a randomized slot machine, and win payouts based on matching emoji symbols.

---

## Features

- Random emoji symbols for each spin (🍒, 🍉, 🍋, 🔔, ⭐)
- Payout system based on symbol rarity
- User balance tracking and betting system
- Input validation for bets and replay prompts
- Modular, well-structured code

---

## Payouts

| Symbol | Match 3 Pays |
|--------|--------------|
| 🍒     | 2× your bet  |
| 🍉     | 3× your bet  |
| 🍋     | 5× your bet  |
| 🔔     | 10× your bet |
| ⭐     | 20× your bet |

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/adabyt/slot-machine-game.git
cd slot-machine-game
```

### Run the game

```bash
python slot_machine.py
```

---

## Example Interaction

```plaintext
*************************
*** SLOT MACHINE GAME ***
***  🍒 🍉 🍋 🔔 ⭐  ***
*************************

Current balance: £100
Place your bet: £10
****** SPINNING ******

************
🍋 | 🍋 | 🍋
************

CONGRATULATIONS! You won £50!
Would you like to play again? (Y/N): y
...
```

---

## Requirements

- Python 3.x
- No external libraries required

---

## File Structure

```
slot-machine-game/
├── slot_machine.py     # Main game script
└── README.md           # Project documentation
```

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


---

## Acknowledgments

This project was inspired by and adapted from the [BroCode Python tutorials](https://www.youtube.com/c/BroCodez), which provided valuable guidance on building engaging CLI applications in Python.
