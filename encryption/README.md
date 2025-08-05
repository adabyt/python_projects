# Substitution Cipher (Python CLI Encryption Tool)

A basic encryption/decryption tool using a randomly shuffled substitution cipher. Users can encrypt messages by mapping each character to a shuffled key and decrypt them using the same key.

---

## Features

- Randomized substitution cipher key
- Supports letters, digits, punctuation, and whitespace
- Encrypts and decrypts messages using a consistent character map
- Key is printed after encryption (must be saved for decryption)
- Clean CLI interface with mode selection

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/adabyt/substitution-cipher.git
cd substitution-cipher
```

### Run the Program

```bash
python cipher.py
```

---

## Example Interaction

```plaintext
Welcome to the Simple Substitution Cipher

1. Encrypt a message
2. Decrypt a message
Choose an option (1 or 2): 1
Enter a message to encrypt: hello world!

Encrypted message: OUXxK7w)XK#o
Key used: &|VPGz... (store this key safely!)
```

---

## 📋 Requirements

- Python 3.x
- No external libraries required

---

## File Structure

```
substitution-cipher/
├── cipher.py       # Main encryption/decryption script
└── README.md       # Project documentation
```

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


---

## Acknowledgments

This project was inspired by and adapted from the [BroCode Python tutorials](https://www.youtube.com/c/BroCodez), which provide clear and practical guidance for beginner-level Python projects.
