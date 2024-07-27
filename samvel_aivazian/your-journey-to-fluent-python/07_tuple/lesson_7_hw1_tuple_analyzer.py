import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def tuple_analyzer():
    logging.info("Enter numbers separated by commas: ")
    numbers = tuple(map(int, input().split(',')))
    logging.info(f"Tuple: {numbers}")
    logging.info(f"Sum: {sum(numbers)}")
    logging.info(f"Average: {sum(numbers) / len(numbers)}")
    logging.info(f"Maximum: {max(numbers)}")
    logging.info(f"Minimum: {min(numbers)}")


if __name__ == "__main__":
    tuple_analyzer()
