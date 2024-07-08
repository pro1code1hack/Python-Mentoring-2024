"""
Task 1: Methods
Objective:

Create two sets, A and B, where A contains numbers from 1 to 10 and B contains numbers from 5 to 15.
Perform the following operations and print the results:
Find the union of A and B.
Find the intersection of A and B.
Find the difference between A and B.
Find the symmetric difference between A and B.
Add a new element 16 to set B and remove element 5.
Check if A is a subset of B and vice versa.
"""

def set_operations():
    A = set(range(1, 11))  
    B = set(range(5, 16)) 
    
    union_AB = A | B
    print(f"Union of A and B: {union_AB}")
    
    intersection_AB = A & B
    print(f"Intersection of A and B: {intersection_AB}")
    
    difference_A_B = A - B
    print(f"Difference of A - B: {difference_A_B}")
    
    symmetric_difference_AB = A ^ B
    print(f"Symmetric Difference of A and B: {symmetric_difference_AB}")
    
    B.add(16)
    B.discard(5)
    print(f"Set B after adding 16 and removing 5: {B}")
    
    if A.issubset(B):
        print("A is a subset of B.")
    else:
        print("A is not a subset of B.")
    
    if B.issubset(A):
        print("B is a subset of A.")
    else:
        print("B is not a subset of A.")


"""
More Methods
Objective:

Create three sets, X, Y, and K, with random numbers and some common elements among them.
Update set X with the intersection of X, Y, and K.
Perform a symmetric difference update between set Y and set K.
Check if X is now a subset of Y or K and print the result.
Convert set K into an immutable set and attempt to add another element to demonstrate the immutable property.
"""
def more_set_operations():
    X = {1, 2, 3, 4, 5}
    Y = {4, 5, 6, 7, 8}
    K = {5, 6, 7, 8, 9}
    
    X.intersection_update(Y, K)
    print(f"Updated set X with intersection of X, Y, and K: {X}")
    
    Y.symmetric_difference_update(K)
    print(f"Symmetric difference update between Y and K: {Y}")
    
    if X.issubset(Y):
        print("X is a subset of Y.")
    else:
        print("X is not a subset of Y.")
    
    if X.issubset(K):
        print("X is a subset of K.")
    else:
        print("X is not a subset of K.")
    
    immutable_K = frozenset(K)
    try:
        immutable_K.add(10) 
    except AttributeError:
        print("Cannot add element to an immutable set.")
    print(f"Immutable set K: {immutable_K}")



"""
Task 3: Guess a Letter
Objective: Create a game where players guess letters of a secret word, using sets to track guessed letters and determine the game's progress.

## Example
Input: Secret Word: "banana", Guessed Letters: {'a', 'n'}, Guess: 'b'
Output: Correct

Input: Secret Word: "apple", Guessed Letters: {'a', 'e', 'p'}, Guess: 'c'
Output: Incorrect
"""

def guess_letter_game(secret_word, guessed_letters, guess):
    secret_set = set(secret_word)
    guessed_set = set(guessed_letters)
    
    if guess in secret_set:
        guessed_set.add(guess)
        print("Correct")
    else:
        guessed_set.add(guess)
        print("Incorrect")
    
    game_progress = all(letter in guessed_set for letter in secret_set)
    if game_progress:
        print("You've guessed all letters! You win!")
    else:
        print("Keep guessing!")

# secret_word = "python"
# guessed_letters = {'o', 't'}
# guess = 'b'
# guess_letter_game(secret_word, guessed_letters, guess)
