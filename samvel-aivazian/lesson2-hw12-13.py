# For Assignment 2, let's implement the Fibonacci Sequence Generator.
def fibonacci_sequence(n: int) -> list[int]:
    sequence = [0, 1]

    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
        
    return sequence[:n]

# For Assignment 3, let's implement The Multiplication Table Printer.
def multiplication_table(number: int) -> None:
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Fibonacci Sequence Generator example with n=5
fib_sequence = fibonacci_sequence(5)
print(f"Fibonacci sequence with 5 numbers: {fib_sequence}")

# Multiplication Table Printer example with number=3
print("\nMultiplication table for 3:")
multiplication_table(3)
