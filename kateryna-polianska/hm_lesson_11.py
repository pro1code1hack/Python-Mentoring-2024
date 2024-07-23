"""
Task 2: Voting

Implement a function `check_voter_age` that checks if a person is eligible to vote and raises an exception if the age is below the minimum voting age.

Requirements:
- The function should accept one integer argument, `age`.
- If `age` is less than 18, raise a `ValueError` with a message indicating that the person is too young to vote.
- If `age` is 18 or above, print a message confirming that the person is allowed to vote.
- Use a `try` block to test the function with different ages and an `except` block to catch and print the ValueError message.
"""

def check_voter_age(age):
    if age < 18:
        raise ValueError("You are too young to vote.")
    else:
        print("You are allowed to vote.")


age = int(input("Input your age:"))
check_voter_age(age)