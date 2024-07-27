import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def list_operations(numbers):
    logging.info(f"Length of the list: {len(numbers)}")
    logging.info(f"Sum of the list: {sum(numbers)}")
    logging.info(f"Max of the list: {max(numbers)}")
    logging.info(f"Min of the list: {min(numbers)}")
    logging.info(f"Average of the list: {sum(numbers) / len(numbers)}")
    logging.info(f"Last element of the list: {numbers[-1]}")
    logging.info(f"List in reverse order: {numbers[::-1]}")
    logging.info(f"YES" if 4 in numbers and 9 in numbers else "NO")
    logging.info(f"List with first and last elements removed: {numbers[1:-1]}")
    logging.info(f"Third element from the end: {numbers[-3]}")
    if numbers[1] > 10:
        numbers[1] = 10
    logging.info(f"Modified list: {numbers}")


def main():
    numbers = [3, 12, 5, 8, 4, 9, 15, 22]
    list_operations(numbers)


if __name__ == "__main__":
    main()
