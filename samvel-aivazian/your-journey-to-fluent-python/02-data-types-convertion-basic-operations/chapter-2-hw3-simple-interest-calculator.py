# Task 3: Simple Interest Calculator
from typing import Union


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


principal_input = 1000
rate_input = 5
time_input = 3
print(calculate_simple_interest(principal_input, rate_input, time_input))  # Output: Simple Interest is 150.0
