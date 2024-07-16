# Task 2: Temperature Converter
from typing import Union


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


fahrenheit_input = 32
print(convert_fahrenheit_to_celsius(fahrenheit_input))  # Output: 0.0 Celsius
