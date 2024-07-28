import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def get_factors(num):
    if num < 1:
        return []
    factors = [i for i in range(1, num + 1) if num % i == 0]
    return factors


if __name__ == "__main__":
    logging.info(f"Factors of 28: {get_factors(28)}")
    logging.info(f"Factors of 13: {get_factors(13)}")
    logging.info(f"Factors of 0: {get_factors(0)}")
