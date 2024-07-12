import random


# Task 1: Basic set Operations and Methods
def task1() -> None:
    A = set(range(1, 11))  # Set A containing numbers from 1 to 10
    B = set(range(5, 16))  # Set B containing numbers from 5 to 15
    union_AB = A.union(B)
    intersection_AB = A.intersection(B)
    difference_AB = A.difference(B)
    symmetric_difference_AB = A.symmetric_difference(B)
    B.add(16)
    B.discard(5)
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


# Task 2: More Complex set Methods and Operations
def task2() -> None:
    X = set(random.sample(range(1, 20), 5))
    Y = set(random.sample(range(1, 20), 5))
    Z = set(random.sample(range(1, 20), 5))
    X.intersection_update(Y, Z)
    Y.symmetric_difference_update(Z)
    X_subset_Y = X.issubset(Y)
    X_subset_Z = X.issubset(Z)
    Z = frozenset(Z)  # Converting set Z to an immutable set
    try:
        Z.add(21)  # Attempting to add another element to the immutable set Z
    except AttributeError as e:
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


# Task 3: Primes
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Task 4: Create a game where players guess letters of a secret word, using sets to track guessed letters
def guess_letter(secret_word: str, guessed_letters: set[str], guess: str) -> tuple[str, set[str]]:
    guessed_letters = set(guessed_letters)
    guessed_letters.add(guess)
    if guess in secret_word:
        return 'Correct', guessed_letters
    else:
        return 'Incorrect', guessed_letters


primes = {n for n in range(1, 101) if is_prime(n)}
task_3_primes = primes
print(task_3_primes)

# Example inputs for Task 4, as we cannot take real user input in this environment.
secret_word = "banana"
guessed_letters = {'a', 'n'}
guess = 'b'
task_4_example_1 = guess_letter(secret_word, guessed_letters, guess)
print(task_4_example_1)

secret_word = "apple"
guessed_letters = {'a', 'e', 'p'}
guess = 'c'
task_4_example_2 = guess_letter(secret_word, guessed_letters, guess)
print(task_4_example_2)
