def is_prime(number: int) -> None:
    """
    Determine if a given number is prime.

    Args:
    number (int): The number to check for primality.

    Returns:
    None: Prints whether the number is prime or not.
    """
    if number <= 1:
        print(f"{number} is not a prime number.")
        return

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            return

    print(f"{number} is a prime number.")


# Example usage
test_number = 11
is_prime(test_number)
