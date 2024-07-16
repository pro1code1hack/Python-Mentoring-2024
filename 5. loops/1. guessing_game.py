# Write a program that selects a random number and asks the user to guess it. 
# Use a while loop to allow multiple attempts until they guess correctly or choose to exit.

# Input:
# Guess the number: 8
# Wrong! Try again or type 'exit' to stop: 5
# Wrong! Try again or type 'exit' to stop: exit
# Output:
# The correct number was 7. Better luck next time!

import random

random_number = random.randint(1, 10)

while True:
    guess_number = int(input("Guess number [1-10]: "))

    if guess_number == 0:
        print(f"Exiting... The correct number was {random_number}. Better luck next time!")
        break
    
    elif guess_number != random_number:
        print("Wrong! Try again. Or type 0 to stop")
        continue

    elif guess_number == random_number:
        print(f"You're right! It's {random_number}")
        break


