"""

Task 1: Safe Division
Create a function `safe_divide` that safely performs division and handles any division errors gracefully.

#### Requirements:
- The function should accept two parameters, `numerator` and `denominator`.
- Use `try` and `except` blocks to handle division errors such as `ZeroDivisionError`.
- If a division by zero occurs, print an error message and return `None`.
- If the division is successful, return the result.
- Use the `finally` block to print a message that the division attempt has been completed.
"""

def safe_divide(num, delim):
    try:
        result = num / delim
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    finally:
        print("Division attempt completed.")

safe_divide(11, 0)
