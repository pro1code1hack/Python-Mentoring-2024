def fibonacci_sequence(n: int) -> list[int]:
    """
    Generate a Fibonacci sequence of length n.

    Args:
    n (int): The length of the Fibonacci sequence to generate.

    Returns:
    list[int]: A list containing the Fibonacci sequence of length n.
    """
    if n <= 0:
        return []

    sequence = [0, 1]

    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)

    return sequence[:n]


def multiplication_table(number: int) -> None:
    """
    Print the multiplication table for a given number from 1 to 10.

    Args:
    number (int): The number for which to print the multiplication table.
    """
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


# Example usage of Fibonacci Sequence Generator
fib_sequence = fibonacci_sequence(5)
print(f"Fibonacci sequence with 5 numbers: {fib_sequence}")

# Example usage of Multiplication Table Printer
print("\nMultiplication table for 3:")
multiplication_table(3)
