"""
Task 1: Unit Converter
Objective: Develop a program to convert inches to centimeters.

Input: The user inputs a length in inches.
Output: The program outputs the equivalent length in centimeters.
Conversion: 1 inch = 2.54 cm.
Input: 10
Output: 25.4 cm
"""

def unit_convereter():
    inches = int(input("Input length of inches ---> "))
    print("Converting inches to centimeters....")
    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters} centimeters")


"""
Task 2: Temperature Converter
Objective: Write a program that converts a temperature from Fahrenheit to Celsius.

Input: The user enters a temperature in Fahrenheit.
Output: The program prints the temperature in Celsius.
Formula: Celsius = (Fahrenheit - 32) * 5/9.
Input: 32
Output: 0.0 Celsius
"""

def temperature_converter():
    fahrenheit = int(input("Input tempereture in Fahrenheit ---> "))
    celsuis = (fahrenheit-32) * 5/9
    print(f"{fahrenheit} fahrenheit in celsuis ---> {celsuis}")

"""
Task 3: Simple Interest Calculator
Objective: Create a script to calculate simple interest.

Input: The user enters the principal amount, the rate of interest (as a percentage), and the time period in years.

Output: The script outputs the calculated simple interest.

Formula: Simple Interest = (Principal * Rate * Time) / 100.

Example
Input: Principal = 1000, Rate = 5, Time = 3
Output: Simple Interest is 150.0
"""

def simple_interest_calculator():
    principal = int(input("Enter principal amount ---> "))
    interest = int(input("Enter rate of interest (as a percentage) ---> "))
    time = int(input("Enter time period in years ---> "))
    result = (principal * interest * time) / 100
    print(f"Your Simple Interest in {time} years is {result}")

simple_interest_calculator()