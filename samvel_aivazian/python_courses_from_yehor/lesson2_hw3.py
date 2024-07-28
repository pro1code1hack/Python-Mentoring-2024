def factorial_calculator(number: int) -> int:
    """
    Calculate the factorial of a given number.

    Args:
    number (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the given number.
    """
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    return factorial


# Example usage:
user_input_number = 500
fact_result = factorial_calculator(user_input_number)
print(f"The factorial of {user_input_number} is {fact_result}.")
