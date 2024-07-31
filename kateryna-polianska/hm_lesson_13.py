"""
Task 2: File Content Reverser

Write a function `reverse_file_content` that reads a file, reverses its content, and writes it back to the same file.

Requirements:
- The function should take a file path as an argument.
- Read the original content of the file and reverse the order of lines.
- Write the reversed content back to the same file.
- Ensure all file operations are done within a `with` block to handle the file resource properly.
"""

def reverse_file_content(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    reversed_lines = lines[::-1]

    with open(file_path, 'w') as file:
        file.writelines(reversed_lines)

reverse_file_content('lesson-13-text.txt')
