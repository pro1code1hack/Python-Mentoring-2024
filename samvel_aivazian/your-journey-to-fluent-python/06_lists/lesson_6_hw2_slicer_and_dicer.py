import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class SlicerDicer:
    def __init__(self, numbers):
        self.numbers = numbers

    def slice_list(self, start, stop):
        sliced_list = self.numbers[start:stop]
        logging.info(f"The sliced list is: {sliced_list}")


def main():
    logging.info("Enter a list of numbers (separated by space): ")
    numbers = list(map(int, input().split()))
    logging.info(f"Input list: {numbers}")

    logging.info("Enter start index for slicing: ")
    start = int(input().strip())

    logging.info("Enter stop index for slicing: ")
    stop = int(input().strip())

    slicer_dicer = SlicerDicer(numbers)
    slicer_dicer.slice_list(start, stop)


if __name__ == "__main__":
    main()
