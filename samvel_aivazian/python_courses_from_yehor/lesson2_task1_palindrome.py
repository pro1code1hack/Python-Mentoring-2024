def find_palindromes(word_list: list[str]) -> list[str]:
    """
    Identify and return a list of palindromes from the given word list.

    Args:
    word_list (list[str]): A list of words to check for palindromes.

    Returns:
    list[str]: A list containing all palindromes found in the input list.
    """
    palindromes = []  # List to hold the palindromes found

    for word in word_list:
        # A word is a palindrome if it is equal to its reverse
        if word == word[::-1]:
            palindromes.append(word)

    return palindromes


# Example usage
word_list = ["radar", "python", "level", "world", "madam"]
palindrome_words = find_palindromes(word_list)
print("Palindrome words:", palindrome_words)  # Output: Palindrome words: ['radar', 'level', 'madam']
