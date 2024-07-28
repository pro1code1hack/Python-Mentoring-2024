import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def main():
    logging.info("Enter the secret word: ")
    secret_word = input().strip()
    guessed_letters = set()

    while True:
        logging.info(f"Guessed letters so far: {guessed_letters}")
        logging.info("Guess a letter: ")
        guess = input().strip().lower()

        if guess in guessed_letters:
            logging.info("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            logging.info("Correct!")
        else:
            logging.info("Incorrect.")

        if set(secret_word).issubset(guessed_letters):
            logging.info("Congratulations! You've guessed the word.")
            break


if __name__ == "__main__":
    main()
