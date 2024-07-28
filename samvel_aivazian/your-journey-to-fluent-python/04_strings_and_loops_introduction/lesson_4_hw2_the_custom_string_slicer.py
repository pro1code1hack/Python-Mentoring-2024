import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class StringSlicer:
    def __init__(self, string, start, stop, step=None):
        self.string = string
        self.start = start
        self.stop = stop
        self.step = step

    def slice_string(self):
        if self.step:
            return self.string[self.start:self.stop:self.step]
        else:
            return self.string[self.start:self.stop]


def main():
    logging.info("Enter a string: ")
    string = input()
    logging.info("Enter start index: ")
    start = int(input())
    logging.info("Enter stop index: ")
    stop = int(input())
    logging.info("Do you want to add a step (yes/no)? ")
    add_step = input().strip().lower()

    if add_step == 'yes':
        logging.info("Enter step: ")
        step = int(input())
        slicer = StringSlicer(string, start, stop, step)
    else:
        slicer = StringSlicer(string, start, stop)

    sliced_string = slicer.slice_string()
    logging.info(f"The sliced string is: {sliced_string}")


if __name__ == "__main__":
    main()
