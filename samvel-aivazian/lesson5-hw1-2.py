def draw_rectangle() -> None:
    """
    Draws a rectangle of stars with a fixed width and height.
    """
    width = 7
    height = 6
    for i in range(height):
        if i == 0 or i == height - 1:
            # Print the top or bottom border of the rectangle
            print('*' * width)
        else:
            # Print the sides of the rectangle with spaces in between
            print('*' + ' ' * (width - 2) + '*')


def print_digit_sum(number: int) -> None:
    """
    Prints the sum of the digits of the given number.

    Args:
    number (int): The number to calculate the sum of its digits.
    """
    # Convert the number to absolute value
    abs_number = abs(number)
    # Calculate the sum of the digits
    total_sum = sum(int(digit) for digit in str(abs_number))
    # Print the result
    print(total_sum)


# Call the function to draw the rectangle
draw_rectangle()

# Call the function with example numbers
print_digit_sum(1234)  # Expected Output: 10
print_digit_sum(-567)  # Expected Output: 18
