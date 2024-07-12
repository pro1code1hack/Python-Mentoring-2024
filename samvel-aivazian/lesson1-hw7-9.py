# Task 1: Unit Converter
def convert_inches_to_centimeters(inches: int) -> str:
    centimeters = inches * 2.54
    return f"{centimeters} cm"


# Task 2: Temperature Converter
def convert_fahrenheit_to_celsius(fahrenheit: int) -> str:
    celsius = (fahrenheit - 32) * 5 / 9
    return f"{celsius:.1f} Celsius"


# Task 3: Simple Interest Calculator
def calculate_simple_interest(principal: int, rate: int, time: int) -> str:
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
