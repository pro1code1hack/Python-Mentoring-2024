import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        logging.info("Error: Cannot divide by zero.")
        return None
    else:
        return result
    finally:
        logging.info("Division attempt completed.")


if __name__ == "__main__":
    logging.info(safe_divide(10, 2))
    logging.info(safe_divide(5, 0))
