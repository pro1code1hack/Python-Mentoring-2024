import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def average_of_evens():
    logging.info("Enter a range of numbers (start and stop separated by space): ")
    start, stop = map(int, input().split())
    evens = [num for num in range(start, stop + 1) if num % 2 == 0]
    if evens:
        average = sum(evens) / len(evens)
        logging.info(f"The average of even numbers is: {average}")
    else:
        logging.info("There are no even numbers in the given range.")


if __name__ == "__main__":
    average_of_evens()
