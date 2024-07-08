"""
Task 1: Star Rectangle
Objective: Implement a function named draw_rectangle that outputs a rectangle made of asterisks (*). The rectangle should have a width of 7 characters and a height of 6 lines.

Requirements:
Use nested for loops to generate the rectangle.
The outer loop should iterate through the lines (height), and the inner loop should iterate through the characters (width) on each line.
Only the border of the rectangle should be drawn with asterisks, while spaces ( ) should fill the interior.
The function does not need to return anything; it should directly print the rectangle to the console.
*******
*     *
*     *
*     *
*     *
*******
"""
def draw_rectangle():
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * width)
        else:
            print('*' + ' ' * (width - 2) + '*')

"""
Task 2: Sum of Digits
Objective: Create a function print_digit_sum that calculates and prints the sum of all digits in a given integer.

Requirements:
The function should accept a single integer argument, possibly negative.
Convert the integer to its absolute value to handle negative numbers.
Iterate over each digit in the number and calculate the total sum.
Print the result to the console. The function returns None.
print_digit_sum(1234)  # Output: 10
print_digit_sum(-567)  # Output: 18
"""
def print_digit_sum(number):
    number = abs(number)
    
    digit_sum = 0
    
    while number > 0:
        digit = number % 10
        digit_sum += digit
        number //= 10
    
    print(f"The sum of digits in the number is: {digit_sum}")

# print_digit_sum(5834) 

"""
Task 3: Find All Factors
Objective: Develop a function get_factors that returns a list of all the divisors of a given natural number.

Requirements:
The function should accept a single integer argument, num.
If num is less than 1, return an empty list to reflect the definition of natural numbers.
Efficiently find and return a list of all divisors of num.
Ensure correct functionality for both small and large values of num.
print(get_factors(28))  # Output: [1, 2, 4, 7, 14, 28]
print(get_factors(13))  # Output: [1, 13]
print(get_factors(0))   # Output: []
"""

def get_factors(num):
    if num < 1:
        return []
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

"""
Task 4: Temperature Converter
Objective: Enhance the convert_temperature function to support optional parameters for conversion direction.

Requirements:
The function should accept one mandatory parameter for the temperature value and one optional parameter for the direction of conversion ('C' for Celsius to Fahrenheit, 'F' for Fahrenheit to Celsius).
Use default arguments to assume conversion from Celsius to Fahrenheit if the direction is not specified.
Calculate and return the converted temperature value.
"""
def convert_temperature(temp, direction='C'):
    if direction == 'C':
        converted_temp = (temp * 9/5) + 32
    elif direction == 'F':
        converted_temp = (temp - 32) * 5/9
    else:
        raise ValueError("Invalid direction. Use 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius.")
    
    return converted_temp

"""
Task 5: Statistics Calculator
Objective: Implement a function calculate_statistics that computes various statistical measures (mean, median, mode, range) for a dataset, based on specified options.

Requirements:
The function should accept an arbitrary number of positional arguments (*data) representing the dataset.
Accept keyword arguments (**options) to specify which statistics to calculate: mean, median, mode, range. If an option is True, calculate that statistic.
Return a dictionary with keys as the names of the statistics calculated and their corresponding results as values.
If no options are specified, calculate and return all statistics.
Handle edge cases such as empty datasets or datasets without a mode.
"""

from collections import Counter

def calculate_statistics(*data, **options):
    statistics = {}
    
    if not data:
        raise ValueError("No data provided.")

    if options.get('mean', True):
        mean = sum(data) / len(data)
        statistics['mean'] = mean

    if options.get('median', True):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            median = sorted_data[n // 2]
        statistics['median'] = median
    
    if options.get('mode', True):
        counter = Counter(data)
        mode = counter.most_common(1)
        if mode:
            statistics['mode'] = mode[0][0]
        else:
            statistics['mode'] = None

    if options.get('range', True):
        range_value = max(data) - min(data)
        statistics['range'] = range_value
    
    return statistics

# print(calculate_statistics(1, 2, 3, 4, 5))                   
# print(calculate_statistics(1, 2, 3, 4, 5, mean=False))        
# print(calculate_statistics(1, 2, 3, 4, 5, mode=False))        
# print(calculate_statistics(1, 2, 3, 4, 5, mode=True, range=False))  
# print(calculate_statistics())                                 

