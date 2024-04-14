# Let's implement the Python functions for each assignment based on the provided image instructions.

# Assignment 1: The Name Corrector
# This function takes a name and corrects it to have the first letter capitalized and the rest lowercase.

def name_corrector(name: str) -> str:
    # Capitalize the first letter and make the rest lowercase
    corrected_name = name.capitalize()
    return corrected_name

# Assignment 2: The Substring Counter
def substring_counter(main_string: str, substring: str) -> str:
    count = main_string.count(substring)
    return f"The substring '{substring}' appears {count} times in '{main_string}'."

# Assignment 3: The Alignment Formatter
def alignment_formatter(sentence: str, width: int) -> str:
    # The center method is used to center align the string within the specified width
    centered_sentence = sentence.center(width)
    return centered_sentence

# Assignment 4: The Case Converter
def case_converter(text: str, case_type: str) -> str:
    if case_type.lower() == 'upper':
        return text.upper()
    elif case_type.lower() == 'lower':
        return text.lower()
    else:
        return "Error: Invalid choice. Please choose 'upper' or 'lower'."

# Assignment 5: The URL Corrector
def url_corrector(url: str) -> str:
    if not url.startswith('http://') and not url.startswith('https://'):
        url = f"https://{url}"
    return f"Corrected URL: {url}"

# Demonstration of results without actual user input (as we can't get user input in this environment):

# Assignment 1 example:
name_example = "aLiCe"
corrected_name = name_corrector(name_example)
print(corrected_name)

# Assignment 2 example:
main_string_example = "hellohellohello"
substring_example = "ello"
substring_count_result = substring_counter(main_string_example, substring_example)
print(substring_count_result)

# Assignment 3 example:
sentence_example = "hello"
frame_width_example = 10
formatted_sentence = alignment_formatter(sentence_example, frame_width_example)
print(formatted_sentence)

# Assignment 4 example:
text_example = "Python is Fun!"
case_choice_example = "upper"
case_converted_text = case_converter(text_example, case_choice_example)
print(case_converted_text)

# Assignment 5 example:
url_example = "www.swetrix.com"
corrected_url = url_corrector(url_example)
print(corrected_url)
