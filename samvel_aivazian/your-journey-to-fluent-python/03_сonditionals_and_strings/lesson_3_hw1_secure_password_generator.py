import logging
import re

logging.basicConfig(level=logging.INFO, format='%(message)s')


class PasswordChecker:
    @staticmethod
    def check_password_strength(password):
        if len(password) < 6:
            strength = "Weak"
        elif (re.search("[a-z]", password) and re.search("[A-Z]", password)
              and re.search("[0-9]", password)
              and re.search("[!@#$%^&*(),.?\":{}|<>]", password)):
            strength = "Strong"
        elif re.search("[a-zA-Z]", password) and re.search("[0-9]", password):
            strength = "Medium"
        else:
            strength = "Weak"

        logging.info(f"{strength} password")
        return strength


def main():
    logging.info("Enter a password: ")
    password = input()
    PasswordChecker.check_password_strength(password)


if __name__ == "__main__":
    main()
