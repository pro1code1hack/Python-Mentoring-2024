import logging
import re

logging.basicConfig(level=logging.INFO, format='%(message)s')


def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails


def main():
    logging.info("Enter the text: ")
    text = input().strip()
    emails = extract_emails(text)
    logging.info(f"Extracted Emails: {'; '.join(emails)}")


if __name__ == "__main__":
    main()
