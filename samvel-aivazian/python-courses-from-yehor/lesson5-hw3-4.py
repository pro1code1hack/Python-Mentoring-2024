def get_factors(num: int) -> list[int]:
    """
    Find all factors of a given number.

    Args:
    num (int): The number to find factors for.

    Returns:
    list[int]: A sorted list of factors of the given number.
    """
    if num < 1:
        return []  # Return empty list for numbers less than 1

    factors = [1]  # Start with 1, which is a factor of all natural numbers

    # Loop through possible divisors from 2 to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:  # Check if divisors are not the square root of num to avoid duplicates
                factors.append(num // i)

    factors.append(num)  # Add the number itself, since all numbers are divisible by themselves

    return sorted(factors)  # Return the sorted list of factors


def convert_temperature(temperature: int, convert_to: str = 'F') -> float:
    """
    Convert temperature between Celsius and Fahrenheit.

    Args:
    temperature (int): The temperature to convert.
    convert_to (str): The target temperature unit ('C' for Celsius, 'F' for Fahrenheit).

    Returns:
    float: The converted temperature.
    """
    if convert_to == 'C':  # Fahrenheit to Celsius conversion
        return (temperature - 32) * 5 / 9
    else:  # Celsius to Fahrenheit conversion
        return temperature * 9 / 5 + 32


# Test outputs for Task 3
task_3_output_1 = get_factors(28)
task_3_output_2 = get_factors(13)
task_3_output_3 = get_factors(0)
print("Factors of 28:", task_3_output_1)  # Expected: [1, 2, 4, 7, 14, 28]
print("Factors of 13:", task_3_output_2)  # Expected: [1, 13]
print("Factors of 0:", task_3_output_3)  # Expected: []

# Test outputs for Task 4
task_4_output_1 = convert_temperature(100)  # Expected: 212.0
task_4_output_2 = convert_temperature(212, convert_to='C')  # Expected: 100.0
print("100°C to Fahrenheit:", task_4_output_1)  # Expected: 212.0
print("212°F to Celsius:", task_4_output_2)  # Expected: 100.0
