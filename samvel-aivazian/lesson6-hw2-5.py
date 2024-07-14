import sys


# Assignment 2: The Substring Counter
def count_substrings(main_string, substring):
    try:
        return main_string.count(substring)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


main_string_test = "hellohellohello"
substring_test = "ello"

try:
    substring_count = count_substrings(main_string_test, substring_test)
    print(substring_count, f"The substring '{substring_test}' appears {substring_count} times in '{main_string_test}'.")
except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)


# Assignment 3: The Alignment Formatter
def format_sentence(sentence, frame_width):
    try:
        if frame_width < len(sentence):
            raise ValueError("Frame width is too small for the sentence.")
        return sentence.center(frame_width)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


sentence_test = "hello"
frame_width_test = 10

try:
    formatted_sentence = format_sentence(sentence_test, frame_width_test)
    print(formatted_sentence)
except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)


# Assignment 4: The Case Converter
def convert_case(text, case):
    try:
        if case.lower() == 'upper':
            return text.upper()
        elif case.lower() == 'lower':
            return text.lower()
        else:
            raise ValueError("Case must be 'upper' or 'lower'.")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


text_test = "Python is Fun!"
case_test = "upper"

try:
    converted_text = convert_case(text_test, case_test)
    print(converted_text)
except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)


# Assignment 5: The URL Corrector
def correct_url(url):
    try:
        if not url.startswith('http://') and not url.startswith('https://'):
            return 'https://' + url
        return url
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


url_test = "www.swetrix.com"

try:
    corrected_url = correct_url(url_test)
    print(corrected_url)
except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)


# Writing to file logic
def write_to_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content + "\n")
    except Exception as e:
        print(f"Failed to write to file: {e}", file=sys.stderr)


# Writing the results to a file
results_file_path = 'results.txt'
write_to_file(results_file_path, f"Substring count: {substring_count}")
write_to_file(results_file_path, f"Formatted sentence: '{formatted_sentence.strip()}'")
write_to_file(results_file_path, f"Converted text: '{converted_text}'")
write_to_file(results_file_path, f"Corrected URL: '{corrected_url}'")