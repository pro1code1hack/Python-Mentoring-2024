import random


def task1() -> None:
    """
    Perform basic set operations and methods on sets A and B.
    """
    A = set(range(1, 11))  # Set A containing numbers from 1 to 10
    B = set(range(5, 16))  # Set B containing numbers from 5 to 15

    # Perform various set operations
    union_AB = A.union(B)
    intersection_AB = A.intersection(B)
    difference_AB = A.difference(B)
    symmetric_difference_AB = A.symmetric_difference(B)

    # Modify sets
    B.add(16)
    B.discard(5)

    # Check subset relationships
    A_subset_B = A.issubset(B)
    B_subset_A = B.issubset(A)

    task_1_results = {
        'A': A,
        'B': B,
        'union': union_AB,
        'intersection': intersection_AB,
        'difference': difference_AB,
        'symmetric_difference': symmetric_difference_AB,
        'A_subset_B': A_subset_B,
        'B_subset_A': B_subset_A
    }
    print(task_1_results)


def task2() -> None:
    """
    Perform more complex set methods and operations on sets X, Y, and Z.
    """
    # Create sets with random samples
    X = set(random.sample(range(1, 20), 5))
    Y = set(random.sample(range(1, 20), 5))
    Z = set(random.sample(range(1, 20), 5))

    # Perform intersection update
    X.intersection_update(Y, Z)

    # Perform symmetric difference update
    Y.symmetric_difference_update(Z)

    # Check subset relationships
    X_subset_Y = X.issubset(Y)
    X_subset_Z = X.issubset(Z)

    # Convert Z to an immutable set (frozenset)
    Z = frozenset(Z)

    # Check immutability of Z
    try:
        Z.add(21)
        z_immutable = False
    except AttributeError:
        z_immutable = True

    task_2_results = {
        'X': X,
        'Y': Y,
        'Z': list(Z),  # Converting the immutable set to a list for display purposes
        'X_subset_Y': X_subset_Y,
        'X_subset_Z': X_subset_Z,
        'Z_immutable': z_immutable
    }
    print(task_2_results)


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def guess_letter(secret_word: str, guessed_letters: set[str], guess: str) -> tuple[str, set[str]]:
    """
    Simulate a letter guessing game.

    Args:
    secret_word (str): The word to guess.
    guessed_letters (set[str]): The set of letters that have been guessed.
    guess (str): The letter being guessed.

    Returns:
    tuple[str, set[str]]: A tuple containing a message ('Correct' or 'Incorrect') and the updated set of guessed letters.
    """
    guessed_letters.add(guess)
    if guess in secret_word:
        return 'Correct', guessed_letters
    else:
        return 'Incorrect', guessed_letters


if __name__ == "__main__":
    # Execute Task 1
    print("Task 1: Basic Set Operations and Methods")
    task1()

    # Execute Task 2
    print("\nTask 2: More Complex Set Methods and Operations")
    task2()

    # Execute Task 3
    print("\nTask 3: Primes")
    primes = {n for n in range(1, 101) if is_prime(n)}
    print(primes)

    # Execute Task 4
    print("\nTask 4: Guessing Game")
    secret_word = "banana"
    guessed_letters = {'a', 'n'}
    guess = 'b'
    result = guess_letter(secret_word, guessed_letters, guess)
    print(result)

    secret_word = "apple"
    guessed_letters = {'a', 'e', 'p'}
    guess = 'c'
    result = guess_letter(secret_word, guessed_letters, guess)
    print(result)
