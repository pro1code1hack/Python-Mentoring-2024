"""
Task 2: Sum of Digits

Create a function `print_digit_sum` that calculates and prints the sum of all digits in a given integer.

#### Requirements:
- The function should accept a single integer argument, possibly negative.
- Convert the integer to its absolute value to handle negative numbers.
- Iterate over each digit in the number and calculate the total sum.
- Print the result to the console. The function returns `None`.

"""

def print_digit_sum(number):
    total_sum = sum(int(digit) for digit in str(abs(number)))
    print(total_sum)


print_digit_sum(1234)
print_digit_sum(-567)






