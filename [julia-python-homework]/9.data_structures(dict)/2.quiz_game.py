"""Create a flashcard quiz game that helps users learn and test their knowledge on various 
topics."""

from random import choice

# Requirements:
# 1. Data: Define a dictionary named flashcards where keys are questions and values are answers.
# 2. Quiz: Implement a quiz functionality that presents users with a random flashcard question and
# prompts them to input their answer.
# 3. Repeat: Allow the user to continue the quiz until they decide to quit.

flashcards = {
    "What is the chemical symbol for water? ": "H2O",
    "What is the capital city of France? ": "PARIS",
    "What is the largest planet in our solar system? ": "JUPITER",
    "What is the hardest natural substance on Earth? ": "DIAMOND",
    "In what year did the Titanic sink? ": "1912",
    "What is the square root of 64? ": "8",
    "What is the tallest mountain in the world? ": "EVEREST",
    "What is the largest mammal? ": "BLUE WHALE"
}

COUNT = 1
while True:
    MAX_COUNT = 9

    if COUNT != MAX_COUNT:
        question = choice(list(flashcards))
        answer = flashcards.pop(question)

        reply = input(f"{COUNT}. {question}(or enter 'exit'): ").upper()

        if reply == answer:
            COUNT += 1
            print("Correct!")

        elif reply == "EXIT":
            print("Quiz stopped!")
            break

        else:
            print("Sorry but you lost :(")
            break

    else:
        print("Hurray! You won the quiz!")
        break
