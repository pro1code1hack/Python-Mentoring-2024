# Assignment 1: The Name Corrector
def name_corrector(name: str) -> str:
    """
    Corrects the given name to have the first letter capitalized and the rest lowercase.

    Args:
    name (str): The name to be corrected.

    Returns:
    str: The corrected name.
    """
    # Capitalize the first letter and make the rest lowercase
    corrected_name = name.capitalize()
    return corrected_name


# Assignment 2: The Substring Counter
def substring_counter(main_string: str, substring: str) -> str:
    """
    Counts the occurrences of a substring within a main string.

    Args:
    main_string (str): The string to search within.
    substring (str): The substring to count.

    Returns:
    str: A formatted string stating the count of the substring within the main string.
    """
    count = main_string.count(substring)
    return f"The substring '{substring}' appears {count} times in '{main_string}'."


# Assignment 3: The Alignment Formatter
def alignment_formatter(sentence: str, width: int) -> str:
    """
    Centers a given sentence within a specified width.

    Args:
    sentence (str): The sentence to center align.
    width (int): The width to center the sentence within.

    Returns:
    str: The centered sentence.
    """
    # The center method is used to center align the string within the specified width
    centered_sentence = sentence.center(width)
    return centered_sentence


# Assignment 4: The Case Converter
def case_converter(text: str, case_type: str) -> str:
    """
    Converts the case of the given text based on the specified case type.

    Args:
    text (str): The text to convert.
    case_type (str): The case type to convert to ('upper' or 'lower').

    Returns:
    str: The text converted to the specified case, or an error message for invalid choice.
    """
    if case_type.lower() == 'upper':
        return text.upper()
    elif case_type.lower() == 'lower':
        return text.lower()
    else:
        return "Error: Invalid choice. Please choose 'upper' or 'lower'."


# Assignment 5: The URL Corrector
def url_corrector(url: str) -> str:
    """
    Corrects the given URL to ensure it starts with 'https://'.

    Args:
    url (str): The URL to correct.

    Returns:
    str: The corrected URL.
    """
    if not url.startswith('http://') and not url.startswith('https://'):
        url = f"https://{url}"
    return f"Corrected URL: {url}"


# Demonstration of results without actual user input (as we can't get user input in this environment):

# Assignment 1 example:
name_example = "aLiCe"
corrected_name = name_corrector(name_example)
print(corrected_name)  # Output: Alice

# Assignment 2 example:
main_string_example = "hellohellohello"
substring_example = "ello"
substring_count_result = substring_counter(main_string_example, substring_example)
print(substring_count_result)  # Output: The substring 'ello' appears 3 times in 'hellohellohello'.

# Assignment 3 example:
sentence_example = "hello"
frame_width_example = 10
formatted_sentence = alignment_formatter(sentence_example, frame_width_example)
print(formatted_sentence)  # Output: "  hello   "

# Assignment 4 example:
text_example = "Python is Fun!"
case_choice_example = "upper"
case_converted_text = case_converter(text_example, case_choice_example)
print(case_converted_text)  # Output: PYTHON IS FUN!

# Assignment 5 example:
url_example = "www.swetrix.com"
corrected_url = url_corrector(url_example)
print(corrected_url)  # Output: Corrected URL: https://www.swetrix.com
