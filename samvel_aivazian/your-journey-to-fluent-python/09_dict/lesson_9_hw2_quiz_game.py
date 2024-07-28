import logging
import random

logging.basicConfig(level=logging.INFO, format='%(message)s')

flashcards = {
    "What is the chemical symbol for water?": "H2O",
    "What is the capital of France?": "Paris",
    "What planet is known as the Red Planet?": "Mars",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the largest ocean on Earth?": "Pacific Ocean"
}


def main():
    logging.info("Welcome to the Flashcard Quiz Game!")
    while True:
        question = random.choice(list(flashcards.keys()))
        logging.info(f"Question: {question}")
        logging.info("Your answer: ")
        user_answer = input().strip()

        if user_answer.lower() == flashcards[question].lower():
            logging.info("Correct!")
        else:
            logging.info(f"Incorrect. The correct answer is: {flashcards[question]}")

        logging.info("Do you want to continue? (yes/no): ")
        if input().strip().lower() != 'yes':
            logging.info("Thank you for playing the Flashcard Quiz Game!")
            break


if __name__ == "__main__":
    main()
