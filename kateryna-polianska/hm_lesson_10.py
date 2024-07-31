"""
Task 1: Star Rectangle

Implement a function named `draw_rectangle` that outputs a rectangle made of asterisks (`*`). The rectangle should have a width of 7 characters and a height of 6 lines.

Requirements:
- Use nested `for` loops to generate the rectangle.
- The outer loop should iterate through the lines (height), and the inner loop should iterate through the characters (width) on each line.
- Only the border of the rectangle should be drawn with asterisks, while spaces (` `) should fill the interior.
- The function does not need to return anything; it should directly print the rectangle to the console.
"""

def draw_rectangle():
    width = 7
    height = 6
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

draw_rectangle()


"""
Task 2: Sum of Digits

Create a function `print_digit_sum` that calculates and prints the sum of all digits in a given integer.

Requirements:
- The function should accept a single integer argument, possibly negative.
- Convert the integer to its absolute value to handle negative numbers.
- Iterate over each digit in the number and calculate the total sum.
- Print the result to the console. The function returns `None`.
"""

def print_digit_sum(number):
    number = abs(number)
    digit_sum = sum(int(digit) for digit in str(number))
    print(digit_sum)

print_digit_sum(1234)
print_digit_sum(-567)

"""
Task 3: Find All Factors

Develop a function `get_factors` that returns a list of all the divisors of a given natural number.

Requirements:
- The function should accept a single integer argument, `num`.
- If `num` is less than 1, return an empty list to reflect the definition of natural numbers.
- Efficiently find and return a list of all divisors of `num`.
- Ensure correct functionality for both small and large values of `num`.
"""

def get_factors(num):
    if num < 1:
        return []
    factors = [i for i in range(1, num + 1) if num % i == 0]
    return factors

print(get_factors(28))
print(get_factors(13))
print(get_factors(0))

"""
Task 4: Temperature Converter
"""

def convert_temperature(value, convert_to='F'):
    if convert_to == 'F':
        return value * 9/5 + 32
    elif convert_to == 'C':
        return (value - 32) * 5/9
    else:
        raise ValueError("Invalid conversion direction. Use 'C' or 'F'.")

print(convert_temperature(100))
print(convert_temperature(212, convert_to='C'))


"""
Task 5: Statistics Calculator

Implement a function `calculate_statistics` that computes various statistical measures (mean, median, mode, range) for a dataset, based on specified options.

Requirements:
- The function should accept an arbitrary number of positional arguments (`*data`) representing the dataset.
- Accept keyword arguments (`**options`) to specify which statistics to calculate: `mean`, `median`, `mode`, `range`. If an option is `True`, calculate that statistic.
- Return a dictionary with keys as the names of the statistics calculated and their corresponding results as values.
- If no options are specified, calculate and return all statistics.
- Handle edge cases such as empty datasets or datasets without a mode.
"""


# I decided to use `statistics` module in this case not to calculate it manually
from statistics import mean, median, mode, StatisticsError

def calculate_statistics(*data, **options):
    if not data:
        return {}
    
    results = {}
    if not options or options.get('mean', False):
        results['mean'] = mean(data)
    if not options or options.get('median', False):
        results['median'] = median(data)
    if not options or options.get('mode', False):
        try:
            results['mode'] = mode(data)
        except StatisticsError:
            results['mode'] = None
    if not options or options.get('range', False):
        results['range'] = max(data) - min(data)
    
    return results

data_points = [4, 1, 2, 2, 3, 5]
print(calculate_statistics(*data_points, mean=True, range=True))  
print(calculate_statistics(*data_points))
