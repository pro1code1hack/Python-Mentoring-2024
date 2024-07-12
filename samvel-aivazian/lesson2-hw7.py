# Adjusting the script to use actual input for the ASCII/Unicode Converter task.

def encrypt_message(message: str) -> str:
    # Encrypt the message by converting each character to its ASCII/Unicode code point
    return ' '.join(str(ord(char)) for char in message)


def decrypt_message(encoded_message: str) -> str:
    # Decrypt the message by converting each ASCII/Unicode code point back to a character
    return ''.join(chr(int(code)) for code in encoded_message.split())


def ascii_unicode_converter() -> None:
    print("# Menu:")
    print("1. Encrypt Messages")
    print("2. Decrypt Messages")

    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        num_messages = int(input("Enter the number of messages to encrypt: "))
        encrypted_messages = []

        for i in range(1, num_messages + 1):
            message = input(f"Enter message {i}: ")
            encrypted_messages.append(encrypt_message(message))

        print("\n# Encrypt Output:")
        for i, encrypted_msg in enumerate(encrypted_messages, 1):
            print(f"Encrypted Message {i}: {encrypted_msg}")

    elif choice == '2':
        num_messages = int(input("Enter the number of messages to decrypt: "))
        decrypted_messages = []

        for i in range(1, num_messages + 1):
            encoded_message = input(f"Enter message {i}: ")
            decrypted_messages.append(decrypt_message(encoded_message))

        print("\n# Decrypt Output:")
        for i, decrypted_msg in enumerate(decrypted_messages, 1):
            print(f"Decrypted Message {i}: {decrypted_msg}")


ascii_unicode_converter()
