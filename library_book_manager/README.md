# Library Manager (Python CLI Project)

This is a command-line application for managing a small library of books. It allows users to:

- Add new books with title, author, and due date
- Search for books by title or author
- List all books, showing which are overdue
- Remove books from the collection

The program uses Python’s built-in `datetime` module to compare due dates with the current date, and handles invalid date inputs gracefully.

---

## 🔧 Features

- Add books with due dates
- Automatically flag books as overdue or not
- Search by title or author (case-insensitive)
- List all books in the collection
- Remove books by title or author
- Input validation for menu selection and date formats
- Modular design with reusable display formatting

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/adabyt/library-manager.git
cd library-manager
```

### 2. Run the Program
```bash
python library_manager.py
```

---

## 🖼️ Example Menu

```plaintext
1. Add a book
2. Search books
3. List all books
4. Remove a book
5. Exit
```

---

## 📋 Requirements

- Python 3.x
- No external libraries required

---

## 🗂️ File Structure

```
library-manager/
├── library_manager.py    # Main Python script
└── README.md             # Project documentation
```

---

## 📌 Notes

- Dates must be entered in the format: `YYYY-MM-DD` (e.g. 2025-04-25).
- Overdue books are detected by comparing their due date with the current system date.
- Invalid inputs are caught and handled with user-friendly messages.

---

## 📝 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute it.

---

## 🙋‍♂️ Author

**Amit Dipak Amin**  
[LinkedIn](https://www.linkedin.com/in/amitdipakamin)