import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def print_digit_sum(n):
    n = abs(n)
    digit_sum = sum(int(digit) for digit in str(n))
    logging.info(f"The sum of digits is: {digit_sum}")


if __name__ == "__main__":
    print_digit_sum(1234)
    print_digit_sum(-567)
