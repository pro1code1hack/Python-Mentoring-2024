def nested_loops() -> None:
    """
    Prints a pattern of numbers using nested loops.
    Each line contains the same number repeated, starting from 1 up to 5.
    """
    for i in range(1, 6):  # Outer loop for each number from 1 to 5
        for _ in range(i):  # Inner loop to print the current number 'i' times
            print(i, end="")
        print()  # Move to the next line after printing each number


if __name__ == "__main__":
    nested_loops()
