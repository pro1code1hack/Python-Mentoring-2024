import re

# Task 7: Mini Database
def mini_database() -> dict[str]:
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

# Task 8: Validating IP Addresses
def validate_ip(ip_str: str) -> bool:
    # Regular expression to match valid IP addresses
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    
    # Validate the IP address
    if ip_pattern.match(ip_str):
        parts = map(int, ip_str.split('.'))
        return all(0 <= part <= 254 for part in parts)
    return False

# Task 9: Email Extractor
def extract_emails(text: str) -> str:
    # Regular expression to find emails in the text
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    # Find all matching emails
    emails = email_pattern.findall(text)
    # Join the emails with semicolons
    return '; '.join(emails)


# Example for Task 7
person = mini_database()
for key, value in person.items():
    print(f"{key}: {value}")
print()

# Example for Task 8
ip_example_valid = '192.168.1.1'
ip_example_invalid = '256.300.2.-10'

valid_check = validate_ip(ip_example_valid)
print(valid_check)

invalid_check = validate_ip(ip_example_invalid)
print(invalid_check)

# Example for Task 9
text_example = "Please contact us at support@example.com or sales@example.com for assistance."
extracted_emails = extract_emails(text_example)
print(extracted_emails)