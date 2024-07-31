"""
Task 1: Methods

1. Create two sets, `A` and `B`, where `A` contains numbers from 1 to 10 and `B` contains numbers from 5 to 15.
2. Perform the following operations and print the results:
3. Find the union of `A` and `B`.
4. Find the intersection of `A` and `B`.
5. Find the difference between `A` and `B`.
6. Find the symmetric difference between `A` and `B`.
7. Add a new element 16 to set `B` and remove element 5.
8. Check if `A` is a subset of `B` and vice versa.
"""

A = set(range(1, 11))
B = set(range(5, 16))

union_set = A.union(B)
intersection_set = A.intersection(B)
difference_set = A.difference(B)
symmetric_difference_set = A.symmetric_difference(B)

B.add(16)
B.remove(5)

is_A_subset_of_B = A.issubset(B)
is_B_subset_of_A = B.issubset(A)

print(f"A: {A}")
print(f"B: {B}")
print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference (A - B): {difference_set}")
print(f"Symmetric Difference: {symmetric_difference_set}")
print(f"A is subset of B: {is_A_subset_of_B}")
print(f"B is subset of A: {is_B_subset_of_A}")


"""
Task 2: More Methods

1. Create three sets, `X`, `Y`, and `K`, with random numbers and some common elements among them.
2. Update set `X` with the intersection of `X`, `Y`, and `K`.
3. Perform a symmetric difference update between set `Y` and set `K`.
4. Check if `X` is now a subset of `Y` or `K` and print the result.
5. Convert set `K` into an immutable set and attempt to add another element to demonstrate the immutable property.
"""

X = {1, 2, 3, 4, 5}
Y = {3, 4, 5, 6, 7}
K = {5, 6, 7, 8, 9}

X.intersection_update(Y, K)
Y.symmetric_difference_update(K)

is_X_subset_of_Y = X.issubset(Y)
is_X_subset_of_K = X.issubset(K)

K = frozenset(K)

print(f"X: {X}")
print(f"Y: {Y}")
print(f"K: {K}")
print(f"X is subset of Y: {is_X_subset_of_Y}")
print(f"X is subset of K: {is_X_subset_of_K}")

try:
    K.add(10)
except AttributeError as e:
    print("Cannot add element to frozenset:", e)


"""
Task 3: Guess a Letter

Create a game where players guess letters of a secret word, using sets to track guessed letters and determine the game's progress.

Example
Input: Secret Word: "banana", Guessed Letters: {'a', 'n'}, Guess: 'b'
Output: Correct

Input: Secret Word: "apple", Guessed Letters: {'a', 'e', 'p'}, Guess: 'c'
Output: Incorrect
"""

secret_word = input("Enter the secret word: ").lower()
guessed_letters = set(input("Enter guessed letters (separated by commas): ").lower().split(','))
guess = input("Guess a letter: ").lower()

if guess in secret_word and guess not in guessed_letters:
    guessed_letters.add(guess)
    print("Correct")
else:
    print("Incorrect")

print(f"Guessed Letters: {guessed_letters}")
print(f"Secret Word: {' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])}")