# Bank Programme (Python CLI Project)

A simple command-line banking simulation built in Python. This program allows users to view their balance, deposit money, and withdraw funds — all via a clean, menu-driven interface.

---

## Features

- View your current balance
- Make deposits and withdrawals
- Input validation for numeric and valid transaction amounts
- Clear user feedback and clean interface
- Modular code using reusable functions

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/adabyt/bank-programme.git
cd bank-programme
```

### Run the program

```bash
python bank.py
```

---

## Example Interaction

```plaintext
Welcome to the Bank CLI
1. Show Balance
2. Make Deposit
3. Make Withdrawal
4. Quit
Choose an option (1-4): 2
Enter amount to deposit: £100
Your balance is: £100.00

Choose an option (1-4): 3
Enter amount to withdraw: £50
Your balance is: £50.00

Choose an option (1-4): 4
Session ended. Thank you for banking with us.
```

---

## Requirements

- Python 3.x
- No external libraries required

---

## File Structure

```
bank-programme/
├── bank.py        # Main script
└── README.md      # Project documentation
```

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


---

## Acknowledgments

This project was inspired by and adapted from the [BroCode Python tutorials](https://www.youtube.com/c/BroCodez), which provided excellent guidance for building beginner-friendly CLI applications in Python.
