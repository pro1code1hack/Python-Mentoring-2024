"""
Task 1: Exception Safe File Reader

Create a function `safe_file_reader` that reads contents from a given file and handles any possible exceptions.

#### Requirements:

- The function should accept a file path as an argument.
- Use a `try-except` block to handle `FileNotFoundError` and print a friendly message if the file is not found.
- Use the `with` statement to ensure the file is properly closed after reading.
- Print the contents of the file if it is found and successfully opened.
"""

def safe_file_reader(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("Sorry, the file was not found.")


safe_file_reader("homework_lesson1231.py")



