import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class TextReverser:
    def __init__(self):
        self.lines = []

    def capture_lines(self):
        for _ in range(3):
            logging.info("Enter a line of text: ")
            line = input()
            self.lines.append(line)

    def reverse_lines(self):
        logging.info("Reversed lines:")
        for line in reversed(self.lines):
            logging.info(line)


def main():
    text_reverser = TextReverser()
    text_reverser.capture_lines()
    text_reverser.reverse_lines()


if __name__ == "__main__":
    main()
