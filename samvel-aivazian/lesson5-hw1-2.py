# Task 1: Star Rectangle
def draw_rectangle() -> None:
    width = 7
    height = 6
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * width)
        else:
            print('*' + ' ' * (width - 2) + '*')

# Task 2: Sum of Digits
def print_digit_sum(number: int) -> None:
    # Convert the number to absolute value
    abs_number = abs(number)
    # Calculate the sum of the digits
    total_sum = sum(int(digit) for digit in str(abs_number))
    # Print the result
    print(total_sum)
    # The function implicitly returns None

# Call the functions for demonstration
draw_rectangle()  # This will print the rectangle

# Call the print_digit_sum function with example numbers
print_digit_sum(1234)  # Expected Output: 10
print_digit_sum(-567)  # Expected Output: 18

