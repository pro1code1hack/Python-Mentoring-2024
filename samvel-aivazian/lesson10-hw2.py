import random


def guessing_game():
    number_to_guess = random.randint(1, 10)
    print("Guess the number (between 1 and 10). Type 'exit' to quit.")

    while True:
        user_input = input("Guess the number: ")

        if user_input.lower() == 'exit':
            break

        try:
            guess = int(user_input)
            if guess == number_to_guess:
                print("Congratulations! You guessed it right.")
                break
            else:
                print("Wrong! Try again or type 'exit' to stop.")
        except ValueError:
            print("Invalid input. Please enter a number or 'exit' to quit.")

    print(f"The correct number was {number_to_guess}. Better luck next time!")


if __name__ == "__main__":
    guessing_game()
