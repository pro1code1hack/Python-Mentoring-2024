def factorial_calculator(number: int) -> int:
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    return factorial


user_input_number = 500
fact_result = factorial_calculator(user_input_number)
print(f"The factorial of {user_input_number} is {fact_result}.")
