import random
import string

# Define the full set of characters that can be encrypted/decrypted
CHARACTERS = list(" " + string.punctuation + string.digits + string.ascii_letters)


def generate_key():
    """
    Generate a shuffled substitution key based on the CHARACTERS list.
    Returns:
        list: A shuffled list representing the cipher key.
    """
    key = CHARACTERS.copy()
    random.shuffle(key)
    return key


def encrypt(plain_text, key):
    """
    Encrypts plain_text using the provided substitution key.

    Args:
        plain_text (str): The message to encrypt.
        key (list): The substitution key.

    Returns:
        str: The encrypted cipher text.
    """
    cipher_text = ""
    for char in plain_text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            cipher_text += key[index]
        else:
            # Characters not in CHARACTERS are added unchanged
            cipher_text += char
    return cipher_text


def decrypt(cipher_text, key):
    """
    Decrypts cipher_text using the provided substitution key.

    Args:
        cipher_text (str): The message to decrypt.
        key (list): The substitution key.

    Returns:
        str: The decrypted plain text.
    """
    plain_text = ""
    for char in cipher_text:
        if char in key:
            index = key.index(char)
            plain_text += CHARACTERS[index]
        else:
            # Characters not in key are added unchanged
            plain_text += char
    return plain_text


def main():
    """
    Main interface for the substitution cipher program.
    Prompts the user to encrypt or decrypt messages.
    """
    key = generate_key()
    print("Welcome to the Simple Substitution Cipher\n")
    print("1. Encrypt a message")
    print("2. Decrypt a message")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        plain_text = input("Enter a message to encrypt: ")
        cipher = encrypt(plain_text, key)
        print(f"\nEncrypted message: {cipher}")
        print(f"Key used: {''.join(key)} (store this to decrypt!)")
    elif choice == "2":
        cipher_text = input("Enter a message to decrypt: ")
        key_str = input("Paste the key used to encrypt the message: ")
        key = list(key_str)
        plain = decrypt(cipher_text, key)
        print(f"\nDecrypted message: {plain}")
    else:
        print("Invalid option. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
