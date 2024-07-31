"""
Task 1: The Guessing Game

Write a program that selects a random number and asks the user to guess it. Use a while loop to allow multiple attempts until they guess correctly or choose to exit.

Input:
Guess the number: 8
Wrong! Try again or type 'exit' to stop: 5
Wrong! Try again or type 'exit' to stop: exit

Output:
The correct number was 7. Better luck next time!

"""

import random


random_number = random.randint(1, 10)
max_attempts=3
attempt=0
while attempt<max_attempts:
    attempt += 1
    x=int(input('Type a number from 1 to 10'))
    if x==random_number:
        print('Well done!')
        break
    else:
        print(f'Incorrect! {max_attempts - attempt} attempts left')1
    print(f'The correct number was {random_number}. Better luck next time!')


