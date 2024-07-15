# Task 1: Unit Converter
from typing import Union


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


inches_input = 10
print(convert_inches_to_centimeters(inches_input))  # Output: 25.4 cm
