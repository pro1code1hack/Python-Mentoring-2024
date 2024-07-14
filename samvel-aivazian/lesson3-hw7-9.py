import re

from typing import Dict, List


def mini_database() -> Dict[str, List[str] | str]:
    """
    Collects personal information from the user and stores it in a dictionary.

    Returns:
    dict: A dictionary containing the user's name, age, hobbies, and favorite foods.
    """
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    hobbies = input("Enter your hobbies (separated by commas): ").split(', ')
    favorite_foods = input("Enter your favorite foods (separated by commas): ").split(', ')

    person_info = {
        'Name': name,
        'Age': age,
        'Hobbies': hobbies,
        'Favorite Foods': favorite_foods
    }

    return person_info


def validate_ip(ip_str: str) -> bool:
    """
    Validates an IPv4 address.

    Args:
    ip_str (str): The IP address string to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    # Regular expression to match valid IP addresses
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')

    # Validate the IP address
    if ip_pattern.match(ip_str):
        parts = map(int, ip_str.split('.'))
        return all(0 <= part <= 254 for part in parts)
    return False


def extract_emails(text: str) -> str:
    """
    Extracts email addresses from the given text.

    Args:
    text (str): The text containing email addresses.

    Returns:
    str: A semicolon-separated string of email addresses.
    """
    # Regular expression to find emails in the text
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    # Find all matching emails
    emails = email_pattern.findall(text)
    # Join the emails with semicolons
    return '; '.join(emails)


if __name__ == "__main__":
    # Execute Task 7
    print("Task 7: Mini Database")
    person = mini_database()
    for key, value in person.items():
        print(f"{key}: {value}")
    print()

    # Execute Task 8
    print("Task 8: Validating IP Addresses")
    ip_example_valid = '192.168.1.1'
    ip_example_invalid = '256.300.2.-10'

    valid_check = validate_ip(ip_example_valid)
    print(f"Is '{ip_example_valid}' a valid IP? {valid_check}")

    invalid_check = validate_ip(ip_example_invalid)
    print(f"Is '{ip_example_invalid}' a valid IP? {invalid_check}")
    print()

    # Execute Task 9
    print("Task 9: Email Extractor")
    text_example = "Please contact us at support@example.com or sales@example.com for assistance."
    extracted_emails = extract_emails(text_example)
    print(f"Extracted emails: {extracted_emails}")
