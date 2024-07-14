from typing import Union


# Task 1: Unit Converter
def convert_inches_to_centimeters(inches: Union[int, float]) -> str:
    """
    Convert inches to centimeters.

    Args:
    inches (Union[int, float]): The length in inches to be converted.

    Returns:
    str: The length in centimeters.
    """
    centimeters = inches * 2.54
    return f"{centimeters} cm"


# Task 2: Temperature Converter
def convert_fahrenheit_to_celsius(fahrenheit: Union[int, float]) -> str:
    """
    Convert Fahrenheit to Celsius.

    Args:
    fahrenheit (Union[int, float]): The temperature in Fahrenheit to be converted.

    Returns:
    str: The temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return f"{celsius:.1f} Celsius"


# Task 3: Simple Interest Calculator
def calculate_simple_interest(principal: Union[int, float], rate: Union[int, float], time: Union[int, float]) -> str:
    """
    Calculate the simple interest.

    Args:
    principal (Union[int, float]): The principal amount.
    Rate (Union[int, float]): The rate of interest per year.
    Time (Union[int, float]): The time the money is invested or borrowed for, in years.

    Returns:
    str: The calculated simple interest.
    """
    simple_interest = (principal * rate * time) / 100
    return f"Simple Interest is {simple_interest}"


# For Task 1
inches_input = 10
print(convert_inches_to_centimeters(inches_input))  # Output: 25.4 cm

# For Task 2
fahrenheit_input = 32
print(convert_fahrenheit_to_celsius(fahrenheit_input))  # Output: 0.0 Celsius

# For Task 3
principal_input = 1000
rate_input = 5
time_input = 3
print(calculate_simple_interest(principal_input, rate_input, time_input))  # Output: Simple Interest is 150.0
