# Concession Stand Simulator (Python CLI Project)

A simple Python command-line program that simulates a movie theater concession stand. Users can view a menu, select items, and get a detailed receipt with itemized pricing.

---

## Features

- Displays a formatted menu with prices
- Accepts user orders interactively
- Capitalized and itemized receipt output
- Tracks quantity and calculates totals
- Validates input and handles unknown items
- Uses Python data structures (`dict`, `list`) cleanly

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/adabyt/concession-stand.git
cd concession-stand
```

### Run the program

```bash
python concession_stand.py
```

---

## Example Output

```plaintext
-------- MENU --------
Popcorn : £5.00
Nachos  : £3.50
Sweets  : £2.00
Soda    : £2.50
Water   : £0.00
----------------------

Select an item (q to quit): popcorn
Select an item (q to quit): soda
Select an item (q to quit): soda
Select an item (q to quit): water
Select an item (q to quit): q

~~~~~ YOUR ORDER ~~~~~
Popcorn x1 = £5.00
Soda    x2 = £5.00
Water   x1 = £0.00
----------------------
Order total: £10.00
~~~~~~~~~~~~~~~~~~~~~~
```

---

## Requirements

- Python 3.x
- No external libraries required

---

## File Structure

```
concession-stand/
├── concession_stand.py   # Main game script
└── README.md             # Project documentation
```

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


---

## Acknowledgments

This project was inspired by and adapted from the [BroCode Python tutorials](https://www.youtube.com/c/BroCodez), which provided helpful guidance on beginner Python CLI programs.
