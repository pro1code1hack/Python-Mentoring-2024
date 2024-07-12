def find_palindromes(word_list: list[str]) -> list[str]:
    palindromes = []  # List to hold the palindromes found
    for word in word_list:
        # A word is a palindrome if it is equal to its reverse
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes


# Example usage
word_list = ["radar", "python", "level", "world", "madam"]
palindrome_words = find_palindromes(word_list)
print("Palindrome words:", palindrome_words)
