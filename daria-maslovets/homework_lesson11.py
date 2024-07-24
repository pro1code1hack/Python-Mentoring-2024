"""

### Task 1: The Guessing Game
**Objective:**: Write a program that selects a random number and asks the user to guess it. Use a while loop to allow multiple attempts until they guess correctly or choose to exit.
Input:
Guess the number: 8
Wrong! Try again or type 'exit' to stop: 5
Wrong! Try again or type 'exit' to stop: exit
Output:
The correct number was 7. Better luck next time!
"""



number = 8
guess = int(input("Enter a number "))       # Read the guess

while number != guess:
    want_exit = input("Do you want to exit?")
    if want_exit == 'Yes':
        print(f'The correct number was {number}. Better luck next time!')  #run function with the number
        break

    guess = int(input("Wrong! Try again"))                     # While guess is not the same as your number ....








