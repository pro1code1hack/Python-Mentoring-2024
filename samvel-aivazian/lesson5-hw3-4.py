# Task 3: Find All Factors
def get_factors(num: int) -> list[int]:
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


# Task 4: Temperature Converter with Optional Parameters
def convert_temperature(temperature: int, convert_to: str = 'F') -> float:
    if convert_to == 'C':  # Fahrenheit to Celsius conversion
        return (temperature - 32) * 5 / 9
    else:  # Celsius to Fahrenheit conversion
        return temperature * 9 / 5 + 32


# Test outputs for Task 3
task_3_output_1 = get_factors(28)
task_3_output_2 = get_factors(13)
task_3_output_3 = get_factors(0)
print(task_3_output_1)
print(task_3_output_2)
print(task_3_output_3)

# Test outputs for Task 4
task_4_output_1 = convert_temperature(100)
task_4_output_2 = convert_temperature(212, convert_to='C')
print(task_4_output_1)
print(task_4_output_2)
