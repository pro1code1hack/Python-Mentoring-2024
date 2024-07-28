import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class AsciiUnicodeConverter:
    @staticmethod
    def encrypt_message(message):
        encrypted = ' '.join(str(ord(char)) for char in message)
        return encrypted

    @staticmethod
    def decrypt_message(message):
        decrypted = ''.join(chr(int(code)) for code in message.split())
        return decrypted

    def encrypt_messages(self, messages):
        encrypted_messages = [self.encrypt_message(message) for message in messages]
        return encrypted_messages

    def decrypt_messages(self, messages):
        decrypted_messages = [self.decrypt_message(message) for message in messages]
        return decrypted_messages


def main():
    logging.info("Menu:")
    logging.info("1. Encrypt Messages")
    logging.info("2. Decrypt Messages")
    logging.info("Choose an option (1 or 2): ")
    choice = input().strip()

    converter = AsciiUnicodeConverter()

    if choice == '1':
        logging.info("Enter the number of messages to encrypt: ")
        num_messages = int(input())
        messages = []
        for i in range(num_messages):
            logging.info(f"Enter message {i + 1}: ")
            message = input()
            messages.append(message)
        encrypted_messages = converter.encrypt_messages(messages)
        for i, encrypted_message in enumerate(encrypted_messages, 1):
            logging.info(f"Encrypted Message {i}: {encrypted_message}")
    elif choice == '2':
        logging.info("Enter the number of messages to decrypt: ")
        num_messages = int(input())
        messages = []
        for i in range(num_messages):
            logging.info(f"Enter message {i + 1}: ")
            message = input()
            messages.append(message)
        decrypted_messages = converter.decrypt_messages(messages)
        for i, decrypted_message in enumerate(decrypted_messages, 1):
            logging.info(f"Decrypted Message {i}: {decrypted_message}")
    else:
        logging.info("Invalid choice, please restart the program.")


if __name__ == "__main__":
    main()
