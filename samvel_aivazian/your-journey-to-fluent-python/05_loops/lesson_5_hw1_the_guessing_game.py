import logging
import random

logging.basicConfig(level=logging.INFO, format='%(message)s')


def guessing_game():
    number_to_guess = random.randint(1, 10)
    logging.info("Guess the number between 1 and 10.")

    while True:
        logging.info("Enter your guess: ")
        guess = input().strip()
        if guess.lower() == 'exit':
            logging.info(f"The correct number was {number_to_guess}. Better luck next time!")
            break
        if guess.isdigit():
            guess = int(guess)
            if guess == number_to_guess:
                logging.info("Congratulations! You guessed the correct number.")
                break
            else:
                logging.info("Wrong! Try again or type 'exit' to stop.")
        else:
            logging.info("Invalid input. Please enter a number or 'exit'.")


if __name__ == "__main__":
    guessing_game()
