"""
Task 2: Quiz Game

Create a flashcard quiz game that helps users learn and test their knowledge on various topics.

#### Requirements:
1. **Data**: Define a dictionary named `flashcards` where keys are questions and values are answers.
2. **Quiz**: Implement a quiz functionality that presents users with a random flashcard question and prompts them to input their answer.
3. **Repeat**: Allow the user to continue the quiz until they decide to quit.

"""

import random

flashcards = {
    "What is the chemical symbol for water?": "H2O",
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the powerhouse of the cell?": "Mitochondria"
}
def quiz():
    while True:
        question, answer = random.choice(list(flashcards.items()))
        user_answer = input(f"{question} ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {answer}")
        continue_quiz = input("Do you want to continue? (yes/no) ")
        if continue_quiz.strip().lower() != 'yes':
            break
quiz()









