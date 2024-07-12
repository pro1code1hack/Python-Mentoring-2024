# Task 1: The Guessing Game.

import random


def guessing_game() -> None:
    correct_number = random.randint(1, 10)

    while True:
        user_input = input("Guess the number or type 'exit' to stop: ")

        if user_input.lower() == 'exit':
            print("You've exited the game.")
            print(f"The correct number was {correct_number}. Better luck next time!")
            break

        try:
            user_guess = int(user_input)
        except ValueError:
            print("That's not a valid number. Try again.")
            continue

        if user_guess == correct_number:
            print(f"Congratulations! You guessed the correct number: {correct_number}.")
            break
        else:
            print("Wrong! Try again.")


guessing_game()
