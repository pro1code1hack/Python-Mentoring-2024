def encrypt_message(message: str) -> str:
    """
    Encrypt the message by converting each character to its ASCII/Unicode code point.

    Args:
    message (str): The message to encrypt.

    Returns:
    str: The encrypted message as a string of ASCII/Unicode code points separated by spaces.
    """
    return ' '.join(str(ord(char)) for char in message)


def decrypt_message(encoded_message: str) -> str:
    """
    Decrypt the message by converting each ASCII/Unicode code point back to a character.

    Args:
    encoded_message (str): The encrypted message as a string of ASCII/Unicode code points separated by spaces.

    Returns:
    str: The decrypted message.
    """
    return ''.join(chr(int(code)) for code in encoded_message.split())


def ascii_unicode_converter() -> None:
    """
    Provides a menu to either encrypt or decrypt messages using ASCII/Unicode conversions.
    """
    print("# Menu:")
    print("1. Encrypt Messages")
    print("2. Decrypt Messages")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == '1':
        num_messages = int(input("Enter the number of messages to encrypt: ").strip())
        encrypted_messages = []

        for i in range(1, num_messages + 1):
            message = input(f"Enter message {i}: ").strip()
            encrypted_messages.append(encrypt_message(message))

        print("\n# Encrypt Output:")
        for i, encrypted_msg in enumerate(encrypted_messages, 1):
            print(f"Encrypted Message {i}: {encrypted_msg}")

    elif choice == '2':
        num_messages = int(input("Enter the number of messages to decrypt: ").strip())
        decrypted_messages = []

        for i in range(1, num_messages + 1):
            encoded_message = input(f"Enter message {i}: ").strip()
            decrypted_messages.append(decrypt_message(encoded_message))

        print("\n# Decrypt Output:")
        for i, decrypted_msg in enumerate(decrypted_messages, 1):
            print(f"Decrypted Message {i}: {decrypted_msg}")
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    ascii_unicode_converter()
