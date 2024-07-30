"""
### Task 1: The Guessing Game

**Objective:**: Write a program that selects a random number and asks the user to guess it. Use a while loop to allow multiple attempts until they guess correctly or choose to exit.


```
Input:
Guess the number: 8
Wrong! Try again or type 'exit' to stop: 5
Wrong! Try again or type 'exit' to stop: exit

Output:
The correct number was 7. Better luck next time!
```

"""

import random

def guessing_game():
    number_to_guess = random.randint(1, 10)
    while True:
        guess = input("Guess the number or type 'exit' to stop: ")
        if guess.lower() == 'exit':
            print(f"The correct number was {number_to_guess}. Better luck next time!")
            break
        elif int(guess) == number_to_guess:
            print("Congratulations! You guessed correctly.")
            break
        else:
            print("Wrong! Try again or type 'exit' to stop.")

"""
Task 2: Nested loops
Objective:: Write a program using nested loops to match the following output.

Output:
1
22
333
4444
55555
"""

def nested_loop_pattern():
    num_lines = int(input("Enter nuber of lines: ")) 
    for i in range(1, num_lines + 1):
        for j in range(i):
            print(i, end="")
        print()  


"""
The Factorial Calculator
Objective:: Create a program that computes the factorial of a given number using a for loop.

Input:
Enter a number to calculate the factorial: 5

Output:
The factorial of 5 is 120.
"""
def factorial_calculator():
    num = int(input("Enter a number to calculate the factorial: "))
    
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    
    print(f"The factorial of {num} is {factorial}")

factorial_calculator()
