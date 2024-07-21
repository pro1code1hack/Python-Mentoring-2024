"""Create a program that computes the factorial
of a given number using a for loop."""

# Input:
# Enter a number to calculate the factorial: 5
# Output:
# The factorial of 5 is 120.

number = int(input("Enter a number to calculate the factorial: "))

FACTORIAL = 1
for i in range(1, number + 1):
    FACTORIAL *= i

print(f"The factorial of {number} is {FACTORIAL}")
