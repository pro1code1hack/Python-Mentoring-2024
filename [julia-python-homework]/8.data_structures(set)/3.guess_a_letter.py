""" Create a game where players guess letters of a secret word, using sets to track guessed 
letters and determine the game's progress."""

# Input: Secret Word: "banana",
# Guessed Letters: {'a', 'n'},
# Guess: 'b'
# Output: Correct

# Input: Secret Word: "apple",
# Guessed Letters: {'a', 'e', 'p'},
# Guess: 'c'
# Output: Incorrect

secret_word = input("Enter a secret word: ")
set_secret_word = set(secret_word)
guessed_letters = set()

while True:
    new_letter = input("Guess a letter: ")

    if  new_letter in set_secret_word:
        guessed_letters.add(new_letter)
        print("Correct!")

        if  set_secret_word != guessed_letters:
            print(f"Guessed Letters: {guessed_letters}. Next one?")

        else:
            print(f"You won! The secret word is: {secret_word}")
            break

    else:
        print("Incorrect! Game over")
        break
