import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def factorial_calculator():
    logging.info("Enter a number to calculate the factorial: ")
    number = int(input().strip())
    logging.info(f"Input number: {number}")
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    logging.info(f"The factorial of {number} is {factorial}.")


if __name__ == "__main__":
    factorial_calculator()
